import tbl

pets_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSK2rd47ogfI2CpQi2L6HDo9AOEhnhqBN4zR4kLPUO28vBzmlc8XQWrvTfBYCU0ePf478yxcNKdOy5m/pub?gid=0&single=true&output=csv"

a_tbl = tbl.tbl(url = pets_url)
a_tbl.show_columns()