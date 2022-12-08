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

#cries dir path
path = "./pokecries"
dir = os.listdir(path)

#Dropping columns if they exist, and creating a new one
mycol = mydb["cries"]

####-------- WinError 32 ------######
#### https://stackoverflow.com/questions/68465210/problem-downloading-mega-files-with-python/68465437#68465437
#### link tells you how to fix it ####
# SPECIFY DOWNLOAD LOCATION
if len(dir) == 0:
    mycol.drop()
    mycol = mydb["cries"]
    i = 1
    for i in range(1, 3):
        filename = str(i)+".mp3"
        file = m.find(filename)
        m.download(file, './pokeCries')
        path = os.getcwd()+"\pokeCries\/"+str(i)+".mp3"
        tmp = { "dexno": i, "path": path}
        mycol.insert_one(tmp)
        i+=1
    print("done")
else:
    print("not empty")

#def saveCry(pokeDex):
#    filename = pokeDex
#    file = m.find(filename)
#    m.download(file, './pokeCries')

def getCry(num):
    pkquery = {"dexno": num}
    pkname = mycol.find(pkquery, {'path': 1, "_id": 0})
    return pkname[0]['path']

