from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


#dx3J7qqNIXNiczl2 (tirar o maior e menor)
#vivianbritosenac_db_user
uri = "mongodb+srv://vivianbritosenac_db_user:dx3J7qqNIXNiczl2@cluster0.dlwxedb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" #conexão com o banco
# Create a new client and connect to the server

client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)