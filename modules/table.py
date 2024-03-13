# import things
from flask_table import Table, Col
from databas.retrieve_data import get_documents
from markupsafe import Markup
# Declare table
class DocumentTable(Table):
    Pos = Col('Pos')
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
# Populate table with data from database
def populate_document_table():
    documents = get_documents()
# Convert MongoDB cursor to a list     documents_list = [doc for doc in documents]  
#Populate table
    print(documents)
    table = DocumentTable(documents)
    return table  