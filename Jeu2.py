from Dico import Capitales
import random

for keys in Capitales.keys() :
    RdmCap = random.sample(list(Capitales.keys()),1)
    Reponse = input("Quelle est la capitale de " + str(RdmCap) + "? ")

    if Reponse == Capitales.get(str(RdmCap)) :
        print("Bravo. ")
    else :
        while Reponse != Capitales.get(str(RdmCap)) :
            Reponse = input("Nan mec, essaye encore. Quelle est la capitale de " + str(RdmCap) + "? ")   
        print("Bravo, au suivant ? ")
