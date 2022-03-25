import pytest
from transactions import Transaction

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' creates a Transaction object with an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    trx1 = {'itemnumber':1,'amount':5, 'category':"sports", 'date':20220324, 'description':"-" }
    trx2 = {'itemnumber':2,'amount':5, 'category':"sports", 'date':20220324, 'description':"-" }
    trx3 = {'itemnumber':3,'amount':5, 'category':"sports", 'date':20220325, 'description':"-" }
    id1=empty_db.add(trx1)
    id2=empty_db.add(trx2)
    id3=empty_db.add(trx3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.mark.add
@pytest.mark.malai
def test_add(small_db):
    ''' add a category to db, the select it, then delete it'''

    trx4 = {'itemnumber':4,'amount':5, 'category':"sports", 'date':20220325, 'description':"-" }
    trx0 = small_db.select_all()
    small_db.add(trx4)
    trx1 = small_db.select_all()
    assert len(trx1) == len(trx0) + 1

@pytest.mark.delete
def test_delete(empty_db):
    ''' add two transactions, remove one and make sure it was removed '''
    empty_db.add({"itemnumber": 1, "amount": 1, "category": "food",
                  "date": 20220324, "description": ""})
    empty_db.add({"itemnumber": 2, "amount": 1, "category": "food",
                  "date": 20220324, "description": ""})

    transactions1 = empty_db.select_all()

    empty_db.delete(2)

    transactions2 = empty_db.select_all()

    assert len(transactions2) == 1
    assert transactions2[0]['itemnumber'] == '1'

@pytest.mark.summarizedate
@pytest.mark.malai
def test_summarize_by_date(small_db):
    ''' add a few transactions, summarize spending by date'''
    transactions_bydate = small_db.summarize_trx_by_date()

    assert len(transactions_bydate) == 2
    assert transactions_bydate[0][0] == 20220324
    assert transactions_bydate[0][1] == 10
    

@pytest.mark.summarizemonth
def test_summarize_by_month(empty_db):
    ''' add a few transactions, ensure that only the correct one makes it '''
    empty_db.add({"itemnumber": 1, "amount": 1, "category": "food",
                  "date": 20220324, "description": ""})
    empty_db.add({"itemnumber": 1, "amount": 1, "category": "food",
                  "date": 20220424, "description": ""})
    empty_db.add({"itemnumber": 1, "amount": 1, "category": "food",
                  "date": 20220524, "description": ""})

    transactions_april = empty_db.summarize_by_month(4)

    assert len(transactions_april) == 1
    assert transactions_april[0]['date'] == 20220424

@pytest.mark.summarizedescription
def test_summarize_by_description(empty_db):
    ''' add a few transactions, ensure that only the correct one makes it '''
    empty_db.add({"itemnumber": 1, "amount": 1, "category": "food",
                  "date": 20220324, "description": "test1"})
    empty_db.add({"itemnumber": 1, "amount": 1, "category": "mood",
                  "date": 20220424, "description": "test2"})
    empty_db.add({"itemnumber": 1, "amount": 1, "category": "dood",
                  "date": 20220524, "description": "test3"})

    transactions_test2 = empty_db.summarize_by_description("test2")

    assert len(transactions_test2) == 1
    assert transactions_test2[0]['date'] == 20220424
