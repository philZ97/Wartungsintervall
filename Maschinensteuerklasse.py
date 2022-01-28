# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 08:17:00 2021

@author: Philipp Ziegler
"""

import glob
from Stanzmaschine import Stanzmaschine

class MaschinenSteuerung():

    maschinenListe = []
    
    def __init__(self):
        self.setMaschinenListe()

        
    def setMaschinenListe(self):
        dateiListe = glob.glob("*.json")

        for datei in dateiListe:
            self.maschinenListe.append(Stanzmaschine(datei))
        
    def getMaschinenListe(self):
        return self.maschinenListe

    def getDateiliste(self):
        return self.dateiliste
    
    def addMachine(path):
        self.maschinenListe.append(Stanzmaschine(path))
    
    def ausbuchen(self, platznummer, halle):

        maschineGefunden = False

        for maschine in self.maschinenListe:

            if maschine.getPlatznummer == platznummer and maschine.getHalle == halle:
                
                print("maschine mit den eigenschaften blalblalb wird entfernt....")
                print(maschine.show)

                self.maschinenListe.remove(maschine)
                maschineGefunden = True

        if maschineGefunden == False:
            print("keine maschine mit den angegebenen parametern gefunden")

maschinenPark = MaschinenSteuerung()

"""for maschine in maschinenPark.maschinenListe:
    print(maschine.getHersteller())"""

print(maschinenPark.maschinenListe[2].getHersteller())
