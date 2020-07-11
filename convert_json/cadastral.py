# -*- coding: utf-8 -*-

# import json_to_sqlite as jq
import json
import sqlite3 as sq
import os
from convert_json import db


def lerJson(arquivo_zip_json):
    # Opening JSON file
    f = open(arquivo_zip_json, 'r')
    print(f.name)

    # returns JSON object as dictionary
    data = json.load(f)

    # Iterating through the json
    # list

    try:
        for v in data['result']:

            linha = v.get('pessoa').get('cadastral')

            keys = ','.join(linha.keys())

            question_marks = ','.join(list('?'*len(linha)))

            values = tuple(linha.values())

            print(values)

            db.conn.execute('INSERT INTO contatos ('+keys +
                            ') VALUES ('+question_marks+')', values)

            db.conn.commit()

        os.remove(arquivo_zip_json)
        print('Leitura concluida.')

    # except sq.OperationalError as e:

    #     print(e)

    except:

        os.remove(arquivo_zip_json)

        print('Arquivo excluido. TypeERROR')


"""
Função que cria a tabela de dados complementares no DB.
"""
