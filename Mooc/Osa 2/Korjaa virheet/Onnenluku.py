#Koitetaan korjata virheet. Ehkä..

luku = int(input("Anna luku: "))
if luku > 100:
    print("Luku oli suurempi kuin sata")
    luku = luku - 100
    print("Nyt luvun arvo on pienentynyt sadalla")
    print("Arvo on nyt"+ str(luku))
print(str(luku) + " taitaa olla onnenlukuni!")
print("Hyvää päivänjatkoa!")