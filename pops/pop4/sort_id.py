# **********************************
# ORDENANDO IDS EN UNA BASE DE DATOS
# **********************************


def sort_id(db: list[dict]) -> list[dict]:
    sorted_db = db.copy()
    for i in range(len(sorted_db)):
        sorted_db[i]["id"] = i + 1
    return sorted_db
