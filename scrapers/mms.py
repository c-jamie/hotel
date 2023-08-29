"""Module provides MMS web scraper."""
import urllib3
import datetime as dt
import re
import time
from collections import defaultdict
from datetime import timedelta

import cloudscraper
import pandas as pd
import requests
import sqlalchemy
from bs4 import BeautifulSoup
from requests import Request
from requests.adapters import HTTPAdapter, Retry

from scrapers import models
from scrapers.models import Api
from scrapers.utils import build_dates, make_session

URL_BASE_HOTELS = "https://www.mrandmrssmith.com/destinations/{region}/{area}/hotels"

SESSION = requests.session()

RETRIES = Retry(total=10, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])

SESSION.mount("http://", HTTPAdapter(max_retries=RETRIES))
SESSION.mount("https://", HTTPAdapter(max_retries=RETRIES))

CLOUD_SCRAPER = cloudscraper.create_scraper(
    browser={"browser": "firefox", "platform": "windows", "mobile": False}, delay=10
)


def make_url(url, **kwargs):
    url_db = Request("GET", url, **kwargs).prepare()

    return url_db.url


class Scraper:
    """Scraper."""

    def __init__(self, session=None):
        self.session = session
        self.date = None

    def get(self, *args, **kwargs):
        if self.session is not None:
            url = make_url(args[0], **kwargs)
            assert self.date is not None

            try:
                db_date = self.date - timedelta(days=self.date.weekday())
                self.session.query(models.Api).filter_by(url=url, date=db_date).one()
                exists = True
            except sqlalchemy.exc.MultipleResultsFound:
                exists = True
            except sqlalchemy.exc.NoResultFound:
                exists = False
            self.session.close()
            return exists, CLOUD_SCRAPER.get(args[0], **kwargs)
        return False, CLOUD_SCRAPER.get(*args, **kwargs)


def deep_price(scraper, hotel, from_date, to_date, top_name, top_id):
    params = {
        # 's[date_from]':None,
        # 's[date_to]':None,
        "s[sort_field]": "price",
        "s[sort_direction]": "asc",
    }
    url_base = f"https://www.mrandmrssmith.com/luxury-hotels/{hotel}/rooms"

    _, response = scraper.get(
        url_base,
        params={**params, **{"s[date_to]": to_date, "s[date_from]": from_date}},
    )

    wp = BeautifulSoup(response.text, "html.parser")
    rooms = wp.find_all("div", attrs={"data-section": True})
    out = defaultdict(list)
    for room in rooms:
        if room["data-room-availability"] == "available":
            name = room.find_all("h2")[0].text
            prices = room.find_all("article", class_="ratecard")
            for price in prices:
                total = price.find("span", class_="totalPrice")
                if total is None:
                    print("no price found")
                    print(price)
                    continue
                is_offer = "as-offer" in price["class"]
                non_refund_hb = price.find_all("h4")[0].text
                hb = price.find_all("p")[0].text.strip()
                for attr in ["data-rate-currency", "data-rate-inc", "data-rate-ex"]:
                    total = price.find("span", class_="totalPrice").find(
                        "span", attrs={attr: True}
                    )
                    night = price.find("span", class_="nightPrice").find(
                        "span", attrs={attr: True}
                    )
                    is_offer = "as-offer" in price["class"]
                    total_display = None
                    night_display = None
                    total_display_offer = None
                    night_display_offer = None
                    if is_offer:
                        night_offer = price.find_all("span", class_="nightPrice")[
                            -1
                        ].find("span", attrs={attr: True})
                        out[attr + "-total-price-offer"].append(total[attr])
                        out[attr + "-night-price-offer"].append(night_offer[attr])
                        out[attr + "-total-price-original"].append(None)
                        out[attr + "-night-price-original"].append(night[attr])
                        total_display = None
                        total_display_offer = total.text
                        night_display = night.text
                        night_display_offer = night_offer.text
                    else:
                        out[attr + "-total-price-offer"].append(None)
                        out[attr + "-night-price-offer"].append(None)
                        out[attr + "-total-price-original"].append(total[attr])
                        out[attr + "-night-price-original"].append(night[attr])
                        total_display = total.text
                        total_display_offer = None
                        night_display = night.text
                        night_display_offer = None
                out["display-night-price-offer"].append(night_display_offer)
                out["display-night-price-original"].append(night_display)
                out["display-total-price-offer"].append(total_display_offer)
                out["display-total-price-original"].append(total_display)
                out["is_offer"].append(is_offer)
                out["is_available"].append(True)
                out["time_stamp"].append(dt.datetime.now())
                out["room_info_raw"].append(non_refund_hb)
                out["board_raw"].append(hb)
                out["hotel_name"].append(hotel)
                out["name"].append(name)
                out["from"].append(from_date)
                out["to"].append(to_date)

        else:
            out["data-rate-currency-total-price-original"].append(None)
            out["data-rate-currency-night-price-original"].append(None)
            out["data-rate-inc-total-price-original"].append(None)
            out["data-rate-inc-night-price-original"].append(None)
            out["data-rate-ex-total-price-original"].append(None)
            out["data-rate-ex-night-price-original"].append(None)
            out["data-rate-currency-total-price-offer"].append(None)
            out["data-rate-currency-night-price-offer"].append(None)
            out["data-rate-inc-total-price-offer"].append(None)
            out["data-rate-inc-night-price-offer"].append(None)
            out["data-rate-ex-total-price-offer"].append(None)
            out["data-rate-ex-night-price-offer"].append(None)
            out["room_info_raw"].append(None)
            out["board_raw"].append(None)
            out["name"].append(room.find_all("h2")[0].text)
            out["hotel_name"].append(hotel)
            out["time_stamp"].append(dt.datetime.now())
            out["is_available"].append(False)
            out["is_offer"].append(False)
            out["display-night-price-offer"].append(None)
            out["display-night-price-original"].append(None)
            out["display-total-price-offer"].append(None)
            out["display-total-price-original"].append(None)
            out["from"].append(from_date)
            out["to"].append(to_date)

    out = pd.DataFrame(out)
    out["top_name"] = top_name
    out["top_id"] = top_id
    return out


def extract_data(data):
    out = {}
    # name
    name_html = data.find("div", attrs={"data-id": True})
    for v in ["data-id", "data-lat", "data-long", "data-name", "data-prop"]:
        out[v] = name_html[v]
    # location
    loc_html = data.find_all("span", attrs={"data-tags": True})
    for v in loc_html:
        out[v.get("class")[-1]] = v["data-tags"]
    try:
        # price
        price_html = data.find("span", attrs={"data-rate-ex": True})
        for v in ["data-rate-currency", "data-rate-ex", "data-rate-inc"]:
            out[v] = price_html[v]
    except TypeError:
        out["data-rate-currency"] = None
        out["data-rate-ex"] = None
        out["data-rate-inc"] = None

    desc = data.select(".accomodation-description > p")

    try: 
        out['style'] = desc[0].text
    except IndexError:
        out['style'] = ""
    
    try:
        out['setting'] = desc[1].text
    except IndexError:
        out['setting'] = ""

    return out


def load_data(scraper, region, area, dates):
    out_top_level = []
    out_deep_price = []
    params = {}
    for date in dates:
        for p in range(1, 20):
            params["s[date_from]"] = date[0].date()
            params["s[date_to]"] = date[1].date()
            params["page"] = p
            url_base = URL_BASE_HOTELS.format(region=region, area=area)
            try:
                exists, response = scraper.get(url_base, params=params)
            except urllib3.exceptions.ProtocolError as e:
                print("ERROR: connection")
                print(f"{e}")
                time.sleep(60 * 30)
                exists, response = scraper.get(url_base, params=params)
            url_db = make_url(url_base, **{"params": params})
            if not exists:
                print("loading: ", response.url)
                wp = BeautifulSoup(response.text, "html.parser")
                _data = wp.find(id="search-list")
                if _data is not None:
                    data = _data.find_all("li", "result")
                    data_df = pd.DataFrame([extract_data(k) for k in data])
                    data_df["timestamp"] = dt.datetime.now()
                    data_df["from"] = date[0]
                    data_df["to"] = date[1]
                    data_df["url"] = response.url
                    data_df[["data-rate-ex", "data-rate-inc"]] = data_df[
                        ["data-rate-ex", "data-rate-inc"]
                    ].astype(float)
                    deep_px = []
                    for d in data:
                        _data = extract_data(d)
                        link = d.find("a", attrs={"href": True})["href"]
                        try:
                            name = re.findall(
                                "(?<=https://www.mrandmrssmith.com/luxury-hotels/).*?(?=/rooms?)",
                                link,
                            )[0]
                            top_level_name = _data["data-name"]
                            top_level_id = _data["data-id"]
                            dp = deep_price(
                                scraper,
                                name,
                                date[0].date(),
                                date[1].date(),
                                top_level_name,
                                top_level_id,
                            )
                            deep_px.append(dp)
                            out_deep_price.append(dp)
                        except Exception as e:
                            print("error - skipping", e)
                    time.sleep(2)
                    out_top_level.append(data_df)

                    if scraper.session is not None:
                        print(f"adding mms_lite for {response.url}")
                        data_df.columns = [c.replace("-", "_") for c in data_df.columns]
                        data_df.to_sql(
                            "mms_lite",
                            con=scraper.session.get_bind(),
                            if_exists="append",
                            index=False,
                        )

                        if len(deep_px) > 0:
                            data_deep_df = pd.concat(deep_px, ignore_index=True)
                            data_deep_df.columns = [
                                c.replace("-", "_") for c in data_deep_df.columns
                            ]
                            data_deep_df.to_sql(
                                "mms_deep",
                                con=scraper.session.get_bind(),
                                if_exists="append",
                                index=False,
                            )
                            print(f"added mms_deep {len(data_deep_df)} rows")
                        else:
                            print("no deep prices found")

                        db_date = scraper.date - timedelta(days=scraper.date.weekday())
                        scraper.session.add(Api(name="mms", url=url_db, date=db_date))
                        scraper.session.commit()
                        scraper.session.close()
                        print("added to Api")
                else:
                    print("end of page")
                    break
            else:
                print(f"already scraped: {region} {area} {params}")

    if len(out_top_level) > 0:
        df_tl = pd.concat(out_top_level, ignore_index=True)
    else:
        df_tl = pd.DataFrame()

    if len(out_deep_price) > 0:
        df_dp = pd.concat(out_deep_price, ignore_index=True)
    else:
        df_dp = pd.DataFrame()

    return df_tl, df_dp


def build_all_regions(num_regions=None, num_dates=None, scraper=None):
    assert scraper is not None

    if scraper.session is not None:
        scraper.date = dt.date.today()
    else:
        print("no session")

    regions = [
        ("greece", "greece"),
        ("italy", "italy"),
        ("spain,", "spain"),
        ("morocco", "moocco"),
        ("turkey", "turkey"),
        ("montenegro", "montenegro"),
        ("croatia", "croatia"),
        ("portgual", "portgual"),
        ("cyprus", "cyprus"),
        ("france", "france"),
        ("united-kingdom", "united-kingdom"),
    ]

    dates = build_dates()

    if num_dates is not None:
        dates = dates[:num_dates]

    if num_regions is not None:
        regions = regions[:num_regions]

    for region, area in regions:
        print("pulling: ", region, area)
        top_level_df, deep_price_df = load_data(scraper, region, area, dates)
        print(f"loaded {len(top_level_df)} {len(deep_price_df)} for {area} {region}")


def main(num_regions, num_dates, connection):
    session = make_session(connection)
    scraper = Scraper(session=session)
    build_all_regions(
        num_regions=num_regions,
        num_dates=num_dates,
        scraper=scraper,
    )
    print("ALL DONE")
