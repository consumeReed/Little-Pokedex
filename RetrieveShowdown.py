import pymongo
import requests

#Establish connection to Mongo DB
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["pokedex"]
showcol = mydb["showdown"]

#Returns string of pokemons name based on its dex no
def getDex(num):
    pkquery = {"num": num}
    pkname = showcol.find(pkquery, {'name': 1, "_id": 0})
    return pkname[0]['name']

#Returns list of strings of the pokemon's type(s)
def getTypes(name):
    pkquery = { "name": name}
    pktypes = showcol.find(pkquery, {"types": 1, "_id": 0})
    return pktypes[0]['types']

#Returns a list of strings of the pokemon's stats
def getStats(name):
    pkquery = { "name": name}
    pkstats = showcol.find(pkquery, {"baseStats": 1, "_id": 0})
    return pkstats[0]['baseStats']

#Returns weight value of pokemon
def getWeight(name):
    pkquery = { "name": name}
    pkstats = showcol.find(pkquery, {"weight": 1, "_id": 0})
    return pkstats[0]['weight']

#Returns height value of pokemon
def getHeight(name):
    pkquery = { "name": name}
    pkstats = showcol.find(pkquery, {"weight": 1, "_id": 0})
    return pkstats[0]['height']