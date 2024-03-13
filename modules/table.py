
# import things
from flask_table import Table, Col
from databas.retrieve_data import get_documents, get_players
from markupsafe import Markup
def _recursive_getattr(obj, attr_list):
    if not attr_list:
        return obj
    attr = attr_list[0]
    if hasattr(obj, attr):
        return _recursive_getattr(getattr(obj, attr), attr_list[1:])
    return None
# Declare table
class DocumentTable(Table):
    position = Col('Pos')
    date = Col('Date')
    found = Col('Found Via')
    player = Col('Player')
    born = Col('Born')
    nationality = Col('Nationality')
    team = Col('Team')
    status = Col('Status')
    comment = Col('Comment')
    xTransferValue = Col('xTransferValue')
    report = Col('Report')

class fullTable(Table):
    pos = Col('Pos')
    date = Col('Date')
    found = Col('Found Via')
    player = Col('Player')
    born = Col('Born')
    nationality = Col('Nationality')
    team = Col('Team')
    status = Col('Status')
    comment = Col('Comment')
    xTransferValue = Col('xTransfer Value')
    report = Col('Report')

    # Define the columns as a set for easy lookup
    columns = {
        'pos', 'date', 'found', 'player', 'born', 'nationality',
        'team', 'status', 'comment', 'xTransferValue', 'report'
    }

    # Override the td_contents method to handle Item objects
def td_contents(self, item, attr_list):
    out = _recursive_getattr(item, attr_list)
    if isinstance(out, dict):
        # If the output is a dictionary, access the value using the key
        out = out[attr_list[0]]
    return self.td_format(out)

# Simple class to convert dictionaries to objects with attributes
class Item:
    def __init__(self, data):
        self.__dict__.update(data)

# Populate table with data from database
def populate_document_table():
    documents = get_documents()
    # Convert MongoDB cursor to a list
    documents_list = [doc for doc in documents]
    # Populate table
    print(documents)
    table = DocumentTable(documents_list)
    return table

def populate_second_table():
    # Retrieve the documents from new_collection
    documents = get_players() # Assuming get_players() retrieves from new_collection
    # Convert MongoDB cursor to a list
    documents_list = [doc for doc in documents]
    # Create a new list of Item objects with the data from the documents
    items = [Item(doc) for doc in documents_list]
    # Populate the table
    full_table = fullTable(items)
    return full_table