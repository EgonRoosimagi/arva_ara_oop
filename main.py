from models.Stopwatch import Stopwatch
from models.Database import Database

if __name__ == '__main__':

    db = Database()
    data = db.read_records()
    if data:
        for record in data:
            print(record)


