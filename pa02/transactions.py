import sqlite3

def to_trx_dict(trx_tuple):
    ''' trx is a trxegory tuple (rowid, name, desc)'''
    trx = {'itemnumber':trx_tuple[1], 'amount':trx_tuple[2], 'category':trx_tuple[3], 
            'date':trx_tuple[4], 'description':trx_tuple[5]}
    return trx

def to_trx_dict_list(trx_tuples):
    ''' convert a list of trxegory tuples into a list of dictionaries'''
    return [to_trx_dict(trx) for trx in trx_tuples]


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
    def select_all(self):
        ''' return all of the categories as a list of dicts.'''
        con= sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("SELECT itemnumber,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trx_dict_list(tuples)

    def select_one(self,itemnumber):
        ''' return a category with a specified rowid '''
        con= sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("SELECT itemnumber,* from transactions where itemnumber=(?)",(itemnumber,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trx_dict(tuples[0])

    def add(self,item):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['itemnumber'],item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        # cur.execute("SELECT last_insert_itemnumber()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        # return last_rowid[0]

    def summarize_trx_by_date(self):
        con= sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("SELECT date,sum(amount) from transactions group by date")
        con.commit()
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return tuples

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
        cur.execute("SELECT itemnumber,* FROM transactions WHERE date%10000/100=(?);",
                    (month,))
        transactions = cur.fetchall()
        con.close()
        return to_trx_dict_list(transactions)

    def summarize_by_year(self, year):#Bradley added this
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("SELECT itemnumber,* FROM transactions WHERE date/10000=(?);",
                    (year,))
        transactions = cur.fetchall()
        con.close()
        return to_trx_dict_list(transactions)

    def summarize_by_category(self, cat):#Bradley added this
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("SELECT itemnumber,* FROM transactions WHERE category=(?);",
                    (cat,))
        transactions = cur.fetchall()
        con.close()
        return to_trx_dict_list(transactions)

    def summarize_by_description(self, info): #Nathan added this
        #My interpretation of the question is print the menu of the selected catagory
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("SELECT itemnumber,* FROM transactions WHERE description=(?);",
                    (info,))
        transactions = cur.fetchall()
        con.close()
        return to_trx_dict_list(transactions)
