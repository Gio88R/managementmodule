from flask import Flask, request, redirect, url_for, render_template
from databas import insert_data, retrieve_data, delete_data
from modules.table import populate_document_table
app = Flask(__name__)

# Flask-rutt för att ta bort dokument
@app.route('/delete_document', methods=['POST'])
def delete_document_route():
    player = request.form['player']
    deleted_count = delete_data.delete_document(player)
    if deleted_count > 0:
        return redirect(url_for('index'))
    else:
        return "Document not found"

# flask
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        position = request.form['position']
        date = request.form['date']
        found = request.form['found']
        player = request.form['player']
        born = request.form['born']
        nationality = request.form['nationality']
        club = request.form['club']
        status = request.form['status']
        comment = request.form['comment']
        xTransferValue = request.form['xTransferValue']
        report = request.form['report']
        insert_data.insert_document(position, date, found, player, born, nationality, club, status, comment, xTransferValue, report)
        return redirect(url_for('index'))
    else:
        #documents = retrieve_data.get_documents()
        table = populate_document_table()
        return render_template('index.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)

