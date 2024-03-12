from .connect_to_database import collection

def get_documents():
    return collection.find({}, {'_id': 0}) # Include all fields except '_id'