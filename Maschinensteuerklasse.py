# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 08:17:00 2021

@author: Philipp Ziegler
"""

import glob
from Wartungsintervall_Klasse import Stanzmaschine

class MaschinenSteuerung():
    maschinenListe = []
    dateiliste = None
    
    def __init__(self, dateiliste):
        self.dateiliste = glob.glob("*.json")
        self.maschinenListe(dateiliste)
        
    def setMaschinenListe(self, dateiliste):
        #dateiliste = glob.glob("*.json")
        for datei in dateiliste:
            self.MaschinenListe.append(Stanzmaschine(datei))
        
    def getMaschinenListe(self):
        return self.MaschinenListe

    def getDateiliste(self):
        return self.dateiliste
    
    def einbuchen(eineMaschine):
        pass
    
    def ausbuchen():
        pass

maschinenPark = MaschinenSteuerung()
maschinenPark.setMaschinenListe()
print(maschinenPark.getMaschinenListe())
    