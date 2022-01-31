from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


# db.movies.update_many({조건}, {'$set': 어떻게 변경})



db.movies.update_many({'star': '0' }, {'$set': {'star': '9.38'}})