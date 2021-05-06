from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
def loadkey():
    """ Loads the key from the current directory"""
    return open("Mongo.key","r").read()




client = MongoClient()
db = client.test

# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
print(serverStatusResult)