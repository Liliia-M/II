from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['users']
# db2 = client['books']
persons = db.persons


doc = {"author": "Peter",
        "age": 38,
        "text": "is cool! Wildberry",
        "tags": ['cool', 'hot', 'ice'],
        "date": '14.06.1983'}

persons.insert_one(doc)

for doc in persons.find():
    print(doc)