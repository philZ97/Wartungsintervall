
import json
import datetime

from Blech import Blech

class Stanzmaschine(Blech):

    raw = None
    hersteller = None
    standort = None
    halle = None
    platznummer = None
    wartung = None
    blech = None
    stanzMuster = None
    stanzMusterNummer = None
    
    
    def __init__(self, jsonData):
        with open(jsonData, "r") as datei:
            daten = json.load(datei)
        self.raw = json.dumps(daten, indent=4)
        self.standort = daten["Standort"]
        self.hersteller = daten["Hersteller"]
        self.wartung = daten["Wartung"]
        self.halle = self.standort["Halle"]
        self.platznummer = self.standort["Platz"]
        
    
    def leseConfigdatei(self, jsonData2):
        with open(jsonData2, "r") as datei:
            daten = json.load(datei)
        self.stanzMuster = json.dumps(daten, indent=4)
        return self.stanzMuster
        
    def setStandort(self, standort):
        self.standort = standort  
        
    def getStandort(self):
        return self.standort
    
    
    def setHersteller(self, hersteller):
        self.hersteller = hersteller
        
    def getHersteller(self):
        return self.hersteller
    
    def setHalle(self, halle):
        self.halle = halle
        
    def getHalle(self):
        return self.halle
    
    def setPlatznummer(self, platznummer):
        self.platznummer = platznummer
        
    def getPlatznummer(self):
        return self.platznummer
    
    def setWartung(self, wartung):
        self.wartung = wartung
        
    def getWartung(self):
        return self.wartung
        
    def checkWartungsintervall(self, minIntervall):
        wartung = self.wartung
        intervall = []
        for i in range (len(wartung)):
            if (i+1 < len(wartung)):
                datumA = wartung[i]["Datum"]
                datumB = wartung[i+1]["Datum"]
                a = datetime.datetime.strptime(datumA,"%d.%m.%Y")
                b = datetime.datetime.strptime(datumB,"%d.%m.%Y") 
                c = b-a
                if (c.days > minIntervall):
                     intervall.append({"Datum": wartung[i+1]["Datum"],"Arbeiter": wartung[i+1]["von"]  , "Überschreitung": c.days-minIntervall})
        return intervall

if __name__ == "__main__":

    stanzmaschine1 = Stanzmaschine("datensatz1.json")
    stanzmaschine2 = Stanzmaschine("datensatz2.json")
    stanzmaschine3 = Stanzmaschine("datensatz3.json")
    stanzmaschine4 = Stanzmaschine("datensatz4.json")

    print(stanzmaschine1.getStandort())
    print(stanzmaschine1.getHersteller())
    print(stanzmaschine1.getWartung())
    print(stanzmaschine1.checkWartungsintervall(30))



