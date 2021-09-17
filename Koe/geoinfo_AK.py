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

def count_distance(fromAddress, toAddress):
    locationFrom = get_location_by_address(fromAddress)
    locationTo = get_location_by_address(toAddress)
    result = distance.distance((locationFrom["lat"], locationFrom["lon"]), (locationTo["lat"], locationTo["lon"]))
    return result.km

fromAddress = input("Anna lähtöpaikan osoite: ")
toAddress = input("Anna määränpään osoite: ")

distance = round(count_distance(fromAddress, toAddress),1)

print()
print('*' *70)
print('Lähtöpaikka: ' + fromAddress )
print('Määränpää: ' + toAddress)
print('\nVälimatka on: ' + str(distance) + ' km')
if distance < 5:
    print("Mataka on alle 5km. Suosittelen kävelemään.")
else:
    print("Matka on yli 5km. Suositetlen ottamaan taksin.")
    print('*' *70)