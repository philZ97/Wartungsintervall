# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 08:17:00 2021

@author: Philipp Ziegler
"""

import glob
from Stanzmaschine import Stanzmaschine
from Blech import Blech

class MaschinenSteuerung():

    maschinenListe = []
    
    def __init__(self):
        self.setMaschinenListe()
        self.blech = Blech()

    def setMaschinenListe(self):
        dateiListe = glob.glob("*.json")

        for datei in dateiListe:
            self.maschinenListe.append(Stanzmaschine(datei))
        
    def getMaschinenListe(self):
        return self.maschinenListe
    
    def addMaschine(self, path):
        self.maschinenListe.append(Stanzmaschine(path))
        print("Maschine mit ",path, "hinzugefügt")
    
    def ausbuchen(self, platznummer, halle):

        maschineGefunden = False

        for maschine in self.maschinenListe:

            if maschine.getPlatznummer() == platznummer and maschine.getHalle() == halle:
                
                print("maschine mit den eigenschaften wird entfernt....")
                print(maschine)

                self.maschinenListe.remove(maschine)
                maschineGefunden = True

        if maschineGefunden == False:
            print("keine maschine mit den angegebenen parametern gefunden")
    
    def produziere(self, programmNr):
        maschinenPark.blech.setProgramm(programmNr)
        programm = maschinenPark.blech.getProgramm()
        for programmCode in programm:
            for programmSchritt in programmCode:
                maschinenPark.maschinenListe[programmSchritt-1].stanze()
        print(maschinenPark.blech.zeigeBlech())
        
maschinenPark = MaschinenSteuerung()

"""for maschine in maschinenPark.maschinenListe:
    print(maschine.getHersteller())"""

#print(maschinenPark.maschinenListe[2].getHersteller())
#print(maschinenPark.maschinenListe[0].getPlatznummer())
#print(maschinenPark.maschinenListe[0].getHalle())
#print(maschinenPark.ausbuchen(12,2))
#print(maschinenPark.getMaschinenListe())
#print(maschinenPark.addMaschine("datensatz1.json"))
#print(maschinenPark.getMaschinenListe())
#maschinenPark.maschinenListe[0].setBlech()
#print(maschinenPark.maschinenListe[0].blech.zeigeBlech())
#maschinenPark.maschinenListe[0].stanze()
#print(maschinenPark.maschinenListe[0].blech.zeigeBlech())
maschinenPark.produziere([3,4])