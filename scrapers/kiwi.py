import json
import pprint
import typing

import requests

from scrapers.models import Kiwi1, Kiwi2, Kiwi3, Kiwi4
from scrapers.utils import (add_data, add_url_date, build_dates,
                            check_url_date, get_date, make_session)

cookies = {
    "kiwiSecure": "99f4d90b2c3faaf34ce057f22c45a571",
    "SnapABugRef": "https%3A%2F%2Fwww.kiwicollection.com%2F%20",
    "SnapABugHistory": "1#",
    "SnapABugVisit": "2#1682949908",
    "SnapABugUserAlias": "%23",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-GB,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}

params = {
    "geolocationId": "1733",
    "hasKiwiPerks": "",
    "hasVisaPerks": "",
    "wowPick": "",
    "starRating": "",
    "brandIds[]": "",
    "affiliateIds[]": "",
}


headers2 = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-GB,en;q=0.5",
    "Origin": "https://www.kiwicollection.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}


def process_bool(data):
    for d in data.__annotations__:
        if data.__annotations__[d] is typing.Optional[bool] or bool:
            if getattr(data, d) == "":
                setattr(data, d, False)

    return data


def process_l1(session, location_ids, debug=False):
    for l in location_ids:
        print(f"processing id {l}")
        par = {**params}
        par["geolocationId"] = l
        response = requests.get(
            "https://www.kiwicollection.com/maps/coordinates",
            params=params,
            cookies=cookies,
            headers=headers,
        )

        if len(response.content):
            res = json.loads(response.content)
            process_l2(session, res.pop("features"), debug=debug)
            print(f"processing id {l}, done...")


def process_l2(session, data, debug=False):
    for d in data:
        print("processing")

        if debug:
            print(d)

        obj = d.get("object", None)

        if obj is not None:
            prop_id = obj.get("propertyId", None)
            if prop_id is not None:
                for date_from, date_to in build_dates():
                    url = f"https://www.kiwicollection.com/rooms/availability/embed/{prop_id}/{date_from:%Y-%m-%d}/{date_to:%Y-%m-%d}/2/0/1"

                    if not check_url_date(session, url, get_date()):
                        print(f"processing: {url}")
                        response = requests.post(
                            url,
                            cookies=cookies,
                            headers=headers,
                        )
                        if len(response.content):
                            data = json.loads(response.content)
                            rooms = data.pop("rooms", None)
                            if rooms is not None and len(rooms) != 0:
                                if debug:
                                    pprint.pprint(data)
                                data.pop("analytics")
                                data.pop("alerts")
                                for c in [
                                    "childrenAges",
                                    "otherPropertiesAvailable",
                                    "propertyAvailabilityCriteria",
                                    "selectedSpecialOfferRooms",
                                    "specialOfferRooms",
                                ]:
                                    data[c] = {"data": data[c]}

                                k2 = Kiwi2(**data)
                                add_data(session, None, k2, check_date=False)
                                print("added l2")
                                process_l3(session, rooms, k2.id, debug=debug)
                            else:
                                print("rooms empty")
                        else:
                            print("response is empty")

                        add_url_date(session, url, get_date())

                    else:
                        print(f"url exists {url}, skipping...")
                d['type'] = {'type': d['type']}
                k1 = Kiwi1(**d)
                add_data(session, None, k1, check_date=False)
                print(f"hotel {prop_id} processed")


def process_l3(session, data, id, debug=False):
    print("processing l3")
    if debug:
        pprint.pprint(data)
    for d in data:
        if debug:
            pprint.pprint(d)
        rates = d.pop("rates", None)
        if rates is not None and len(rates) != 0:
            for c in ["allImages", "extraImages"]:
                d[c] = {"data": d[c]}

            k3 = Kiwi3(**d, kiwi_l2_id=id)
            add_data(session, None, k3, check_date=False)
            process_l4(session, rates, k3.id, debug=debug)
            print("processing l3 done")
        else:
            print("rates is empty")
    return True


def process_l4(session, data, id, debug=False):
    print("processing l4")
    for d in data:
        for c in [
            "amenities",
            "benefitCollections",
            "consolidatedFeesTaxes",
            "nightlyCostsInfo",
        ]:
            d[c] = {"data": d[c]}

        if debug:
            pprint.pprint(d)
        if isinstance(d["specialOffer"], str):
            d["specialOffer"] = {"data": d["specialOffer"]}
        k4 = Kiwi4(kiwi_l3_id=id, **d)
        k4 = process_bool(k4)

        add_data(session, None, k4, check_date=False)
        print("processing l4 done")
    return True


def main(connection, debug, **kwargs):
    session = make_session(connection)
    session.expire_on_commit = False
    process_l1(session, [226, 814, 1, 188, 178, 694, 1906, 2032, 2070], debug)
