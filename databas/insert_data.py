from .connect_to_database import collection

def insert_document(Pos, date, found, Player, born, nationality, Team, status, comment, xTransferValue, report):

    new_document = {
        "Pos": Pos,
        "date": date,
        "found": found,
        "Player": Player,
        "born": born,
        "nationality": nationality,
        "Team": Team,
        "status": status,
        "comment": comment,
        "xTransferValue": xTransferValue,
        "report": report
    }
    result = collection.insert_one(new_document)
    return result.inserted_id