
import json
import datetime

from Blech import Blech

class Stanzmaschine():

    raw = ""
    hersteller = ""
    standort = ""
    halle = ""
    platznummer = ""
    wartung = ""
    
    blech = []
    stanzMuster = []
    stanzMusterNummer = ""
    
    
    def __init__(self, jsonData):
        self.leseConfigdatei(jsonData)
        self.standort = self.raw["Standort"]
        self.hersteller = self.raw["Hersteller"]
        self.wartung = self.raw["Wartung"]
        self.halle = self.standort["Halle"]
        self.platznummer = self.standort["Platz"]
        self.stanzMuster = self.raw["Muster"]
        self.stanzMusterNummer = self.raw["MusterNr"]
        
    def leseConfigdatei(self, jsonData):
       with open(jsonData, "r") as datei:
            self.raw = json.load(datei)
    
    def showConfig(self):
        return json.dumps(self.raw, indent=4)
        
    def setStanzMuster(self, stanzMuster):
        self.stanzMuster = stanzMuster
        
    def getStanzMuster(self):
        for zeile in self.stanzMuster:
            print(zeile)
                    
    def setStanzMusterNummer(self, stanzMusterNummer):
        self.stanzMusterNummer = stanzMusterNummer
        
    def getStanzMusterNummer(self):
        return self.stanzMusterNummer
        
    def setBlech(self):
        self.blech = Blech()
        
    def getBlech(self):
        return self.blech
    
    def stanze(self):
        self.setBlech()
        for zeile in range (len(self.stanzMuster)):
            for spalte in range (len(self.stanzMuster[zeile])):
                if self.stanzMuster[zeile][spalte] == 0:
                    self.blech.entfernen(zeile,spalte)
        return self.blech
                    
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
    
    
    #print(stanzmaschine1.getStandort())
    #print(stanzmaschine1.getHersteller())
    #print(stanzmaschine1.getWartung())
    #print(stanzmaschine1.checkWartungsintervall(30))
    #print(stanzmaschine1.setBlech())
    #print(stanzmaschine1.getBlech())
    stanzmaschine1.stanze()
    print(stanzmaschine1.blech.zeigeBlech())
    
    stanzmaschine2.stanze()
    print(stanzmaschine2.blech.zeigeBlech())
    
    stanzmaschine3.stanze()
    print(stanzmaschine3.blech.zeigeBlech())
    
    
    
    
    
    
    
  


