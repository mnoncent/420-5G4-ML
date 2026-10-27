# import numpy as nmp
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('future.no_silent_downcasting', True)

# nosPokemons = pd.read_csv("datas/pokedex.csv")

# # #Affichage des colonnes du Dataframe
# # print(nosPokemons.columns.values)
# # print(nosPokemons.head(10))

# # remplacement de VRAI FAUX par 1 0
# nosPokemonsClean = nosPokemons
# nosPokemonsClean["LEGENDAIRE"] = nosPokemonsClean["LEGENDAIRE"].replace("VRAI", 1)
# nosPokemonsClean["LEGENDAIRE"] = nosPokemonsClean["LEGENDAIRE"].replace("FAUX", 0)
# nosPokemonsClean["LEGENDAIRE"] = nosPokemonsClean["LEGENDAIRE"].astype(int)
# # print(nosPokemonsClean.head())

# #Comptage du nombre d'observations et de features
# # print(nosPokemonsClean.shape)

# #Informations sur notre jeu de donnees
# # print(nosPokemonsClean.info())
# print(nosPokemonsClean[nosPokemonsClean['NOM'].isnull()])
# nosPokemonsClean.loc[62, 'NOM'] = "Colossinge"
# print(nosPokemonsClean['NOM'][62])

combats = pd.read_csv("datas/combats.csv")

#Affichage des colonnes du Dataframe
print(combats.columns.values)

#Affichage des 10 premières lignes du Dataframe
print(combats.head(10))

#Comptage du nombre de lignes et de colonnes
print (combats.shape)

#Informations sur notre jeu de données
print (combats.info())

nbFoisPremierePosition = combats.groupby('Premier_Pokemon').count()
print(nbFoisPremierePosition)