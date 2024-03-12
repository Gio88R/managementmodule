from .connect_to_database import collection

def delete_document(player):
    query = {"player": player}
    result = collection.delete_one(query)
    return result.deleted_count
