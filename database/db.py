from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
# client = client.vestaboard # For production
client = client.installableqa # For testing
