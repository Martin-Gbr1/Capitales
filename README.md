# Capitales
Jeu des capitales

Le code génère bien une capitale aléatoire 
Je ne veux pas de répétition dans les questions (pas de doublon)

La méthode random.choice fonctionne mais fait des doublons

La méthode random.sample ne fait pas de doublons mais j'ai un pb :
    Les input() d'après ne souhaite pas concaténer des str avec des list
    Donc j'ai choisi d'appeler la fonction str() pour convertir la liste RdmCap en str

Or dans la console le résultat n'est pas : "Quelle est la capitale de Ouganda ?" mais, "Quelle est la capitale de ['Oudanda']"

Comment faire en sorte de ne plus avoir les crochets ? 

Merci !!
      
