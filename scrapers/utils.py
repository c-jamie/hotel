import datetime as dt
import os
from datetime import timedelta
from pathlib import Path

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from scrapers import models
from scrapers.db import start_mappers
from scrapers.models import Api


def make_session(connection):
    start_mappers()
    engine = create_engine(
        connection, echo=False, pool_pre_ping=True, pool_recycle=60 * 5
    )
    database_session = sessionmaker(bind=engine)()
    return database_session


def build_dates():
    date_rng = pd.date_range(
        dt.date.today() + dt.timedelta(60), freq="W-SAT", periods=35
    )
    date_1 = date_rng[::1]
    date_2 = date_rng[1::1]
    return list(zip(date_1, date_2))


TODAY = dt.date.today()


def get_date():
    return TODAY - timedelta(days=TODAY.weekday())


BASE = Path(os.path.dirname(os.path.abspath(__file__)))


def check_url_date(session, url, date):
    try:
        session.query(models.Api).filter_by(url=url, date=date).one()
        exists = True
    except sqlalchemy.exc.MultipleResultsFound:
        exists = True
    except sqlalchemy.exc.NoResultFound:
        exists = False
    return exists


def add_url_date(session, url, date, name="virtuoso"):
    session.add(
        Api(
            name=name,
            url=url,
            date=date,
        )
    )
    session.commit()


def add_data(session, url, data, check_date=True):
    db_date = get_date()

    if check_date:
        print("date check")
        exists = check_url_date(session, url, db_date)

    else:
        print("no date check")
        exists = False

    if not exists:
        print(f"doesn't exist for {db_date}, adding {url}")
        session.add(data)
        session.commit()

        session.add(Api(name="virtuoso", url=url, date=db_date))
        session.commit()

    else:
        print(f"exists for {db_date}, {url}, nothing to do")

    session.close()
    return exists
