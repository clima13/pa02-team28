import sqlite3

class Transaction:
    def __init__(self, database):
        self.database = database

        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS transactions \
                    (itemnumber text, amount int, category text, date int, \
                    description text)")
        con.commit()
        con.close()
