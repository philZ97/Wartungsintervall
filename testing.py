#was brauch ich dafür?
import glob
from Stanzmaschine import Stanzmaschine
#was will ich rausbekommen?
maschinenListe = []
#was muss ich tun?
dateiliste = glob.glob("*.json")

for datei in dateiliste:
    maschinenListe.append(Stanzmaschine(datei))

#testen:
print(dateiliste)
