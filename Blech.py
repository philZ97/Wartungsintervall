# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:14:49 2022

@author: Philipp Ziegler
"""

n=10


class Blech:
    
    raster = [["1"]*n for i in range(n)]
    programm = []

    def _init_(self, raster):
        self.raster = raster
        
    def getRaster(self):
        return self.raster
    
    def setProgramm(self, programmNr):
        self.programm.append(programmNr)
        print(f"{programmNr} wurde als Programm gesetzt")
        
    def getProgramm(self):
        return self.programm
    
    def zeigeBlech(self):
        for zeile in self.raster:
            for spalte in zeile:
                print(spalte, end="|")
            print()
        
    def entfernen(self, x,y):
        self.raster [x][y] = 0
        return self.raster
        

if __name__ == "__main__":
    
    blech1 = Blech()
    
    print(blech1.getProgramm())
    blech1.setProgramm([1,2,3])
    print(blech1.getProgramm())
    #print(blech1.zeigeBlech())

    