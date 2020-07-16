import sqlite3 as sq

conn = sq.connect(
    "data/CNPJ_full.db"
)

c = conn.cursor()
