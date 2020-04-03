from pymongo import MongoClient

client = MongoClient("mongodb+srv://analytics:analytics-password@mflix-vfdsr.mongodb.net/test?retryWrites=true&w=majority")


print(client.mflix)
