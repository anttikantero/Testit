from geopy.geocoders import Nominatim
from geopy import distance
import time

app = Nominatim(user_agent="GeoInfo 2.0")

def get_location_by_address(address):
    time.sleep(1)
    return app.geocode(address).raw

def count_distance(fromAddress, toAddress):
    locationFrom = get_location_by_address(fromAddress)
    locationTo = get_location_by_address(toAddress)
    result = distance.distance((locationFrom["lat"], locationFrom["lon"]), (locationTo["lat"], locationTo["lon"]))
    return result.km

fromAddress = "Keilaranta 4, 02150 Espoo" 
toAddress = "9800 Savage Rd. United States"

distance = round(count_distance(fromAddress, toAddress),1)

print()
print('*' *70)
print('Lähtöpaikka: ' + fromAddress )
print('Määränpää: ' + toAddress)
print('\nVälimatka on: ' + str(distance) + ' km')
print('*' *70)