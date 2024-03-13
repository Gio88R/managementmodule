from .connect_to_database import collection, new_collection

def get_documents():
    return collection.find({}, {'_id': 0}) # Include all fields except '_id'

def get_players():
    return new_collection.find({}, {'_id': 0}) # Include all fields except '_id'