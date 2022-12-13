#pokeapi
#pulls pokemon: id, name, moves, types, dex entry from pokeapi
#written by: Rich Erskine

import pymongo
import requests
import sys
non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode+1), 0xfffd)

#connecting to Mongodb and making database + col
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['pokedex']

mycol = mydb["firstgen"]

if mycol.count_documents({}) != 151:
    mycol.drop()
    mycol = mydb["firstgen"]
    #need 2 urls to connect to the pokemon and dex entries
    url = "https://pokeapi.co/api/v2/pokemon/"
    url2 = "https://pokeapi.co/api/v2/pokemon-species/"

    #iterator through pokemon that start at 1
    i=1
    poketype = ""
    pokemoves= ""

    #this is the first generation pokemon and we are only gathering 151
    for i in range(151):
        url += str(i+1)
        url += "/"
        url2 += str(i+1)
        url2 += "/"

        #first request is for the pokemon data
        response = requests.get(url)
        data = response.json()

        pokeid = data['id']
        pokename = data['name']

        #type and moves are arrays so we need to break them down
        for j in data['types']:
            x= j['type']['name'].translate(non_bmp_map)
            poketype += x + "\n"
            
        for k in data['moves']:
            p= k['move']['name'].translate(non_bmp_map)
            pokemoves += p + "\n"

        #changing url to dex entry data
        response = requests.get(url2)
        data = response.json()
        j = 1
        while True:
            pokedex = data['flavor_text_entries'][j]['flavor_text']
            if data['flavor_text_entries'][j]['language']['name'] == 'en':
                break
            j = j + 1
        jpnname = data['names'][0]['name']

        #input data into database
        myentry = { "id": pokeid, "name": pokename, "jpnname": jpnname, "types": poketype, 
                    "moves": pokemoves, "pokedexentry": pokedex }
        x = mycol.insert_one(myentry)

        #reset/increment
        url = "https://pokeapi.co/api/v2/pokemon/"
        url2 = "https://pokeapi.co/api/v2/pokemon-species/"
        poketype = ""
        pokemoves = ""

def getJpnname(name):
    pkquery = { "name": name}
    pktypes = mycol.find(pkquery, {"jpnname": 1, "_id": 0})
    return pktypes[0]['jpnname']

def getMoves(name):
    pkquery = { "name": name}
    pktypes = mycol.find(pkquery, {"moves": 1, "_id": 0})
    return pktypes[0]['moves']

def getEntry(name):
    pkquery = { "name": name}
    pktypes = mycol.find(pkquery, {"pokedexentry": 1, "_id": 0})
    return pktypes[0]['pokedexentry']
