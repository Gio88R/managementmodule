from .connect_to_database import collection

def insert_document(position, date, found, player, born, nationality, club, status, comment, xTransferValue, report):

    new_document = {
        "position": position,
        "date": date,
        "found": found,
        "player": player,
        "born": born,
        "nationality": nationality,
        "club": club,
        "status": status,
        "comment": comment,
        "xTransferValue": xTransferValue,
        "report": report
    }
    result = collection.insert_one(new_document)
    return result.inserted_id