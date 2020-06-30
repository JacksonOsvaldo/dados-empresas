#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Código para consulta e ordenamento de CNAES.
"""

import pandas as pd
import sqlite3 as sq

conn = sq.connect('/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/data/CNPJ_full.db')

df = pd.read_sql_query("select * from empresas", conn)

print(df)
