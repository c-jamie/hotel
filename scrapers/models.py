from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Api:
    """reprents the key meta data for a API"""

    name: str
    url: str
    date: datetime = None
    meta: field(default_factory=dict) = None


@dataclass
class Virtuoso1:
    """virtuoso 1"""

    CityStateCountry: field(default_factory=dict)
    Company: str
    CurrencySymbol: str
    DefaultImageUrl: str
    Description: str
    DetailUrl: str
    Dimension: str
    Email: str
    EntityType: str
    Experiences: field(default_factory=dict)
    HasAdvisorIncentive: bool
    AdvisorIncentiveType: str
    HasHotelLookupDates: bool
    HasNetworkIncentive: bool
    HotelRateTypeString: str
    Id: str
    IsOptedIn: bool
    Name: str
    NearestAirportInfo: str
    Neighborhood: str
    NetworkIncentiveType: str
    Phone: str
    PropertyHasVirtuosoExclusivePromotion: bool
    PropertyIsEligibleOnlineBooking: bool
    PropertySabreId: int
    RateBARConverted: float
    RateGeneralConverted: float
    RateVMCConverted: float
    RateVirtuosoConverted: float
    RoomCount: int
    RoomStyle: str
    SupplierDetailUrl: str
    SupplierId: str
    Title: str
    Variant: str
    Vibe: str
    url: str = None
    date: datetime = None


@dataclass
class Virtuoso2:
    """virtuoso 1"""

    AmountConverted: float
    AmountLocalCurrency: float
    AmountUsd: float
    CancelPolicy: str
    CancellationInstructionsDisplay: str
    CommissionDetails: str
    CurrencySymbol: str
    DepositDisplay: str
    Description: str
    GuarantPolicy: str
    GuaranteeDisplay: str
    GuaranteeType: str
    IataCharacteristicIdentification: str
    IataCharacteristicIdentificationApiEquivalent: str
    IsCommissionable: bool
    IsRatePricingSameCurrency: bool
    IsRefundable: bool
    LocalHotelCurrencyCode: str
    LocalHotelCurrencySymbol: str
    NightlyRatesConverted: field(default_factory=dict)
    NightlyRatesLocalCurrency: field(default_factory=dict)
    NightlyRatesUsd: field(default_factory=dict)
    PricingDisclaimer: str
    PromotionName: str
    RateAccessCode: str
    RateAccessCodeApiEquivalent: str
    RateType: int
    RateTypeDisplay: str
    RateTypeDisplay: str
    RoomTypeCode: str
    SabreBookingKey: str
    SabreRph: str
    SabreRphApiEquivalent: str
    TaxesAndSurchargesIncluded: bool
    TotalAmountConverted: float
    TotalAmountLocalCurrency: float
    TotalAmountUsd: float
    TotalSurchargesConverted: float
    TotalSurchargesLocalCurrency: float
    TotalSurchargesUsd: float
    TotalTaxesAndFeesConverted: float
    TotalTaxesAndFeesLocalCurrency: float
    TotalTaxesAndFeesUsd: float
    TotalTaxesConverted: float
    TotalTaxesLocalCurrency: float
    TotalTaxesUsd: float
    url: str = None
    date: datetime = None


@dataclass
class Kiwi1:
    id: int
    geometry: field(default_factory=dict)
    object: field(default_factory=dict)
    type: field(default_factory=dict)


@dataclass
class Kiwi2:
    allRatesAreSpecialOffers: bool
    # == == ==
    childrenAges: field(default_factory=dict)
    currency: str
    errors: str
    hasKiwiRooms: bool
    hasPublicRooms: bool
    hasRoomImages: bool
    hasSpecialOffer: bool
    hasVisaRooms: bool
    hnwMinNights: bool
    inDate: datetime
    inDateFormatted: str
    locale: str
    numberAdults: int
    numberAdultsFormatted: str
    numberBeds: int
    numberChildren: int
    numberChildrenFormatted: str
    numberNights: int
    numberNightsFormatted: str
    numberRates: int
    numberRatesSpecialOffers: int
    numberRooms: int
    # == == ==
    otherPropertiesAvailable: field(default_factory=dict)
    otherPropertiesAvailableGeolocationId: str
    outDate: datetime
    outDateFormatted: str
    propertyAvailabilityCriteria: field(default_factory=dict)
    propertyAverageNightlyRateMinimum: str
    propertyId: str
    propertyRateMinimum: str

    selectedSpecialOfferAvailability: bool
    selectedSpecialOfferRooms: field(default_factory=dict)
    specialOfferRooms: field(default_factory=dict)
    success: bool
    userCurrency: str
    whiteLabel: str
    whiteLabelSrc: str

    id: int = None


@dataclass
class Kiwi3:
    kiwi_l2_id: int
    # == == ==
    allImages: field(default_factory=dict)
    averageNightlyRate: float
    averageTotalRate: float
    code: str
    description: str
    # == == ==
    extraImages: field(default_factory=dict)
    hasImages: bool
    hasKiwiBenefits: bool
    hasSpecialOffer: bool
    hasVisaBenefits: bool
    maxOccupancy: str
    minAverageNightlyRate: float
    minNightlyRate: float
    minSpecialOfferNightlyRate: float
    minSpecialOfferTotalRate: float
    minTotalRate: float
    primaryImage: field(default_factory=dict)
    ratesCount: int
    roomSize: field(default_factory=dict)
    title: str
    id: int = None


@dataclass
class Kiwi4:
    kiwi_l3_id: int
    allowedCreditCards: field(default_factory=dict) = None
    # == == ==
    amenities: field(default_factory=dict) = None
    averageNightlyRate: Optional[float] = None
    averageNightlyRateInclusive: Optional[float] = None
    averageNightlyRateTotal: Optional[float] = None
    averageNightlyRateWithSymbol: Optional[str] = None
    benefitCollections: Optional[str] = None
    cancelBy: Optional[datetime] = None
    cancelByFormatted: Optional[str] = None
    cancellable: Optional[str] = None
    cancellableStatus: Optional[str] = None
    cancellationPolicy: Optional[str] = None
    checkinText: Optional[str] = None
    childPolicy: Optional[str] = None
    code: Optional[str] = None
    # == == ==
    consolidatedFeesTaxes: field(default_factory=dict) = None
    corpCode: Optional[str] = None
    corpCodeEncoded: Optional[str] = None
    currencyId: Optional[str] = None
    depositPolicy: Optional[str] = None
    description: Optional[str] = None
    gdsDescription: Optional[str] = None
    gdsTitle: Optional[str] = None
    guaranteePolicy: Optional[str] = None
    hasKiwiBenefits: Optional[bool] = None
    hasSpecialOffer: Optional[bool] = None
    hasVisaBenefits: Optional[bool] = None
    hideCancellableStatus: Optional[bool] = None
    hideGdsDescription: Optional[bool] = None
    isDiscrepancyInTotalInclusive: Optional[bool] = None
    isInclusive: Optional[bool] = None
    minNightlyRate: field(default_factory=dict) = None
    minNightlyRateWithSymbol: Optional[str] = None
    miscellaneousText: Optional[str] = None
    morRate: Optional[bool] = None
    morRateCommission: Optional[int] = None
    # == == ==
    nightlyCostsInfo: field(default_factory=dict) = None
    nightlyRate: Optional[float] = None
    nightlyRateInclusive: Optional[float] = None
    nightlyRateWithSymbol: Optional[str] = None
    numNights: Optional[str] = None
    petPolicy: Optional[str] = None
    prepayPolicy: Optional[str] = None
    rateCodeToSend: Optional[str] = None
    rateCodeToSendEncoded: Optional[str] = None
    roomCodeToSend: Optional[str] = None
    roomCodeToSendEncoded: Optional[str] = None
    serviceChargesText: Optional[str] = None
    shouldDisplayTotalInclusive: Optional[bool] = None
    specialOffer: field(default_factory=dict) = None
    specialRequirementsText: Optional[str] = None
    taxInformation: Optional[str] = None
    title: Optional[str] = None
    totalFeesAndSurcharges: Optional[int] = None
    totalFeesAndSurchargesWithSymbol: Optional[str] = None
    totalFeesTaxes: Optional[int] = None
    totalFeesTaxesWithSymbol: Optional[str] = None
    totalRate: Optional[int] = None
    totalRateChargeable: Optional[int] = None
    totalRateChargeableWithSymbol: Optional[str] = None
    totalRateInclusive: Optional[int] = None
    totalRateInclusiveWithSymbol: Optional[str] = None
    totalRateUSD: Optional[int] = None
    totalRateWithSymbol: Optional[str] = None
    totalTaxes: Optional[int] = None
    totalTaxesWithSymbol: Optional[str] = None
    type: Optional[str] = None
    typeGroup: Optional[int] = None
    userAverageNightlyRate: Optional[int] = None
    userAverageNightlyRateWithSymbol: Optional[str] = None
    userMinNightlyRate: Optional[int] = None
    userMinNightlyRateWithSymbol: Optional[str] = None
    userNightlyRate: Optional[int] = None
    userNightlyRateWithSymbol: Optional[str] = None
    userTotalFeesAndSurcharges: Optional[int] = None
    userTotalFeesAndSurchargesWithSymbol: Optional[str] = None
    userTotalFeesTaxesWithSymbol: Optional[str] = None
    userTotalRate: Optional[int] = None
    userTotalRateChargeable: Optional[int] = None
    userTotalRateChargeableWithSymbol: Optional[str] = None
    userTotalRateInclusive: Optional[int] = None
    userTotalRateInclusiveWithSymbol: Optional[str] = None
    userTotalRateWithSymbol: Optional[str] = None
    userTotalTaxes: Optional[int] = None
    userTotalTaxesWithSymbol: Optional[str] = None
    id: int = None
