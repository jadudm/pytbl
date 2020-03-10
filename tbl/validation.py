import validators as val
from collections import namedtuple as NT
import re

OK = NT("OK", [])
KO = NT("KO", ["code", "message"])

# Error Codes
BAD_URL = 0
DOES_NOT_END_IN_CSV = 1
URL_NOT_A_STRING = 2

def _check_from_sheet(url, has_header):
  # These will "fail fast."
  # Make sure it is a string.
  if not isinstance(url, str):
    return KO(URL_NOT_A_STRING, "The URL you passed does not look like a string: {}".format(url))
  if not val.url(url):
    return KO(BAD_URL, "The URL '{}' appears to be invalid.".format(url))
  # Should the URL end in CSV? Am I guaranteed that a Google Sheets 
  # CSV URL will end this way? This might get tricky.
  # If it is a sheets URL, and the letters "csv" appear in the URL, it will be OK.
  if (re.search("docs.google.com", url)
      and re.search("spreadsheets", url)
      and re.search("csv", url)):
      return OK()
  # If it isn't a sheets URL, then perhaps it is a valid URL that 
  # just points to a CSV. Therefore, it should end in '.csv'.
  if not (re.search(".csv$", url) or re.search(".CSV$", url)):
    return KO(DOES_NOT_END_IN_CSV, "The file you linked to does not end in '.csv'.")
  return OK() 

