from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/vestaboard')
client = client.vestaboard.installables

