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
    return db

@pytest.mark.delete
def test_delete(empty_db):
    ''' add two transactions, remove one and make sure it was removed '''
    empty_db.add(1, 1, "food", 20220324, "")
    empty_db.add(2, 1, "food", 20220324, "")

    transactions1 = empty_db.select_all()

    empty_db.delete(2)

    transactions2 = empty_db.select_all()

    assert len(transactions2) == 1
    assert transactions2[0]['item #'] == 1

@pytest.mark.summarizemonth
def test_summarize_by_month(empty_db):
    ''' add a few transactions, ensure that only the correct one makes it '''
    empty_db.add(1, 1, "food", 20220324, "")
    empty_db.add(1, 1, "food", 20220424, "")
    empty_db.add(1, 1, "food", 20220524, "")

    transactions_april = empty_db.summarize_by_month(4)

    assert len(transactions_april) == 1
    assert transactions_april[0]['date'] == 20220424