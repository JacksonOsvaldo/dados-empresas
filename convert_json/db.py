import json
import sqlite3 as sq
import os

conn = sq.connect(
    "data/CNPJ_full.db"
)

c = conn.cursor()
