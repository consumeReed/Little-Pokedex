import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["pokedex"]
showcol = mydb["showdown"]


def getDex(num):
    pkquery = {"num": num}
    pkname = showcol.find(pkquery, {'name': 1, "_id": 0})
    return pkname[0]['name']

test = getDex(3)
print(test)

def getTypes(name):
    pkquery = { "name": name}
    pktypes = showcol.find(pkquery, {"types": 1, "_id": 0})
    return pktypes[0]['types']

test2 = getTypes('bulbasaur')
print(test2)

def getStats(name):
    pkquery = { "name": name}
    pkstats = showcol.find(pkquery, {"baseStats": 1, "_id": 0})
    return pkstats[0]['baseStats']

test3 = getStats('bulbasaur')
print(test3)