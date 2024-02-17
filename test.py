# from pymongo import MongoClient
# client= MongoClient('mongodb://muthumani:muthumani%40098@localhost:27017/?authSource=users')
# db=client.muthumani_blog
# result=db.test.find_one({"username":"muthumani"})
# res=db.test.find()
# print(res)

# print(result)
from src import getConfig
print(getConfig("mongodb_string"))