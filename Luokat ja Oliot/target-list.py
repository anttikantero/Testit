
import requests
import socket


class Target:
    
    def __init__(self, siteName, address):
        self.name = siteName
        self.address = address
        self.server = ""
        self.IP = ""

    def setIP(self):
        parsed_address = self.address.replace("http://", "")
        parsed_address = parsed_address.replace("https://", "")
        parsed_address = parsed_address.replace("/", "")
        self.IP = socket.gethostbyname(parsed_address)


    def setServer(self):
        result = requests.get(self.address)
        
        self.server = result.headers["Server"]

   

    def printData(self):
        print("\nSivuston tiedot:")
        print("Site name: " + self.name)
        print("Server: " + self.server) 
        print("IP: " + self.IP)
        
        print("\n")



zerobank = Target("Zerobank", "http://zero.webappsecurity.com/")
zerobank.setServer()
zerobank.setIP()
zerobank.printData()

mtv = Target("MTV3", "http://www.mtv.fi")
mtv.setServer()
mtv.setIP()
mtv.printData()

hs = Target("HS", "http://www.hs.fi")
hs.setServer()
hs.setIP()
hs.printData()