from pathlib import Path

import cloudscraper
import pandas as pd
import sqlalchemy
from bs4 import BeautifulSoup
from requests import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from scrapers import db, models
from scrapers.mms import build_all_regions
from scrapers.models import Api

CLOUD_SCRAPER = cloudscraper.create_scraper(
    browser={"browser": "firefox", "platform": "windows", "mobile": False},
)


BASE_PATH = Path(__file__).parent.absolute()


class MockReq:
    def __init__(self, text):
        self.text = text
        self.url = ""


def save_to_file(name, text):

    with open(BASE_PATH / "resources" / f"{name}.txt", "w") as file:
        file.write(text)
        print("saved")


def read_from_file(name):
    with open(BASE_PATH / "resources" / f"{name}.txt", "r") as file:
        return file.read()


def try_cache(url_db, url, **kwargs):

    try:

        d = read_from_file(hash(url))
        d = MockReq(text=d)

    except IOError:
        print("cache miss")

    d = CLOUD_SCRAPER.get(url, **kwargs)

    save_to_file(hash(url_db), d.text)

    return d


class Scraper:
    """Scraper."""

    def __init__(self):
        self.session = None
        self.date = None
        self.use_cache = True

    def get(self, *args, **kwargs):

        url_db = Request("GET", args[0], **kwargs).prepare().url
        if self.session is not None:
            assert self.date is not None

            try:
                self.session.query(models.Api).filter_by(
                    url=url_db, date=self.date
                ).one()
                exists = True
            except sqlalchemy.exc.MultipleResultsFound:
                exists = True
            except sqlalchemy.exc.NoResultFound:
                exists = False

            return exists, try_cache(url_db, args[0], **kwargs)
        return False, try_cache(url_db, *args, **kwargs)


def test_mms_integration(pytestconfig, database_session):

    from datetime import date

    scraper = Scraper()
    scraper.session = database_session
    scraper.date = date.today()

    connection = pytestconfig.getoption("url")
    build_all_regions(connection, 1, 1, scraper)
