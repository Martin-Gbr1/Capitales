from types import new_class
from Dico import Capitales
import random

items = list(Capitales.items())
items = random.sample(items,len(items))

New_Capitales = dict(items)

for keys in New_Capitales :
    Reponse = input("Quelle est la capitale de " + keys + "? ")

    if Reponse == New_Capitales.get(str(keys)) :
        print("Bravo l'artiste ! ")
    
    else :
        Mauvaise_Reponse = 0
        while Reponse != New_Capitales.get(str(keys)) :
            Reponse = input("Désolé bro... Essaye encore : ")
            Mauvaise_Reponse = Mauvaise_Reponse + 1

            if Mauvaise_Reponse >= 3 :
                List_Reponse = [random.sample(list(Capitales.values()), 3), Capitales.get(str(keys))]
                List_Reponse = random.sample(List_Reponse, len(List_Reponse))
                
                print(*List_Reponse)
                Reponse = input("Choisi la bonne réponse dans les villes ci-dessus : ")
        print("Bravo !")

print("Ça y est tu as fait le tour du monde ! ")