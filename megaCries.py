import requests
import pymongo
from mega import Mega
import os

#Setting up the connection to Mongo DB
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["pokedex"]

#Setting up connection to Mega API
mega = Mega()
m = mega.login("peaksk85@students.rowan.edu", "Kingdom#7467sora")

#Dropping columns if they exist, and creating a new one
mycol = mydb["cries"]
if mycol.count_documents({}) != 151:
    mycol.drop()
    mycol = mydb["cries"]
    # Grabs link and puts it into cries db
    print("Starting link retrieval from api. This may take a few minutes")
    for i in range(1, 152):
        filename = str(i)+".mp3"
        file = m.find(filename)
        link = m.get_link(file)
        print(str(i) + " of 151")
        tmp = { "dexno": i, "url": link}
        mycol.insert_one(tmp)


    #def saveCry(pokeDex):
    #    filename = pokeDex
    #    file = m.find(filename)
    #    m.download(file, './pokeCries')

def getCry(num):
    pkquery = {"dexno": num}
    pkname = mycol.find(pkquery, {'url': 1, "_id": 0})
    return pkname[0]['url']

