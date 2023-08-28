import json
import pprint
import re
import time
from datetime import datetime

import requests

from scrapers.models import Virtuoso1, Virtuoso2
from scrapers.utils import (add_data, add_url_date, build_dates,
                            check_url_date, get_date, make_session)

cookies = {
    "ApplicationGatewayAffinityProCORS": "cbaa8e3ffccf0de949518d7dd1470bd7",
    "ApplicationGatewayAffinityPro": "cbaa8e3ffccf0de949518d7dd1470bd7",
    ".AspNetCore.Session": "CfDJ8JpuCUHCamVMjEaxOtPKe5CoMxSKJveKrGyYDRTSGHtRa6W8y43AkCUFpyFReMbseopZS6L0S%2FsPsTUllh0l6y69TvPzTJzdMoO2eSSa3mBugE5w6SJThxpnB3fMDtH8BH%2Fg5%2Bw85Vix35A%2BliXsaEzreq01GtNsoSK2%2FyEzthbm",
    "OptanonConsent": "isIABGlobal=false&datestamp=Mon+Apr+17+2023+20%3A29%3A51+GMT%2B0100+(British+Summer+Time)&version=6.20.0&hosts=&landingPath=NotLandingPage&groups=C0005%3A0%2CC0001%3A1%2CC0007%3A0%2CC0008%3A0&geolocation=GB%3BENG&AwaitingReconsent=false",
    "OptanonAlertBoxClosed": "2023-04-17T19:29:20.110Z",
    "CookiesEnabled": "true",
    "slc": "boXaq4QNpY+Kh8bfR9i/RMT7kQmi+cN20w6Bd8PevopTfSOcZ05YTNYoe2TXufFJlFlvOP6f1YvtvqgOLGYZKYip33yFTwp8TCJi2Idp8JXfwotlw3Ik6Y8zxpbfhtxx",
    "CMSPreferredCulture": "en-US",
    "ASP.NET_SessionId": "iihvtvu4551y4cvgd0jatcwj",
    "ATC": "LastLoggedInAs=Anonymous&HasLoggedInBefore=0&SessionId=iihvtvu4551y4cvgd0jatcwj",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-GB,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.virtuoso.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.virtuoso.com/hotels",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
}

json_data = {
    "options": {
        "ClientSideOptions": {
            "CurrentPage": 1,
            "FacetCategoryIndex": 0,
            "FacetCategoryTitle": "",
            "FacetLimit": 6,
            "LeftToShow": 0,
            "ProductIds": [],
            "RowsPerPage": 25,
            "SearchMode": "",
            "SearchTerms": "",
            "SearchView": "1col",
            "SelectedFacets": [],
            "StartRow": 0,
            "HotelBookingNumberChildren": 0,
            "HotelBookingNumberAdults": 2,
            "HotelBookingCheckinDate": None,
            "HotelBookingCheckoutDate": None,
            "SearchType": "Property",
            "SortType": "HotelNameAsc",
        },
    },
}


cookies_2 = {
    "ApplicationGatewayAffinityProCORS": "cbaa8e3ffccf0de949518d7dd1470bd7",
    "ApplicationGatewayAffinityPro": "cbaa8e3ffccf0de949518d7dd1470bd7",
    ".AspNetCore.Session": "CfDJ8JpuCUHCamVMjEaxOtPKe5CoMxSKJveKrGyYDRTSGHtRa6W8y43AkCUFpyFReMbseopZS6L0S%2FsPsTUllh0l6y69TvPzTJzdMoO2eSSa3mBugE5w6SJThxpnB3fMDtH8BH%2Fg5%2Bw85Vix35A%2BliXsaEzreq01GtNsoSK2%2FyEzthbm",
    "OptanonConsent": "isIABGlobal=false&datestamp=Mon+Apr+17+2023+21%3A00%3A59+GMT%2B0100+(British+Summer+Time)&version=6.20.0&hosts=&landingPath=NotLandingPage&groups=C0005%3A0%2CC0001%3A1%2CC0007%3A0%2CC0008%3A0&geolocation=GB%3BENG&AwaitingReconsent=false",
    "OptanonAlertBoxClosed": "2023-04-17T19:29:20.110Z",
    "CookiesEnabled": "true",
    "slc": "boXaq4QNpY+Kh8bfR9i/RMT7kQmi+cN20w6Bd8PevopTfSOcZ05YTNYoe2TXufFJlFlvOP6f1YvtvqgOLGYZKYip33yFTwp8TCJi2Idp8JXfwotlw3Ik6Y8zxpbfhtxx",
    "CMSPreferredCulture": "en-US",
    "ASP.NET_SessionId": "iihvtvu4551y4cvgd0jatcwj",
    "ATC": "LastLoggedInAs=Anonymous&HasLoggedInBefore=0&SessionId=iihvtvu4551y4cvgd0jatcwj",
    "__RequestVerificationToken": "DIDhvmaJpbiJE5NrUKqOuW4rjPMTl76jDeHNlkIWO3GRBJvDLskW-s4OkYQ7_aJc-I_duyT3Tas1QBL_2jARirtQgwTfQXg3V8xxROBfBFM1",
}

headers_2 = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Accept": "*/*",
    "Accept-Language": "en-GB,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.virtuoso.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.virtuoso.com/hotels/14949727/auberge-du-jeu-de-paume-chantilly-relais-chateaux",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
}

data_2 = {
    "PropertySabreId": "167410",
    "HotelSupplierMeid": "14943144",
    "PropertyMeid": "14949727",
    "HotelPrimaryEmailAddress": "",
    "HotelPrimaryPhone": "33 344655000",
    "DetailUrl": "https://www.virtuoso.com/hotels/14949727/auberge-du-jeu-de-paume-chantilly-relais-chateaux#HotelBookingCheckinDate=2023-07-22&HotelBookingCheckoutDate=2023-07-29",
    "CheckinDate": "22 Jul 2023",
    "CheckoutDate": "29 Jul 2023",
    "NumberOfGuests": "2",
    "NumberOfAdults": "2",
    "NumberOfChildren": "0",
    "ShowFullRates": "true",
    "GoogleAnalyticsModel.EventName": "option_details",
    "GoogleAnalyticsModel.ItemId": "14949727",
    "GoogleAnalyticsModel.ItemName": "Auberge du Jeu de Paume, Chantilly, Relais & Chateaux",
    "GoogleAnalyticsModel.Coupon": "",
    "GoogleAnalyticsModel.ItemCategory": "Hotel",
    "GoogleAnalyticsModel.ItemCategory2": "8",
    "GoogleAnalyticsModel.ItemCategory3": "Sophisticated",
    "GoogleAnalyticsModel.ItemCategory4": "",
    "GoogleAnalyticsModel.ItemCategory5": "",
    "GoogleAnalyticsModel.ItemVariant": "Indigenous",
    "GoogleAnalyticsModel.Quantity": "0",
}


script_regex = re.compile(r"<script>(.*?)</script>", re.DOTALL)


def main(connection, debug, lim, lim_dates=None):
    session = make_session(connection)
    for i in range(1, 200):
        d = {**json_data}
        d["options"]["ClientSideOptions"]["CurrentPage"] = i
        d["options"]["ClientSideOptions"]["RowsPerPage"] = 50
        d["options"]["ClientSideOptions"]["StartRow"] = i * 50
        time.sleep(5)

        try:
            response = requests.post(
                "https://www.virtuoso.com/hotels/GetSearchView",
                cookies=cookies,
                headers=headers,
                json=d,
            )
        except urllib3.exceptions.ProtocolError as e:
            print("ERROR: connection")
            print(f"{e}")
            time.sleep(60*30)
            response = requests.post(
                "https://www.virtuoso.com/hotels/GetSearchView",
                cookies=cookies,
                headers=headers,
                json=d,
            )
        data = json.loads(response.content)
        hotels = data.get("Hotels", None)

        if debug:
            import pprint
            pprint.pprint(hotels)

        if lim is not None:
            hotels = hotels[:lim]

        if hotels is not None:
            for d in hotels:
                for cj in ["Experiences"]:
                    d[cj] = {"data": d[cj]}
                for cj in ["CityStateCountry"]:
                    d[cj] = json.loads(d[cj])

                data_virt_1 = Virtuoso1(**d)

                add_data(
                    session=session,
                    url="https://www.virtuoso.com/hotels/GetSearchView",
                    data=data_virt_1,
                    check_date=False,
                )

                dates = build_dates()

                if lim_dates is not None:
                    dates = dates[:lim_dates]

                for date_from, date_to in dates:
                    data_req = {**data_2}

                    data_req["PropertySabreId"] = d["PropertySabreId"]
                    data_req["HotelSupplierMeid"] = d["SupplierId"]
                    data_req["PropertyMeid"] = d["Id"]
                    data_req["DetailUrl"] = f"https://www.virtuso.com{d['DetailUrl']}"
                    data_req["CheckinDate"] = date_from.strftime("%d %b %Y")
                    data_req["CheckoutDate"] = date_to.strftime("%d %b %Y")

                    url_db = f"https://www.virtuoso.com{d['DetailUrl']}#HotelBookingCheckinDate={date_from:%Y-%m-%d}&HotelBookingCheckoutDate={date_to:%Y-%m-%d}"

                    print(f"url: {url_db}")
                    if debug:
                        pprint.pprint(data_req)

                    with requests.Session() as s:
                        s.get("http://www.virtuoso.com")

                        response = s.post(
                            "https://www.virtuoso.com/hotels/ajax/DisplayHotelRoomsRateList",
                            data=data_req,
                            cookies=cookies_2,
                            headers=headers_2,
                        )

                    if response.status_code != 200:
                        print(f"skipping {response.status_code}: {url_db}")
                        continue

                    if not check_url_date(session, url_db, get_date()):
                        if len(response.content):
                            scripts = script_regex.findall(
                                str(response.content))
                            scr = (
                                scripts[0]
                                .replace("tp.ServerSideData.add(\\'rateList\\',\\'", "")
                                .replace("\\');", "")
                            )

                            scr = (
                                scr.encode().decode(
                                    "utf-8").replace("\\x", "[ESCAPEx]")
                            )

                            print(scr)
                            data_virt = json.loads(scr)

                            for dv in data_virt:
                                if debug:
                                    pprint.pprint(dv)
                                dv["url"] = url_db
                                dv["date"] = datetime.now()
                                data_virt_2 = Virtuoso2(**dv, start_date=date_from, end_date=date_to)

                                add_data(
                                    session=session,
                                    url=dv["url"],
                                    data=data_virt_2,
                                    check_date=False,
                                )
                            add_url_date(session, url_db, get_date())

                        else:
                            print("no data returned")
                    else:
                        print("url already exists")

        else:
            print("hotels are none skipping")
