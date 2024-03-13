from .connect_to_database import collection

def insert_document(pos, date, found, player, born, nationality, team, status, comment, xTransferValue, report):

    new_document = {
        "pos": pos,
        "date": date,
        "found": found,
        "player": player,
        "born": born,
        "nationality": nationality,
        "team": team,
        "status": status,
        "comment": comment,
        "xTransferValue": xTransferValue,
        "report": report
    }
    result = collection.insert_one(new_document)
    return result.inserted_id