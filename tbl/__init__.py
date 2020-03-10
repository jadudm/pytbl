#The MIT License
# Copyright (c) Matthew C. Jadud <matt@jadud.com>

# This code is being developed in conjunction with a series of blog
# posts at https://jadud.com/. Many aspects are therefore being 
# staged, so that they are incrementally addressed, as opposed to
# being implemented "all-at-once".

# Imports
import csv
import requests
from types import SimpleNamespace
from collections import namedtuple as NT

# Local imports
from tbl import util
from tbl import validation as V

# NamedTuples provide simple record-type structures for giving
# names to information. I don't need full classes here (yet),
# but I don't want to use plain lists or tuples, because down that road
# lies madness. There will ultimately be quite a few, and I'll probably
# move them into their own namespace.
# http://bit.ly/2PVUSha
Column = NT("Column", ["name", "type"])

class tbl:

  def __init__(self, url=None, has_header=True):
    # A SimpleNamespace is really an empty object that
    # lets me set, modify, and delete attributes.
    # http://bit.ly/3aHq2Rx
    self.fields = SimpleNamespace()
    # Initialize fields
    self.fields.columns = list()
    self.fields.rows = list()
    self.fields.status = V.OK()

    # Handle keywords
    if url:
      self.fields.status = V._check_from_sheet(url, has_header)
      if isinstance(self.fields.status, V.OK):
        self.from_sheet(url, has_header=has_header)

  def _add_column(self, column):
    self.fields.columns.append(column)
    # Add the columns to the object as an attribute.
    # Storing the column object in the value of the attribute.
    # FIXME: Should I lowercase everything? Or, follow the conventions of 
    # the underlying data? This will matter when dealing with DBs, etc.
    setattr(self, column.name.lower(), column)

  def _add_row(self, row):
    self.fields.rows.append(row)
  
  def _set_rows(self, rows):
    self.fields.rows = rows

  def _get_column_index(self, C):
    ndx = 0
    for index, c in enumerate(self.fields.columns):
      if c.name == C.name:
        ndx = index
    return ndx

  def from_sheet(self, url, has_header=True):
    self.fields.url = url
    with requests.Session() as s:
      download = s.get(self.fields.url)
      content = download.content.decode('utf-8')
      reader = csv.reader(content.splitlines(), delimiter=',')
      # FIXME: I need to conditionally handle the absence of a header.
      if has_header:
        header_row = next(reader)
        for name in header_row:
          # FIXME: I need to guess the type of the column here.
          self._add_column(Column(name=name, type=None))
      else: # No header
        # FIXME: Define some exceptions and raise one.
        # http://bit.ly/2TC3yve
        pass
      
      for row in reader:
        self._add_row(row)


def show_columns (a_tbl):
  for c in a_tbl.fields.columns:
    print("{} : {}".format(util.pad(c.name, limit=12, side=util.RIGHT), c.type))

def show_tbl (a_tbl):
  field_width = 12
  for c in a_tbl.fields.columns:
    print(util.pad(c.name, limit=field_width), end="")
  print()
  for r in a_tbl.fields.rows:
    for v in r:
      print(util.pad(v, limit=field_width), end="")
    print()

