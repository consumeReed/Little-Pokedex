import requests
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["pokedex"]
mycol = mydb["ALLPKMN"]
mycol.drop()
mycol = mydb["ALLPKMN"]

showcol = mydb["showdown"]
showcol.drop()
showcol = mydb["showdown"]

allurl = 'https://pokeapi.co/api/v2/pokemon?limit=151&offset=0'

allresponse = requests.get(allurl)
alldata = allresponse.json()

for i in range(151):
    tmp = { "name": alldata['results'][i]['name'], "dexno": i+1}
    mycol.insert_one(tmp)

showdownurl = 'https://play.pokemonshowdown.com/data/pokedex.json'

showdownresponse = requests.get(showdownurl)
showdowndata = showdownresponse.json()

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