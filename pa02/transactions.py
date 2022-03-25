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

    def delete(self, itemnumber):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("DELETE FROM transactions WHERE itemnumber=(?);",
                    (itemnumber,))
        con.commit()
        con.close()

    def summarize_by_month(self, month):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("SELECT * FROM transactions WHERE date%10000/100=(?);",
                    (month,))
        transactions = cur.fetchall()
        con.close()
        return self.list_to_dict(transactions)
