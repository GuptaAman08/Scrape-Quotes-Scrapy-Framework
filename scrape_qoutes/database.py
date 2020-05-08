# NOTE => Use this file for manually intervening in our existing sqlite DB.

import sqlite3

conn = sqlite3.connect("quotes.db")
cur = conn.cursor()

# cur.execute("""
#                 create table quotes_tb(
#                     title text,
#                     author text,
#                     tag text
#                 )
#             """)

# cur.execute("""
#                 insert into quotes_tb values ("Jo Dar Gaya Wo Ghar Gaya", "Akshay Kumar", "Dare")
#             """)

# ans = cur.execute("""Select count(*) from quotes_tb""")
cur.execute("""DROP TABLE IF EXISTS quotes_tb""")

conn.commit()
conn.close()

