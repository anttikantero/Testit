### Class = luokka. Luokan sisälle voidaan tehdä metodeja.
### Metodi alkaa def
### Olio on yleiskäyttöinen luokka. Oliota varten tarvitaan __init__ -fuktio
### ja self -käsite. 
### __init__ -funktio määrittelee olion luonnin aikana tapahtuvat määrittelyt.
### self -käsitteellä määritellään juuri tämän olion tiedot.


class Website:
    
    def __init__(self, siteName):
        self.hacked = False
        self.name = siteName
        self.ip = ""
        self.platform = ""

    def setAddress(self, address):
        self.ip = address

    def setPlatform(self, platform):
        self.platform = platform 

    def setHacked(self):
        self.hacked = True

    def printData(self):
        print("\nSivuston tiedot:")
        print("Site name: " + self.name)
        print("IP: " + self.ip)
        print("Platform: " + self.platform) 

        if self.hacked:
            print("Sivu on hakkeroitu")  
        
        print("\n")


# normaali koodin suoritus jatkuu

def info():
    print("Kirjaa tiedot hakkeroitavista kohteista")

info()


kissagalleria = Website("KissaGalleria")

kissagalleria.setAddress("20.93.141.10")
kissagalleria.setPlatform("WordPress")
kissagalleria.setHacked()



mehukauppa = Website("Mehukauppa")
mehukauppa.setAddress("192.0.0.1")
