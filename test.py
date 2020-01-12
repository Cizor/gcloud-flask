import pymongo

client = pymongo.MongoClient(
        "mongodb+srv://Cizor:best123@cluster0-wazd4.gcp.mongodb.net/test?retryWrites=true&w=majority")

b = client.list_database_names()

c = client.sample_mflix
d = c.comments
for i in d.find():
    print(i)

'''
db = client.sample_mflix
cursor = db.find({})
for document in cursor:
    print(document)
'''