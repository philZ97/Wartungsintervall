# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:14:49 2022

@author: Philipp Ziegler
"""
n = 10

class Blech:
    
    raster = [["1"]*n for i in range(n)]
    
    def _init_(self):
        #self.raster = [["1"]*n for i in range(n)]
        pass        
    def zeigeBlech(self):
        for zeile in self.raster:
            for spalte in zeile:
                print(spalte, end="|")
            print()

    def entfernen(self, x,y):
        self.raster [x][y] = 0
        return self.raster
        
       
blech1 = Blech()

#Blech1.zeigeBlech()
#Blech1.entfernen(2,7)
#Blech1.zeigeBlech()
#Blech1.entfernen(0,0)
#Blech1.zeigeBlech()