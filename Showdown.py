import requests
import pymongo

#Setting up the connection to Mongo DB
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["pokedex"]

#Dropping columns if they exist, and creating a new one
mycol = mydb["ALLPKMN"]
mycol.drop()
mycol = mydb["ALLPKMN"]

showcol = mydb["showdown"]
showcol.drop()
showcol = mydb["showdown"]

#Pokeapi url that has 151 pokemon 
allurl = 'https://pokeapi.co/api/v2/pokemon?limit=151&offset=0'

allresponse = requests.get(allurl)
alldata = allresponse.json()

#Storing each pokemon and its dex number in Mongo DB
for i in range(151):
    tmp = { "name": alldata['results'][i]['name'], "dexno": i+1}
    mycol.insert_one(tmp)

#Pokemon Showdown url that will be used to get more detailed info about pokemon
showdownurl = 'https://play.pokemonshowdown.com/data/pokedex.json'

showdownresponse = requests.get(showdownurl)
showdowndata = showdownresponse.json()

#Storing more data about each pokemon
for j in range(151):
    pkquery = { "dexno": j+1}
    pkname = mycol.find(pkquery, {"name": 1, "_id": 0})
    name = pkname[0]['name'].replace('-', '')
    
    types = showdowndata[name]['types']
    baseStats = showdowndata[name]['baseStats']
    weight = showdowndata[name]['weightkg']
    height = showdowndata[name]['heightm']
    num = showdowndata[name]['num']
    tmp = {'name': name, 'types': types, 'baseStats': baseStats, 'weight': weight, 'height': height, 'num': num}
    showcol.insert_one(tmp)