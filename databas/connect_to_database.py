from pymongo import MongoClient

# Skapa en anslutning till MongoDB-servern
client = MongoClient('localhost', 27017)

# Välj eller skapa en databas
db = client['min_databas']

# Välj eller skapa en samling
collection = db['min_samling']