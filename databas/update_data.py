from .connect_to_database import collection

# Uppdatera ett dokument i samlingen, ej aktiv
query = {"name": "Alice"}
new_values = {"$set": {"age": 35}}
result = collection.update_one(query, new_values)
print("Modified documents count:", result.modified_count)
