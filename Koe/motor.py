from geopy.geocoders import Nominatim
from geopy import distance
import time

app = Nominatim(user_agent="GeoInfo 2.0")

def get_location_by_address(address):
    try:
        time.sleep(1)
        return app.geocode(address).raw
    except AttributeError:
        print("Osoitetetta ei ole olemassa!")
    quit()

def count_distance(fromAddress, toAddress):
    locationFrom = get_location_by_address(fromAddress)
    locationTo = get_location_by_address(toAddress)
    result = distance.distance((locationFrom["lat"], locationFrom["lon"]), (locationTo["lat"], locationTo["lon"]))
    return result.km

