import tbl
from tbl import validation as V

pets_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSK2rd47ogfI2CpQi2L6HDo9AOEhnhqBN4zR4kLPUO28vBzmlc8XQWrvTfBYCU0ePf478yxcNKdOy5m/pub?gid=0&single=true&output=csv"

def test_bool_url():
  a_tbl = tbl.tbl(url = True)
  assert type(a_tbl.fields.status) is V.KO

def test_int_url():
  a_tbl = tbl.tbl(url = 1)
  assert type(a_tbl.fields.status) is V.KO

def test_url_str_not_url():
  a_tbl = tbl.tbl(url = "lobster")
  assert type(a_tbl.fields.status) is V.KO

def test_url_list_bool():
  a_tbl = tbl.tbl(url = [True])
  assert type(a_tbl.fields.status) is V.KO

def test_url_list_int():
  a_tbl = tbl.tbl(url = [1])
  assert type(a_tbl.fields.status) is V.KO

def test_url_list_str():
  a_tbl = tbl.tbl(url = ["lobster"])
  assert type(a_tbl.fields.status) is V.KO

def test_list_good_url():
  a_tbl = tbl.tbl(url = ["https://lobster.org/northaven.csv"])
  assert type(a_tbl.fields.status) is V.KO

def test_protocol():
  a_tbl = tbl.tbl(url = "http")
  assert type(a_tbl.fields.status) is V.KO

def test_protocol_s():
  a_tbl = tbl.tbl(url = "https")
  assert type(a_tbl.fields.status) is V.KO

def test_partial_url():
  a_tbl = tbl.tbl(url = "https://lobster")
  assert type(a_tbl.fields.status) is V.KO

# Technically, this is a good URL, but we have no idea if 
# it serves up a CSV file. 
def test_good_url_not_csv():
  a_tbl = tbl.tbl(url = "https://lobster.org/")
  assert type(a_tbl.fields.status) is V.KO

def test_good_url_not_csv2():
  a_tbl = tbl.tbl(url = "https://lobster.org/northhaven")
  assert type(a_tbl.fields.status) is V.KO

def test_good_url_txt():  
  a_tbl = tbl.tbl(url = "https://lobster.org/northhaven.txt")
  assert type(a_tbl.fields.status) is V.KO

def test_goog_url_incomplete():
  a_tbl = tbl.tbl(url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSK2rd47ogfI2CpQi2L6HDo9AOEhnhqBN4zR4kLPUO28vBzmlc8XQWrvTfBYCU0ePf478yxcNKdOy5m/pub?gid=0&single=true")
  assert type(a_tbl.fields.status) is V.KO

def test_complete_goog_url():
  a_tbl = tbl.tbl(url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSK2rd47ogfI2CpQi2L6HDo9AOEhnhqBN4zR4kLPUO28vBzmlc8XQWrvTfBYCU0ePf478yxcNKdOy5m/pub?gid=0&single=true&output=csv")
  assert type(a_tbl.fields.status) is V.OK
  