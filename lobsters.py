from tbl import tbl, show_columns, show_tbl
from tbl.queries import gt, keep_rows_where

pets_url = "http://bit.ly/2IzVqoV"

print("The original table:")
T = tbl(url = pets_url)
show_tbl(T)

print()

print("The new table:")
newT = T |keep_rows_where| (T.weight |gt| 0.8)
show_tbl(newT)