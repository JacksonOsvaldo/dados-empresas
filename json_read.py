#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ler JSONS e, com base na leitura, criar tabela no db
"""

import json
import sqlite3 as sq

conn = sq.connect(
    "data/CNPJ_full.db"
)

c = conn.cursor()


def createTable():
    try:
        c.execute("CREATE TABLE dados_socios(numIndex TEXT, cpf TEXT, nomePrimeiro TEXT, nomeMeio TEXT, nomeUltimo TEXT, nome_socio TEXT)")
        c.execute(
            "CREATE UNIQUE INDEX idx_nome_socio ON dados_socios (nome_socio);")
    except:
        print('\nOcorreu um erro ao criar a tabela. Verfique se já não está criada.')


def lerJson():
    # Opening JSON file
    f = open(
        """teste/socios_json/00000000004502-FABIO AUGUSTO CANTIZANI BARBOSA.json""", 'r'
    )

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list

    a = 0

    sqlite_insert_with_param = """INSERT INTO dados_socios(numIndex, cpf, nomePrimeiro, nomeMeio, nomeUltimo) VALUES (?,?,?,?,?)"""

    for v in data['result']:

        tuplaData = (str(a),
                     str(v.get('pessoa')['cadastral'].get('CPF')),
                     str(v.get('pessoa')['cadastral'].get('nomePrimeiro')),
                     str(v.get('pessoa')['cadastral'].get('nomeMeio')),
                     str(v.get('pessoa')['cadastral'].get('nomeUltimo')))

        a += 1

        conn.execute(sqlite_insert_with_param, tuplaData)

        conn.commit()

    f.close()


def updateDB(parameter_list):
    pass


createTable()
# lerJson()
