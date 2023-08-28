from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_region_country_nearest_city(coordinates):
    # Initialize geocoder
    geolocator = Nominatim(user_agent="geo_app")

    # Extract coordinates
    lat, lon = coordinates

    # Get location information
    location = geolocator.reverse((lat, lon), exactly_one=True, language="en")

    if location:
        address = location.raw.get("address", {})
        city = address.get("city", "")
        region = address.get("state", "")
        country = address.get("country", "")

        if not city:
            # If city is not available, use town or village
            city = address.get("town", address.get("village", ""))
        
        return {
            "region": region,
            "country": country,
            "nearest_city": city
        }
    else:
        return {
            "region": "N/A",
            "country": "N/A",
            "nearest_city": "N/A"
        }