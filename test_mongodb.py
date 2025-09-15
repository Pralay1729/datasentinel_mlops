
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://pralay1729_db_user:Pralay123@cluster0.pzfju3n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# from pymongo.mongo_client import MongoClient
# from urllib.parse import quote_plus

# username = quote_plus("pralay1729_db_user")
# password = quote_plus("Pralay123")
# cluster = "cluster0.ajwayfc.mongodb.net"

# print(f"Username: '{username}'")
# print(f"Password: '{password}'")

# uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0"
# print(f"URI: {uri}")

# client = MongoClient(uri)

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)