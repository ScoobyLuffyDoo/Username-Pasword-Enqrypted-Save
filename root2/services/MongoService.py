import pymongo 
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
def loadkey():
    """ Loads the key from the current directory"""
    return open("Mongo.key","r").read()


myclient = pymongo.MongoClient(loadkey())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
else:
    print("DB does not exist")
# # Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# print(serverStatusResult)


# mydb = myclient["mydatabase"]

# mycol = mydb["customers"]