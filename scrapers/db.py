import sqlalchemy
from sqlalchemy import (Boolean, Column, DateTime, Integer, MetaData, Numeric,
                        String, Table)
from sqlalchemy.orm import mapper
from sqlalchemy_json import MutableJson

from scrapers import models

metadata = MetaData()

api = Table(
    "api",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(256), nullable=True),
    Column("url", String(512), nullable=True),
    Column("date", DateTime, nullable=True),
    Column("meta", MutableJson, nullable=True),
)

"""
 0   data-id             100 non-null    object
 1   data-lat            100 non-null    object
 2   data-long           100 non-null    object
 3   data-name           100 non-null    object
 4   data-prop           100 non-null    object
 5   location            100 non-null    object
 6   country             100 non-null    object
 7   data-rate-currency  19 non-null     object
 8   data-rate-ex        19 non-null     float64
 9   data-rate-inc       19 non-null     float64
 10  timestamp           100 non-null    datetime64[ns]
 11  from                100 non-null    datetime64[ns]
 12  to                  100 non-null    datetime64[ns]
 13  url
"""

mms_lite = Table(
    "mms_lite",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("data_id", String(256), nullable=True),
    Column("data_lat", String(256), nullable=True),
    Column("data_long", String(256), nullable=True),
    Column("data_name", String(256), nullable=True),
    Column("data_prop", String(256), nullable=True),
    Column("location", String(256), nullable=True),
    Column("country", String(256), nullable=True),
    Column("data_rate_currency", String(256), nullable=True),
    Column("data_rate_ex", Numeric(18, 6), nullable=True),
    Column("data_rate_inc", Numeric(18, 6), nullable=True),
    Column("timestamp", DateTime, nullable=True),
    Column("from", DateTime, nullable=True),
    Column("to", DateTime, nullable=True),
    Column("url", String(512), nullable=True),
)


"""
 0   data-rate-currency-total-price-offer     60 non-null     object
 1   data-rate-currency-night-price-offer     60 non-null     object
 2   data-rate-currency-total-price-original  199 non-null    object
 3   data-rate-currency-night-price-original  259 non-null    object
 4   data-rate-inc-total-price-offer          60 non-null     object
 5   data-rate-inc-night-price-offer          60 non-null     object
 6   data-rate-inc-total-price-original       199 non-null    object
 7   data-rate-inc-night-price-original       259 non-null    object
 8   data-rate-ex-total-price-offer           60 non-null     object
 9   data-rate-ex-night-price-offer           60 non-null     object
 10  data-rate-ex-total-price-original        199 non-null    object
 11  data-rate-ex-night-price-original        259 non-null    object
 12  display-night-price-offer                60 non-null     object
 13  display-night-price-original             259 non-null    object
 14  display-total-price-offer                60 non-null     object
 15  display-total-price-original             199 non-null    object
 16  is_offer                                 1011 non-null   bool
 17  is_available                             1011 non-null   bool
 18  time_stamp                               1011 non-null   datetime64[ns]
 19  room_info_raw                            259 non-null    object
 20  board_raw                                259 non-null    object
 21  hotel_name                               1011 non-null   object
 22  name                                     1011 non-null   object
 23  from                                     1011 non-null   object
 24  to                                       1011 non-null   object
 25  top_name                                 1011 non-null   object
 26  top_id                                   1011 non-null   object
"""
mms_deep = Table(
    "mms_deep",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("data_rate_currency_total_price_offer", String(256), nullable=True),
    Column("data_rate_currency_night_price_offer", String(256), nullable=True),
    Column("data_rate_currency_total_price_original",
           String(256), nullable=True),
    Column("data_rate_currency_night_price_original",
           String(256), nullable=True),
    Column("data_rate_inc_total_price_offer", String(256), nullable=True),
    Column("data_rate_inc_night_price_offer", String(256), nullable=True),
    Column("data_rate_inc_total_price_original", String(256), nullable=True),
    Column("data_rate_inc_night_price_original", String(256), nullable=True),
    Column("data_rate_ex_total_price_offer", String(256), nullable=True),
    Column("data_rate_ex_night_price_offer", String(256), nullable=True),
    Column("data_rate_ex_total_price_original", String(256), nullable=True),
    Column("data_rate_ex_night_price_original", String(256), nullable=True),
    Column("display_night_price_offer", String(256), nullable=True),
    Column("display_night_price_original", String(256), nullable=True),
    Column("display_total_price_offer", String(256), nullable=True),
    Column("display_total_price_original", String(256), nullable=True),
    Column("is_offer", Boolean, nullable=True),
    Column("is_available", Boolean, nullable=True),
    Column("time_stamp", DateTime, nullable=True),
    Column("room_info_raw", String(1024), nullable=True),
    Column("board_raw", String(1024), nullable=True),
    Column("hotel_name", String(1024), nullable=True),
    Column("name", String(256), nullable=True),
    Column("from", DateTime, nullable=True),
    Column("to", DateTime, nullable=True),
    Column("top_name", String(256), nullable=True),
    Column("top_id", String(256), nullable=True),
)


def start_mappers():

    try:
        _ = mapper(models.Api, api)
    except sqlalchemy.exc.ArgumentError:
        pass
