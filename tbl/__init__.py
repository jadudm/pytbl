#The MIT License
# Copyright (c) Matthew C. Jadud <matt@jadud.com>

# This code is being developed in conjunction with a series of blog
# posts at https://jadud.com/. Many aspects are therefore being 
# staged, so that they are incrementally addressed, as opposed to
# being implemented "all-at-once".

# Imports
import csv
import requests

def from_sheet(csv_url):
  with requests.Session() as s:
    download = s.get(csv_url)
    content = download.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in list(reader):
      print (row)
