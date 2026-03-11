from project_2 import valid_email
from project_2 import valid_password

def test_valid_email():
    assert valid_email("de1@kent.ac.uk") == True
    assert valid_email("gk4@gmail.com") == True

def test_invalid_email():
   assert valid_email("ds1@kent.ac.fe.uk") == False
   assert valid_email("dsa@gmail@com") == False


def test_valid_password():
    assert valid_password("123456") == True
    assert valid_password("342465") == True

def test_invalid_password():
    assert valid_password("543533636") == False
    assert valid_password("qwretry") == False