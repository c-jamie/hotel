import sqlalchemy
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        MetaData, Numeric, String, Table, Text)
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
    Column("style", String(512), nullable=True),
    Column("setting", String(512), nullable=True),
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

"""
virtuoso_l1

 'CityStateCountry': '{"City":"Chantilly","State":"Picardie","Country":"France","StateAbbr":null}',
 'Company': None,
 'CurrencySymbol': '$',
 'DefaultImageUrl': 'https://media.virtuoso.com/m/Images/Brochures/14943144_2_0_0409.jpg',
 'Description': None,
 'DetailUrl': '/hotels/14949727/auberge-du-jeu-de-paume-chantilly-relais-chateaux',
 'Dimension': None,
 'Email': 'reservations@aubergedujeudepaume.fr',
 'EntityType': 'Property',
 'Experiences': ['Wellness', 'Local Immersion', 'Landmarks'],
 'HasAdvisorIncentive': False,
 'HasHotelLookupDates': False,
 'HasNetworkIncentive': False,
 'HotelRateTypeString': 'General',
 'Id': '14949727',
 'IsOptedIn': False,
 'Name': 'Auberge du Jeu de Paume, Chantilly, Relais & Chateaux',
 'NearestAirportInfo': 'Charles De Gaulle (CDG) 12 mi/19 km',
 'Neighborhood': None,
 'NetworkIncentiveType': None,
 'Phone': '33 344655000',
 'PropertyHasVirtuosoExclusivePromotion': False,
 'PropertyIsEligibleOnlineBooking': True,
 'PropertySabreId': 167410,
 'RateBARConverted': None,
 'RateGeneralConverted': None,
 'RateVMCConverted': None,
 'RateVirtuosoConverted': None,
 'RoomCount': 92,
 'RoomStyle': 'Indigenous',
 'SupplierDetailUrl': '/suppliers/14943144/auberge-du-jeu-de-paume-chantilly-relais-chateaux',
 'SupplierId': '14943144',
 'Title': 'Auberge du Jeu de Paume, Chantilly, Relais & Chateaux',
 'Variant': '',
 'Vibe': 'Sophisticated'}],
"""

virt_l1 = Table(
    "virtuoso_l1",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("CityStateCountry", MutableJson, nullable=True),
    Column("Company", String(512), nullable=True),
    Column("CurrencySymbol", String(3), nullable=True),
    Column("DefaultImageUrl", String(512), nullable=True),
    Column("Description", String(512), nullable=True),
    Column("DetailUrl", String(512), nullable=True),
    Column("Dimension", String(512), nullable=True),
    Column("Email", String(512), nullable=True),
    Column("EntityType", String(512), nullable=True),
    Column("Experiences", MutableJson, nullable=True),
    Column("HasAdvisorIncentive", Boolean, nullable=True),
    Column("AdvisorIncentiveType", String(128), nullable=True),
    Column("HasHotelLookupDates", Boolean, nullable=True),
    Column("HasNetworkIncentive", Boolean, nullable=True),
    Column("HotelRateTypeString", String(128), nullable=True),
    Column("Id", String(128), nullable=True),
    Column("IsOptedIn", Boolean, nullable=True),
    Column("Name", String(512), nullable=True),
    Column("NearestAirportInfo", String(512), nullable=True),
    Column("Neighborhood", String(512), nullable=True),
    Column("NetworkIncentiveType", String(512), nullable=True),
    Column("Phone", String(512), nullable=True),
    Column("PropertyHasVirtuosoExclusivePromotion", Boolean, nullable=True),
    Column("PropertyIsEligibleOnlineBooking", Boolean, nullable=True),
    Column("PropertySabreId", Integer, nullable=True),
    Column("RateBARConverted", Numeric(18, 6), nullable=True),
    Column("RateGeneralConverted", Numeric(18, 6), nullable=True),
    Column("RateVMCConverted", Numeric(18, 6), nullable=True),
    Column("RateVirtuosoConverted", Numeric(18, 6), nullable=True),
    Column("RoomCount", Integer, nullable=True),
    Column("RoomStyle", String(512), nullable=True),
    Column("SupplierDetailUrl", String(512), nullable=True),
    Column("SupplierId", String(512), nullable=True),
    Column("Title", String(512), nullable=True),
    Column("Variant", String(512), nullable=True),
    Column("Vibe", String(512), nullable=True),
    Column("url", String(512), nullable=True),
    Column("date", DateTime, nullable=True),
)

"""
virtuoso_l2

{'AmountConverted': 684.46,
 'AmountLocalCurrency': 624.29,
 'AmountUsd': 684.46,
 'CancelPolicy': 'Refundable. Cancellation deadline: 1 Day(s) prior to '
                 'arrival.',
 'CancellationInstructionsDisplay': 'Free Cancellation-Modification Until '
                                    'Noon; 3 Days Prior To Arrival. A Penalty '
                                    'Of 1 Night Stay Including Tax Will Be '
                                    'Charged For Late '
                                    'Cancellation/Modification. The Entire '
                                    'Stay Will Be Charged For No-Show And '
                                    'Early Departure.  Specific Policies May '
                                    'Apply To Some Rates Or Periods - Please '
                                    'Check.',
 'CommissionDetails': 'COMMISSIONABLE - 10.00 PERCENT',
 'CurrencySymbol': '$',
 'DepositDisplay': 'Pay At The Property - No Prepayment Required - Credit Card '
                   'Number With Valid Expiry Date And Security Code Is '
                   'Required To Guarantee Your Reservation. Specific Policies '
                   'May Apply To Some Rates Or Periods - Please Check.',
 'Description': 'Deluxe Room - 1 Double Bed - 31Sqm-333Sqft Patio Or City View',
 'GuarantPolicy': 'Guarantee required. Credit card AX, DC, JC, MC, VI, VS, CA, '
                  'IK accepted as guarantee.',
 'GuaranteeDisplay': None,
 'GuaranteeType': None,
 'IataCharacteristicIdentification': 'C1DAPI',
 'IataCharacteristicIdentificationApiEquivalent': None,
 'IsCommissionable': True,
 'IsRatePricingSameCurrency': False,
 'IsRefundable': True,
 'LocalHotelCurrencyCode': 'EUR',
 'LocalHotelCurrencySymbol': '[UNIESC]e2[UNIESC]82[UNIESC]ac',
 'NightlyRatesConverted': {'Fri, Jul 28 2023': 668.8,
                           'Mon, Jul 24 2023': 668.8,
                           'Sat, Jul 22 2023': 833.26,
                           'Sun, Jul 23 2023': 613.98,
                           'Thu, Jul 27 2023': 668.8,
                           'Tue, Jul 25 2023': 668.8,
                           'Wed, Jul 26 2023': 668.8},
 'NightlyRatesLocalCurrency': {'Fri, Jul 28 2023': '[UNIESC]e2[UNIESC]82[UNIESC]ac610.00',
                               'Mon, Jul 24 2023': '[UNIESC]e2[UNIESC]82[UNIESC]ac610.00',
                               'Sat, Jul 22 2023': '[UNIESC]e2[UNIESC]82[UNIESC]ac760.00',
                               'Sun, Jul 23 2023': '[UNIESC]e2[UNIESC]82[UNIESC]ac560.00',
                               'Thu, Jul 27 2023': '[UNIESC]e2[UNIESC]82[UNIESC]ac610.00',
                               'Tue, Jul 25 2023': '[UNIESC]e2[UNIESC]82[UNIESC]ac610.00',
                               'Wed, Jul 26 2023': '[UNIESC]e2[UNIESC]82[UNIESC]ac610.00'},
 'NightlyRatesUsd': {'Fri, Jul 28 2023': '$668.80',
                     'Mon, Jul 24 2023': '$668.80',
                     'Sat, Jul 22 2023': '$833.26',
                     'Sun, Jul 23 2023': '$613.98',
                     'Thu, Jul 27 2023': '$668.80',
                     'Tue, Jul 25 2023': '$668.80',
                     'Wed, Jul 26 2023': '$668.80'},
 'PricingDisclaimer': 'Includes Taxes And Surcharges',
 'PromotionName': '',
 'RateAccessCode': 'API',
 'RateAccessCodeApiEquivalent': None,
 'RateType': 4,
 'RateTypeDisplay': 'Virtuoso',
 'RoomTypeCode': 'C1D',
 'SabreBookingKey': None,
 'SabreRph': 'RXaxqoB7g6+kxDSgo7ZsQPdxfeZcK0UNX3X/220mOCA2yKEhvXwRe87P5CMihhWB5yPLypZXdNZ0OgQYJh7Qpz2GGeVyUphzOmsFjcgne47IEmf1DoEs5taskqUuIQBj30MCqQ3UMJFAJ/4okC4U7aFHwZlCOzsp2M+NbH1mM1pI4h7LxtD99QWt9O1YwJKatVuuxpxuyNqU/+zHWGaR82bbTE9SUlmnT3SUg4T6DtFA5E9/V2IjGK8Sg520//VCvcdyiP0UEiH3dDwok47WNtP+nYkj44BoVhhmuaCaTiE9I3EqzMrKCVMRVSD0164+nEm0NFQ5N6m/+y35xsYfUKfb8o0q1DfWg6D+nlcyui3WwJMU0KYSk2SZgchBT8YkRRJwc3RDHcgsPp2lDzzuyUfGbs+ax5/ASYZeco1uge8qIyilBHewz2elgKxMkLzqDyWhCKB0MP0ifTp3QdS1KFARyLA2hELiAt7ZK+dDs7ulS0rQNxQ4uwvBhBH5lAsddf6+FFwX98c3WVKoeBXk6trGFg/IEAo7H0DbP9r9asb4+A7yYgzrpL0pJZjdcLv2/qwV4ihpnvQ4URegdAA1r0MO6zO7SSDwLGPLlYA53qFYGWIlrqSC2Wrj3vJGf6zuv6Be/6zKLuXoHfVF7a5ZLg==',
 'SabreRphApiEquivalent': None,
 'TaxesAndSurchargesIncluded': False,
 'TotalAmountConverted': 4791.24,
 'TotalAmountLocalCurrency': 4370.0,
 'TotalAmountUsd': 4791.24,
 'TotalSurchargesConverted': 0,
 'TotalSurchargesLocalCurrency': 0,
 'TotalSurchargesUsd': 0,
 'TotalTaxesAndFeesConverted': 0,
 'TotalTaxesAndFeesLocalCurrency': 0,
 'TotalTaxesAndFeesUsd': 0,
 'TotalTaxesConverted': 0,
 'TotalTaxesLocalCurrency': 0,
 'TotalTaxesUsd': 0}
"""


virt_l2 = Table(
    "virtuoso_l2",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("AmountConverted", Numeric(512), nullable=True),
    Column("AmountLocalCurrency", Numeric(512), nullable=True),
    Column("AmountUsd", Numeric(512), nullable=True),
    Column("CancelPolicy", Text, nullable=True),
    Column("CancellationInstructionsDisplay", Text, nullable=True),
    Column("CommissionDetails", Text, nullable=True),
    Column("CurrencySymbol", String(21), nullable=True),
    Column("DepositDisplay", Text, nullable=True),
    Column("Description", Text, nullable=True),
    Column("GuarantPolicy", Text, nullable=True),
    Column("GuaranteeDisplay", Text, nullable=True),
    Column("GuaranteeType", Text, nullable=True),
    Column("IataCharacteristicIdentification", Text, nullable=True),
    Column("IataCharacteristicIdentificationApiEquivalent", Text, nullable=True),
    Column("IsCommissionable", Boolean, nullable=True),
    Column("IsRatePricingSameCurrency", Boolean, nullable=True),
    Column("IsRefundable", Boolean, nullable=True),
    Column("LocalHotelCurrencyCode", String(64), nullable=True),
    Column("LocalHotelCurrencySymbol", String(64), nullable=True),
    Column("NightlyRatesConverted", MutableJson, nullable=True),
    Column("NightlyRatesLocalCurrency ", MutableJson, nullable=True),
    Column("NightlyRatesUsd", MutableJson, nullable=True),
    Column("PricingDisclaimer", Text, nullable=True),
    Column("PromotionName", Text, nullable=True),
    Column("RateAccessCode", Text, nullable=True),
    Column("RateAccessCodeApiEquivalent", Text, nullable=True),
    Column("RateType", Integer, nullable=True),
    Column("RateTypeDisplay", String(64), nullable=True),
    Column("RateTypeDisplay", String(64), nullable=True),
    Column("RoomTypeCode", String(64), nullable=True),
    Column("SabreBookingKey", Text, nullable=True),
    Column("SabreRph", String(2064), nullable=True),
    Column("SabreRphApiEquivalent", String(2064), nullable=True),
    Column("TaxesAndSurchargesIncluded", Boolean, nullable=True),
    Column("TotalAmountConverted", Numeric(18, 6), nullable=True),
    Column("TotalAmountLocalCurrency", Numeric(18, 6), nullable=True),
    Column("TotalAmountUsd", Numeric(18, 6), nullable=True),
    Column("TotalSurchargesConverted", Numeric(18, 6), nullable=True),
    Column("TotalSurchargesLocalCurrency", Numeric(18, 6), nullable=True),
    Column("TotalSurchargesUsd", Numeric(18, 6), nullable=True),
    Column("TotalTaxesAndFeesConverted", Numeric(18, 6), nullable=True),
    Column("TotalTaxesAndFeesLocalCurrency", Numeric(18, 6), nullable=True),
    Column("TotalTaxesAndFeesUsd", Numeric(18, 6), nullable=True),
    Column("TotalTaxesConverted", Numeric(18, 6), nullable=True),
    Column("TotalTaxesLocalCurrency", Numeric(18, 6), nullable=True),
    Column("TotalTaxesUsd", Numeric(18, 6), nullable=True),
    Column("url", Text, nullable=True),
    Column("date", DateTime, nullable=True),
    Column("start_date", DateTime, nullable=True),
    Column("end_date", DateTime, nullable=True),
    Column("supplier_id", Text, nullable=True),
)

"""
{'alerts': ['Please note, guests aged 17 and up will be considered as adults '
            "under the hotel's child policy."],
 'allRatesAreSpecialOffers': False,
 'analytics': {'googleAnalyticsDataActionDetails': {'detail': {'list': 'Hotel '
                                                                       'Availability '
                                                                       'Request'}},
               'googleAnalyticsDataImpressionDetails': [{'brand': 'Rosewood '
                                                                  'Hotels & '
                                                                  'Resorts',
                                                         'category': 'Europe/United '
                                                                     'Kingdom/England/London',
                                                         'coupon': '',
                                                         'currencyId': 'GBP',
                                                         'id': 'PR011003',
                                                         'list': '',
                                                         'name': 'Rosewood '
                                                                 'London',
                                                         'position': 1,
                                                         'price': 1000,
                                                         'quantity': '',
                                                         'variant': ''}],
               'googleAnalyticsDataPageHost': 'www.kiwicollection.com',
               'googleAnalyticsDataPagePath': '/rooms/availability/embed/PR011003/2023-06-09/2023-06-16/2/0/1',
               'googleAnalyticsDataPageTitle': 'Rosewood London, London, '
                                               'England',
               'googleAnalyticsDataProductDetails': [{'brand': 'Rosewood '
                                                               'Hotels & '
                                                               'Resorts',
                                                      'category': 'Europe/United '
                                                                  'Kingdom/England/London',
                                                      'coupon': '',
                                                      'currencyId': 'GBP',
                                                      'id': 'PR011003',
                                                      'list': '',
                                                      'name': 'Rosewood London',
                                                      'position': 1,
                                                      'price': 1000,
                                                      'quantity': '',
                                                      'variant': ''}],
               'googleAnalyticsDataPromotionDetails': []},
 'childrenAges': [],
 'currency': 'GBP',
 'errors': None,
 'hasKiwiRooms': False,
 'hasPublicRooms': True,
 'hasRoomImages': True,
 'hasSpecialOffer': False,
 'hasVisaRooms': True,
 'hnwMinNights': False,
 'inDate': '2023-06-09T00:00:00-07:00',
 'inDateFormatted': 'Fri, Jun 9, 2023',
 'locale': 'en_US',
 'numberAdults': 2,
 'numberAdultsFormatted': '2 Adults',
 'numberBeds': 1,
 'numberChildren': 0,
 'numberChildrenFormatted': None,
 'numberNights': '7',
 'numberNightsFormatted': '7 Nights',
 'numberRates': 51,
 'numberRatesSpecialOffers': 0,
 'numberRooms': 1,
 'otherPropertiesAvailable': [],
 'otherPropertiesAvailableGeolocationId': None,
 'outDate': '2023-06-16T00:00:00-07:00',
 'outDateFormatted': 'Fri, Jun 16, 2023',
 'propertyAvailabilityCriteria': {'inDate': '2023-06-09T00:00:00-07:00',
                                  'numAdults': 2,
                                  'numBeds': 1,
                                  'numChildren': 0,
                                  'numRooms': 1,
                                  'outDate': '2023-06-16T00:00:00-07:00',
                                  'propertyIds': ['PR011003'],
                                  'specialOfferId': None},
 'propertyAverageNightlyRateMinimum': '$1,000',
 'propertyId': 'PR011003',
 'propertyRateMinimum': '$844',
 'rooms': [{'allImages': [{'altText': 'Executive Twin Room, Rosewood London',
                           'fileName': '011003-executive-twin-rosewood-london.jpg',
                           'paths': {'l': 'https://cdn.kiwicollection.com/media/room_images/PR011003/l/011003-executive-twin-rosewood-london.jpg',
                                     'll': 'https://cdn.kiwicollection.com/media/room_images/PR011003/ll/011003-executive-twin-rosewood-london.jpg',
                                     'm': 'https://cdn.kiwicollection.com/media/room_images/PR011003/m/011003-executive-twin-rosewood-london.jpg',
                                     's': 'https://cdn.kiwicollection.com/media/room_images/PR011003/s/011003-executive-twin-rosewood-london.jpg',
                                     'xl': 'https://cdn.kiwicollection.com/media/room_images/PR011003/xl/011003-executive-twin-rosewood-london.jpg',
                                     'xs': 'https://cdn.kiwicollection.com/media/room_images/PR011003/xs/011003-executive-twin-rosewood-london.jpg',
                                     'xxl': 'https://cdn.kiwicollection.com/media/room_images/PR011003/xxl/011003-executive-twin-rosewood-london.jpg'},
                           'title': ''}],
            'averageNightlyRate': 938.4,
            'averageTotalRate': 6568.8,
            'code': 'A2T',
            'description': 'The refined Executive Rooms two oversized twin '
                           'beds and air conditioning.',
            'extraImages': [],
            'hasImages': True,
            'hasKiwiBenefits': False,
            'hasSpecialOffer': False,
            'hasVisaBenefits': True,
            'maxOccupancy': None,
            'minAverageNightlyRate': 800.14,
            'minNightlyRate': 675,
            'minSpecialOfferNightlyRate': None,
            'minSpecialOfferTotalRate': None,
            'minTotalRate': 5601,
            'primaryImage': {'altText': 'Executive Twin Room, Rosewood London',
                             'fileName': '011003-executive-twin-rosewood-london.jpg',
                             'paths': {'l': 'https://cdn.kiwicollection.com/media/room_images/PR011003/l/011003-executive-twin-rosewood-london.jpg',
                                       'll': 'https://cdn.kiwicollection.com/media/room_images/PR011003/ll/011003-executive-twin-rosewood-london.jpg',
                                       'm': 'https://cdn.kiwicollection.com/media/room_images/PR011003/m/011003-executive-twin-rosewood-london.jpg',
                                       's': 'https://cdn.kiwicollection.com/media/room_images/PR011003/s/011003-executive-twin-rosewood-london.jpg',
                                       'xl': 'https://cdn.kiwicollection.com/media/room_images/PR011003/xl/011003-executive-twin-rosewood-london.jpg',
                                       'xs': 'https://cdn.kiwicollection.com/media/room_images/PR011003/xs/011003-executive-twin-rosewood-london.jpg',
                                       'xxl': 'https://cdn.kiwicollection.com/media/room_images/PR011003/xxl/011003-executive-twin-rosewood-london.jpg'},
                             'title': ''},
            'rates': [{'allowedCreditCards': {'VI': {'id': 'VI',
                                                     'name': 'Visa'}},
                       'amenities': [],
                       'averageNightlyRate': 940.71,
                       'averageNightlyRateInclusive': 940.71,
                       'averageNightlyRateTotal': 940.71,
                       'averageNightlyRateWithSymbol': '£941',
                       'benefitCollections': {'1': {'benefitCollectionTypeId': 1,
                                                    'benefits': {'1': 'Complimentary '
                                                                      'breakfast '
                                                                      'for two',
                                                                 '2': '$25 USD '
                                                                      'food or '
                                                                      'beverage '
                                                                      'credit',
                                                                 '3': 'Automatic '
                                                                      'room '
                                                                      'upgrade '
                                                                      'upon '
                                                                      'arrival, '
                                                                      'when '
                                                                      'available',
                                                                 '4': 'Complimentary '
                                                                      'in-room '
                                                                      'Wi-Fi, '
                                                                      'when '
                                                                      'available',
                                                                 '5': 'Late '
                                                                      'check-out '
                                                                      'upon '
                                                                      'request, '
                                                                      'when '
                                                                      'available',
                                                                 '6': 'VIP '
                                                                      'Guest '
                                                                      'status',
                                                                 '7': 'Best '
                                                                      'available '
                                                                      'rate '
                                                                      'guarantee '
                                                                      '(temporarily '
                                                                      'unavailable)'},
                                                    'collectionId': 1,
                                                    'exception': None,
                                                    'id': 3468,
                                                    'name': 'Premium Benefits',
                                                    'propertyId': None,
                                                    'rateCodeId': None,
                                                    'restriction': '<strong>Restrictions: '
                                                                   '</strong><ul>\n'
                                                                   '<li>This '
                                                                   'rate plan '
                                                                   'is for '
                                                                   'select '
                                                                   'Visa '
                                                                   'Premium '
                                                                   'Card '
                                                                   'holders</li>\n'
                                                                   '<li>Cardholder '
                                                                   'must '
                                                                   'reserve '
                                                                   'and pay '
                                                                   'for the '
                                                                   'room using '
                                                                   'a '
                                                                   'qualifying '
                                                                   'credit '
                                                                   'card. '
                                                                   'Qualifying '
                                                                   'Visa '
                                                                   'Premium '
                                                                   'Cards '
                                                                   'include '
                                                                   'Visa '
                                                                   'Signature '
                                                                   'and Visa '
                                                                   'Infinite '
                                                                   'cards and '
                                                                   'select '
                                                                   'Visa Gold '
                                                                   'and Visa '
                                                                   'Platinum '
                                                                   'cards</li>\n'
                                                                   '</ul>'}},
                       'cancelBy': '2023-06-08T00:00:00-07:00',
                       'cancelByFormatted': 'Jun 8, 2023',
                       'cancellable': 'CANCELLABLE',
                       'cancellableStatus': None,
                       'cancellationPolicy': 'Cancellation by 1800 hotel time '
                                             'on 08jun23-fee 1 night '
                                             'reservations must be cancelled '
                                             'by 6pm local hotel time 1 day '
                                             'pri',
                       'checkinText': '',
                       'childPolicy': '',
                       'code': 'KCV',
                       'consolidatedFeesTaxes': [],
                       'corpCode': '361785',
                       'corpCodeEncoded': 'MzYxNzg1',
                       'currencyId': 'GBP',
                       'depositPolicy': '',
                       'description': '<p>                <p '
                                      'class="roomrate-heading">            '
                                      '<strong '
                                      'class="roomrate-heading">Premium '
                                      'Benefits</strong>        </p>        '
                                      '<ul '
                                      'class="amenities-container">                '
                                      '<li class="amenity-check">            '
                                      '<i tabindex="-1" aria-hidden="true" '
                                      'class="icon"></i>            '
                                      'Complimentary breakfast for '
                                      'two</li>                <li '
                                      'class="amenity-check">            <i '
                                      'tabindex="-1" aria-hidden="true" '
                                      'class="icon"></i>            $25 USD '
                                      'food or beverage '
                                      'credit</li>                <li '
                                      'class="amenity-check">            <i '
                                      'tabindex="-1" aria-hidden="true" '
                                      'class="icon"></i>            Automatic '
                                      'room upgrade upon arrival, when '
                                      'available</li>                <li '
                                      'class="amenity-check">            <i '
                                      'tabindex="-1" aria-hidden="true" '
                                      'class="icon"></i>            '
                                      'Complimentary in-room Wi-Fi, when '
                                      'available</li>                <li '
                                      'class="amenity-check">            <i '
                                      'tabindex="-1" aria-hidden="true" '
                                      'class="icon"></i>            Late '
                                      'check-out upon request, when '
                                      'available</li>                <li '
                                      'class="amenity-check">            <i '
                                      'tabindex="-1" aria-hidden="true" '
                                      'class="icon"></i>            VIP Guest '
                                      'status</li>                <li '
                                      'class="amenity-check">            <i '
                                      'tabindex="-1" aria-hidden="true" '
                                      'class="icon"></i>            Best '
                                      'available rate guarantee (temporarily '
                                      'unavailable)</li>            '
                                      '</ul>            <span '
                                      'class="roomrate-restrictions '
                                      'benefit-collection-restriction"><strong>Restrictions: '
                                      '</strong><ul><li>This rate plan is for '
                                      'select Visa Premium Card '
                                      'holders</li><li>Cardholder must reserve '
                                      'and pay for the room using a qualifying '
                                      'credit card. Qualifying Visa Premium '
                                      'Cards include Visa Signature and Visa '
                                      'Infinite cards and select Visa Gold and '
                                      'Visa Platinum '
                                      'cards</li></ul></span></p>',
                       'gdsDescription': '<p>VISA PREMIUM CARD RATE VISA CBF '
                                         'RMUPG 3PM C/O 25USD FBCR INT</p>',
                       'gdsTitle': 'Visa Premium Card Rate',
                       'guaranteePolicy': 'Guar types - ta ax dc jc mc ca vi '
                                          'ma up',
                       'hasKiwiBenefits': False,
                       'hasSpecialOffer': False,
                       'hasVisaBenefits': True,
                       'hideCancellableStatus': False,
                       'hideGdsDescription': False,
                       'isDiscrepancyInTotalInclusive': False,
                       'isInclusive': False,
                       'minNightlyRate': 793,
                       'minNightlyRateWithSymbol': '£793',
                       'miscellaneousText': '',
                       'morRate': False,
                       'morRateCommission': 0,
                       'nightlyCostsInfo': [{'charge': '807.00',
                                             'chargeFormatted': '£807',
                                             'chargeTotal': 807,
                                             'date': '2023-06-09T00:00:00-07:00',
                                             'tax': None,
                                             'taxTotal': 0,
                                             'userChargeFormatted': '$1,009',
                                             'userDate': 'June 9, 2023'},
                                            {'charge': '793.00',
                                             'chargeFormatted': '£793',
                                             'chargeTotal': 793,
                                             'date': '2023-06-10T00:00:00-07:00',
                                             'tax': None,
                                             'taxTotal': 0,
                                             'userChargeFormatted': '$991',
                                             'userDate': 'June 10, 2023'},
                                            {'charge': '997.00',
                                             'chargeFormatted': '£997',
                                             'chargeTotal': 997,
                                             'date': '2023-06-11T00:00:00-07:00',
                                             'tax': None,
                                             'taxTotal': 0,
                                             'userChargeFormatted': '$1,246',
                                             'userDate': 'June 11, 2023'},
                                            {'charge': '997.00',
                                             'chargeFormatted': '£997',
                                             'chargeTotal': 997,
                                             'date': '2023-06-12T00:00:00-07:00',
                                             'tax': None,
                                             'taxTotal': 0,
                                             'userChargeFormatted': '$1,246',
                                             'userDate': 'June 12, 2023'},
                                            {'charge': '997.00',
                                             'chargeFormatted': '£997',
                                             'chargeTotal': 997,
                                             'date': '2023-06-13T00:00:00-07:00',
                                             'tax': None,
                                             'taxTotal': 0,
                                             'userChargeFormatted': '$1,246',
                                             'userDate': 'June 13, 2023'},
                                            {'charge': '997.00',
                                             'chargeFormatted': '£997',
                                             'chargeTotal': 997,
                                             'date': '2023-06-14T00:00:00-07:00',
                                             'tax': None,
                                             'taxTotal': 0,
                                             'userChargeFormatted': '$1,246',
                                             'userDate': 'June 14, 2023'},
                                            {'charge': '997.00',
                                             'chargeFormatted': '£997',
                                             'chargeTotal': 997,
                                             'date': '2023-06-15T00:00:00-07:00',
                                             'tax': None,
                                             'taxTotal': 0,
                                             'userChargeFormatted': '$1,246',
                                             'userDate': 'June 15, 2023'}],
                       'nightlyRate': 940.71,
                       'nightlyRateInclusive': 940.71,
                       'nightlyRateWithSymbol': '£941',
                       'numNights': '7',
                       'petPolicy': '',
                       'prepayPolicy': '',
                       'rateCodeToSend': 'KCV',
                       'rateCodeToSendEncoded': 'S0NW',
                       'roomCodeToSend': 'A2T',
                       'roomCodeToSendEncoded': 'QTJU',
                       'serviceChargesText': '',
                       'shouldDisplayTotalInclusive': True,
                       'specialOffer': None,
                       'specialRequirementsText': '',
                       'taxInformation': '',
                       'title': 'Visa Premium Card Rate',
                       'totalFeesAndSurcharges': 0,
                       'totalFeesAndSurchargesWithSymbol': '£0',
                       'totalFeesTaxes': 0,
                       'totalFeesTaxesWithSymbol': '£0',
                       'totalRate': 6585,
                       'totalRateChargeable': 6585,
                       'totalRateChargeableWithSymbol': '£6,585',
                       'totalRateInclusive': 6585,
                       'totalRateInclusiveWithSymbol': '£6,585',
                       'totalRateUSD': 8229,
                       'totalRateWithSymbol': '£6,585',
                       'totalTaxes': 0,
                       'totalTaxesWithSymbol': '£0',
                       'type': 'visa',
                       'typeGroup': 3,
                       'userAverageNightlyRate': 1176,
                       'userAverageNightlyRateWithSymbol': '$1,176',
                       'userMinNightlyRate': 991,
                       'userMinNightlyRateWithSymbol': '$991',
                       'userNightlyRate': 1176,
                       'userNightlyRateWithSymbol': '$1,176',
                       'userTotalFeesAndSurcharges': 0,
                       'userTotalFeesAndSurchargesWithSymbol': '$0',
                       'userTotalFeesTaxesWithSymbol': '$0',
                       'userTotalRate': 8229,
                       'userTotalRateChargeable': 8229,
                       'userTotalRateChargeableWithSymbol': '$8,229',
                       'userTotalRateInclusive': 8229,
                       'userTotalRateInclusiveWithSymbol': '$8,229',
                       'userTotalRateWithSymbol': '$8,229',
                       'userTotalTaxes': 0,
                       'userTotalTaxesWithSymbol': '$0'},
                       'userTotalTaxesWithSymbol': '$0'}],
            'ratesCount': 5,
            'roomSize': {'fromFeet': 334,
                         'fromMeter': 31,
                         'toFeet': 0,
                         'toMeter': None},
            'title': 'Executive Twin Room'}],

        {'geometry': {'coordinates': [12.486553969311526,
                                            41.90752413027887],
                            'type': 'Point'},
               'object': {'hasHnwPerks': False,
                          'propertyId': 'PR100265',
                          'showMinRateFlyout': True,
                          'title': 'Sofitel Roma Villa Borghese'},
               'type': 'Feature'}],

"""

kiwi_l1 = Table(
    "kiwi_l1",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("geometry", MutableJson, nullable=True),
    Column("object", MutableJson, nullable=True),
    Column("type", MutableJson, nullable=True),
    Column("region_info", MutableJson, nullable=True),
    Column("description", MutableJson, nullable=True),
)

kiwi_l2 = Table(
    "kiwi_l2",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("allRatesAreSpecialOffers", Boolean, nullable=True),
    # == == ==
    Column("childrenAges", MutableJson, nullable=True),
    Column("currency", String(24), nullable=True),
    Column("errors", String(512), nullable=True),
    Column("hasKiwiRooms", Boolean, nullable=True),
    Column("hasPublicRooms", Boolean, nullable=True),
    Column("hasRoomImages", Boolean, nullable=True),
    Column("hasSpecialOffer", Boolean, nullable=True),
    Column("hasVisaRooms", Boolean, nullable=True),
    Column("hnwMinNights", Boolean, nullable=True),
    Column("inDate", DateTime, nullable=True),
    Column("inDateFormatted", String(2064), nullable=True),
    Column("locale", String(64), nullable=True),
    Column("numberAdults", Integer, nullable=True),
    Column("numberAdultsFormatted", String(64), nullable=True),
    Column("numberBeds", Integer, nullable=True),
    Column("numberChildren", Integer, nullable=True),
    Column("numberChildrenFormatted", String(64), nullable=True),
    Column("numberNights", Integer, nullable=True),
    Column("numberNightsFormatted", String(64), nullable=True),
    Column("numberRates", Integer, nullable=True),
    Column("numberRatesSpecialOffers", Integer, nullable=True),
    Column("numberRooms", Integer, nullable=False),
    # == == ==
    Column("otherPropertiesAvailable", MutableJson, nullable=True),
    Column("otherPropertiesAvailableGeolocationId",
           String(2064), nullable=True),
    Column("outDate", DateTime, nullable=True),
    Column("outDateFormatted", String(64), nullable=True),
    Column("propertyAvailabilityCriteria", MutableJson, nullable=True),
    Column("propertyAverageNightlyRateMinimum", String(2064), nullable=True),
    Column("propertyId", String(2064), nullable=True),
    Column("propertyRateMinimum", String(2064), nullable=True),
    Column("selectedSpecialOfferAvailability", Boolean, nullable=True),
    Column("selectedSpecialOfferRooms", MutableJson, nullable=True),
    Column("specialOfferRooms", MutableJson, nullable=True),
    Column("success", Boolean, nullable=True),
    Column("userCurrency", String(64), nullable=True),
    Column("whiteLabel", String(64), nullable=True),
    Column("whiteLabelSrc", String(64), nullable=True),
)

kiwi_l3 = Table(
    "kiwi_l3",
    metadata,
    Column("kiwi_l2_id", ForeignKey("kiwi_l2.id")),
    Column("id", Integer, primary_key=True, autoincrement=True),
    # == == ==
    Column("allImages", MutableJson, nullable=True),
    Column("averageNightlyRate", Numeric(18, 6), nullable=True),
    Column("averageTotalRate", Numeric(18, 6), nullable=True),
    Column("code", String(64), nullable=True),
    Column("description", String(2064), nullable=True),
    # == == ==
    Column("extraImages", MutableJson, nullable=True),
    Column("hasImages", Boolean, nullable=True),
    Column("hasKiwiBenefits", Boolean, nullable=True),
    Column("hasSpecialOffer", Boolean, nullable=True),
    Column("hasVisaBenefits", Boolean, nullable=True),
    Column("maxOccupancy", String(64), nullable=True),
    Column("minAverageNightlyRate", Numeric(18, 6), nullable=True),
    Column("minNightlyRate", Numeric(18, 6), nullable=True),
    Column("minSpecialOfferNightlyRate", Numeric(18, 6), nullable=True),
    Column("minSpecialOfferTotalRate", Numeric(18, 6), nullable=True),
    Column("minTotalRate", Numeric(18, 6), nullable=True),
    Column("primaryImage", MutableJson, nullable=True),
    Column("ratesCount", Integer, nullable=True),
    Column("roomSize", MutableJson, nullable=True),
    Column("title", String(512), nullable=True),
)

kiwi_l4 = Table(
    "kiwi_l4",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("kiwi_l3_id", ForeignKey("kiwi_l3.id")),
    Column("allowedCreditCards", MutableJson, nullable=True),
    # == == ==
    Column("amenities", MutableJson, nullable=True),
    Column("averageNightlyRate", Numeric(18, 6), nullable=True),
    Column("averageNightlyRateInclusive", Numeric(18, 6), nullable=True),
    Column("averageNightlyRateTotal", Numeric(18, 6), nullable=True),
    Column("averageNightlyRateWithSymbol", String(64), nullable=True),
    Column("benefitCollections", MutableJson, nullable=True),
    Column("cancelBy", DateTime, nullable=True),
    Column("cancelByFormatted", Text, nullable=True),
    Column("cancellable", Text, nullable=True),
    Column("cancellableStatus", String(512), nullable=True),
    Column("cancellationPolicy", String(512), nullable=True),
    Column("checkinText", Text, nullable=True),
    Column("childPolicy", Text, nullable=True),
    Column("code", Text, nullable=True),
    # == == ==
    Column("consolidatedFeesTaxes", MutableJson, nullable=True),
    Column("corpCode", Text, nullable=True),
    Column("corpCodeEncoded", Text, nullable=True),
    Column("currencyId", Text, nullable=True),
    Column("depositPolicy", Text, nullable=True),
    Column("description", Text, nullable=True),
    Column("gdsDescription", Text, nullable=True),
    Column("gdsTitle", Text, nullable=True),
    Column("guaranteePolicy", Text, nullable=True),
    Column("hasKiwiBenefits", Boolean, nullable=True),
    Column("hasSpecialOffer", Boolean, nullable=True),
    Column("hasVisaBenefits", Boolean, nullable=True),
    Column("hideCancellableStatus", Boolean, nullable=True),
    Column("hideGdsDescription", Boolean, nullable=True),
    Column("isDiscrepancyInTotalInclusive", Boolean, nullable=True),
    Column("isInclusive", Boolean, nullable=True),
    Column("minNightlyRate", Integer, nullable=True),
    Column("minNightlyRateWithSymbol", Text, nullable=True),
    Column("miscellaneousText", Text, nullable=True),
    Column("morRate", Boolean, nullable=True),
    Column("morRateCommission", Integer, nullable=True),
    # == == ==
    Column("nightlyCostsInfo", MutableJson, nullable=True),
    Column("nightlyRate", Numeric(18, 6), nullable=True),
    Column("nightlyRateInclusive", Numeric(18, 6), nullable=True),
    Column("nightlyRateWithSymbol", Text, nullable=True),
    Column("numNights", Text, nullable=True),
    Column("petPolicy", Text, nullable=True),
    Column("prepayPolicy", Text, nullable=True),
    Column("rateCodeToSend", Text, nullable=True),
    Column("rateCodeToSendEncoded", Text, nullable=True),
    Column("ooomCodeToSend", Text, nullable=True),
    Column("roomCodeToSendEncoded", Text, nullable=True),
    Column("serviceChargesText", Text, nullable=True),
    Column("shouldDisplayTotalInclusive", Boolean, nullable=True),
    Column("specialOffer", MutableJson, nullable=True),
    Column("specialRequirementsText", Text, nullable=True),
    Column("taxInformation", Text, nullable=True),
    Column("title", Text, nullable=True),
    Column("totalFeesAndSurcharges", Integer, nullable=True),
    Column("totalFeesAndSurchargesWithSymbol", Text, nullable=True),
    Column("totalFeesTaxes", Integer, nullable=True),
    Column("totalFeesTaxesWithSymbol", Text, nullable=True),
    Column("totalRate", Integer, nullable=True),
    Column("totalRateChargeable", Integer, nullable=True),
    Column("totalRateChargeableWithSymbol", String(64), nullable=True),
    Column("totalRateInclusive", Integer, nullable=True),
    Column("totalRateInclusiveWithSymbol", String(65), nullable=True),
    Column("totalRateUSD", Integer, nullable=True),
    Column("totalRateWithSymbol", String(64), nullable=True),
    Column("totalTaxes", Integer, nullable=True),
    Column("totalTaxesWithSymbol", String(64), nullable=True),
    Column("type", String(64), nullable=True),
    Column("typeGroup", Integer, nullable=True),
    Column("userAverageNightlyRate", Integer, nullable=True),
    Column("userAverageNightlyRateWithSymbol", String(64), nullable=True),
    Column("userMinNightlyRate", Integer, nullable=True),
    Column("userMinNightlyRateWithSymbol", String(64), nullable=True),
    Column("userNightlyRate", Integer, nullable=True),
    Column("userNightlyRateWithSymbol", String(64), nullable=True),
    Column("userTotalFeesAndSurcharges", Integer, nullable=True),
    Column("userTotalFeesAndSurchargesWithSymbol", String(64), nullable=True),
    Column("userTotalFeesTaxesWithSymbol", String(64), nullable=True),
    Column("userTotalRate", Integer, nullable=True),
    Column("userTotalRateChargeable", Integer, nullable=True),
    Column("userTotalRateChargeableWithSymbol", String(64), nullable=True),
    Column("userTotalRateInclusive", Integer, nullable=True),
    Column("userTotalRateInclusiveWithSymbol", String(64), nullable=True),
    Column("userTotalRateWithSymbol", String(64), nullable=True),
    Column("userTotalTaxes", Integer, nullable=True),
    Column("userTotalTaxesWithSymbol", String(64), nullable=True),
    Column("date", DateTime, nullable=True),
)


def start_mappers():
    _ = mapper(models.Api, api)
    _ = mapper(models.Virtuoso1, virt_l1)
    _ = mapper(models.Virtuoso2, virt_l2)
    _ = mapper(models.Kiwi1, kiwi_l1)
    _ = mapper(models.Kiwi2, kiwi_l2)
    _ = mapper(models.Kiwi3, kiwi_l3)
    _ = mapper(models.Kiwi4, kiwi_l4)
