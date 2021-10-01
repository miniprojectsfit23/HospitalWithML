from pymongo import MongoClient
import os
MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
client = pymongo.MongoClient('mongodb+srv://'+MONGODB_USERNAME+':'+MONGODB_PASS+'@cluster0.xz3j1.mongodb.net/HospitalWithMLDB?retryWrites=true&w=majority')
db = client['HospitalWithMLDB']