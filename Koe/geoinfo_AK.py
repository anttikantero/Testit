from motor import get_location_by_address, count_distance

fromAddress = input("Anna lähtöpaikan osoite: ")
toAddress = input("Anna määränpään osoite: ")

distance = round(count_distance(fromAddress, toAddress),1)

print()
print('*' *70)
print('Lähtöpaikka: ' + fromAddress )
print('Määränpää: ' + toAddress)
print('\nVälimatka on: ' + str(distance) + ' km')
if distance < 5:
    print("Matka on alle 5km. Suosittelen kävelemään.")
else:
    print("Matka on yli 5km. Suosittelen ottamaan taksin.")
    print('*' *70)