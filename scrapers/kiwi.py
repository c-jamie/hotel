import datetime as dt
import json
import re
import sqlite3
from collections import defaultdict

import pandas as pd
import requests
from bs4 import BeautifulSoup
from utils import BASE, build_dates


def parse_data(url):
    print("entering parse")
    response = requests.get(url)
    wp = BeautifulSoup(response.text, "html.parser")
    for v in wp.find_all("script"):
        if v.string is not None:
            if "initRoomsData" in v.string:
                ak = v.string
    hotel_name = re.findall(
        r"(?<=hotel-detail/)(.*)(?=/\d{4}-\d{2}-\d{2}/\d{4}-\d{2}-\d{2})", url
    )[-1]
    p = re.compile("(?<=var initRoomsData =)(.*)(?=;)")
    parsed = p.findall(ak)
    return json.loads(parsed[0].strip()), hotel_name


def level_two_prices(data, name, room):
    for k in data:
        k.pop("nightlyCostsInfo")
        k.pop("allowedCreditCards")
        k.pop("benefitCollections")
        fees = k.pop("consolidatedFeesTaxes")
        if fees is not None:
            fee = ""
            for f in fees:
                fee += str(f)
            k["fees"] = fee
        else:
            k["fees"] = ""
        k["amenities"] = "|".join([list(a.values())[-1]
                                  for a in k.pop("amenities")])
    out = pd.DataFrame(data)
    out["name"] = name
    out["rooom"] = room
    return out


def level_one_prices(rooms, name, room_type="rooms"):
    level_two = []
    for room in rooms[room_type]:
        # room = rooms['rooms']
        level_two.append(level_two_prices(
            room.pop("rates"), name, room["title"]))
        room.pop("allImages")
        for k in ["primaryImage"]:
            image = ""
            if room[k] is not None:
                for p in room[k].keys():
                    if p not in ("paths"):
                        # import pdb; pdb.set_trace()
                        if room[k][p] is not None:
                            image += "|" + k + p + "=" + room[k][p]
                    else:
                        for q in room[k]["paths"].keys():
                            image += "|" + k + "paths" + \
                                q + "=" + room[k]["paths"][q]
            room.pop(k)
            room["image"] = image
        room.pop("extraImages")
        room["roomSize"] = str(room["roomSize"])

    out = pd.DataFrame(rooms[room_type])
    out["name"] = name
    return out, pd.concat(level_two)


def load_region(region):
    url = (
        url
    ) = """https://www.kiwicollection.com/search?numAdults=2&numChildren=0&rows=50&page={page}&sortBy=relevancy&getSpecialOffers=1&keyword={region}&inDate=2020-04-04&outDate=2020-04-11"""
    out = defaultdict(list)

    def _grab(box, out):
        # link
        link = box.find("a", attrs={"href": True})["href"]
        # name
        name = box.find("a", class_="results-list-item-link").text.strip()
        # rooms
        rooms = (
            box.find(
                "ul", class_="hotel-information").find_all("li")[0].text.strip()
        )
        # setting
        try:
            setting = (
                box.find("ul", class_="hotel-information")
                .find_all("li")[1]
                .text.strip()
            )
        except:
            setting = None
        # style
        try:
            style = (
                box.find("ul", class_="hotel-information")
                .find_all("li")[2]
                .text.strip()
            )
        except:
            style = None
        # teaser
        teaser = box.find("p", class_="teaser").text
        # location
        location = box.find("span", class_="results-list-location").text
        # rating
        try:
            rating = box.find("span", class_="rate-number").text
        except:
            print("error ", name)
            rating = None
        print("processed ", name)

        out["link"].append(link)
        out["name"].append(name)
        out["rooms"].append(rooms)
        out["setting"].append(setting)
        out["style"].append(style)
        out["teaser"].append(teaser)
        out["location"].append(location)
        out["rating"].append(rating)

        return out

    response = requests.get(url.format(region=region, page=1))
    wp = BeautifulSoup(response.text, "html.parser")
    results = int(
        wp.find("div", class_="heading-sub-tag").text.strip().split(" ")[0])
    pages = (results // 50) + 1

    hotels = wp.find_all("li", class_="results-list-item")
    for hotel in hotels:
        _grab(hotel, out)

    for page in range(2, pages + 1):
        print("processing", page)
        response = requests.get(url.format(region=region, page=page))
        wp = BeautifulSoup(response.text, "html.parser")

        hotels = wp.find_all("li", class_="results-list-item")
        for hotel in hotels:
            _grab(hotel, out)
    out = pd.DataFrame(out)
    out["search_region"] = region
    return out


def process_hotels(data, conn):
    dates = build_dates()
    base = "https://www.kiwicollection.com"
    for u in data.itertuples(index=False):
        level_one = []
        level_two = []
        print("processing...", u.link)
        for d in dates:
            url = base + u.link
            url = re.sub(
                r"\d{4}-\d{2}-\d{2}/\d{4}-\d{2}-\d{2}",
                d[0].strftime("%Y-%m-%d") + "/" + d[1].strftime("%Y-%m-%d"),
                url,
            )
            try:
                print("building...", url)
                raw_data, name = parse_data(url)
                l1, l2 = level_one_prices(raw_data, name)

                l1["date_from"] = d[0]
                l1["date_from"] = d[1]

                l2["date_to"] = d[0]
                l2["date_to"] = d[1]

                l1["time_stamp"] = dt.datetime.now()
                l2["time_stamp"] = dt.datetime.now()

                level_one.append(l1)
                level_two.append(l2)
            except:
                print("unable to process ", url)

        if level_one:
            try:
                pd.concat(level_one).to_sql(
                    "kiwi_level_one", conn, if_exists="append")
                print("l1 loaded to database")
            except Exception as e:
                print("unable to load L1 {}".format(u.link))
                print("error: ".format(str(e)))

            try:
                pd.concat(level_two).to_sql(
                    "kiwi_level_two", conn, if_exists="append")
                print("l2 loaded to database")
            except Exception as e:
                print("unable to load L2 {}".format(u.link))
                print("error: ".format(str(e)))

        print("processed...", u.link)

    return True


def build_all_regions():
    conn = sqlite3.connect(str(BASE / "hotel.db"))
    data = [
        "Italy",
        "Greece",
        "Spain",
        "Morocco",
        "France",
        "Portugal",
        "Montenegro",
        "Cyprus",
    ]
    out = []
    for country in data:
        try:
            print("#" * 20, "building... ", country)
            regions = load_region(country)
            out = process_hotels(regions, conn)
            print("#" * 20, "finished...", country)
        except Exception as e:
            print("error", e)
            pass


if __name__ == "__main__":
    build_all_regions()
