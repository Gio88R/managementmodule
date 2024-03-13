from pymongo import MongoClient
from flask import Flask, request, redirect, url_for, render_template, jsonify
from databas import insert_data, retrieve_data, delete_data
from modules.table import populate_document_table
app = Flask(__name__)

# Flask endpoint to list all collections
@app.route('/collections', methods=['GET'])
def get_collections():
    client = MongoClient('localhost', 27017)
    db = client['min_databas']
    collections = db.list_collection_names()
    return jsonify(collections)

# Flask endpoint to list players in a collection
@app.route('/players/<collection_name>', methods=['GET'])
def get_players(collection_name):
    client = MongoClient('localhost', 27017)
    db = client['min_databas']
    collection = db[collection_name]
    players = collection.find({}, {'Player': 1, '_id': 0})
    player_names = [player['Player'] for player in players]
    return jsonify(player_names)

# Flask-rutt för att ta bort dokument
@app.route('/delete_document', methods=['POST'])
def delete_document_route():
    Player = request.form['Player']
    deleted_count = delete_data.delete_document(Player)
    if deleted_count > 0:
        return redirect(url_for('index'))
    else:
        return "Document not found"

# flask
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Pos = request.form['Pos']
        date = request.form['date']
        found = request.form['found']
        Player = request.form['Player']
        born = request.form['born']
        nationality = request.form['nationality']
        Team = request.form['Team']
        status = request.form['status']
        comment = request.form['comment']
        xTransferValue = request.form['xTransferValue']
        report = request.form['report']
        insert_data.insert_document(Pos, date, found, Player, born, nationality, Team, status, comment, xTransferValue, report)
        return redirect(url_for('index'))
    else:
        #documents = retrieve_data.get_documents()
        table = populate_document_table()
        return render_template('index.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)

