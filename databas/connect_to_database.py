import csv
from pymongo import MongoClient

# Skapa en anslutning till MongoDB-servern
client = MongoClient('localhost', 27017)

# Välj eller skapa en databas
db = client['min_databas']

# Välj eller skapa en samling (original collection)
collection = db['min_samling']

# Skapa en ny samling (separate collection)
new_collection = db['fullstandig_db']

mexican_collection = db['mexikansk_db']

chilean_collection = db['chilensk_db']

csv_files = [
    'datasets/Chile_Primera_Division_2023_stats.csv',
    'datasets/Liga_MX_2023_stats.csv'
]

csv_files_mexico = [
    'datasets/Liga_MX_2023_stats.csv'
]

csv_files_chile = [
    'datasets/Chile_Primera_Division_2023_stats.csv'
]

# Läs innehållet i varje CSV-fil och lägg till i den nya samlingen
for file_path in csv_files:
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_collection.insert_one(row)

for file_path in csv_files_mexico:
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            mexican_collection.insert_one(row)

for file_path in csv_files_chile:
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            chilean_collection.insert_one(row)