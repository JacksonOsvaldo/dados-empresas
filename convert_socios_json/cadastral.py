# -*- coding: utf-8 -*-

import json
# import sqlite3 as sq
import os
from convert_socios_json import db
from convert_socios_json import criarTabela as ct


def lerJson(arquivo_zip_json):
    # Opening JSON file
    f = open(arquivo_zip_json, 'r')
    print(f.name)

    # returns JSON object as dictionary
    data = json.load(f)

    try:
        print('Convertendo cadastros...')
        for v in data['result']:

            linha = v.get('pessoa').get('cadastral')

            keys = ','.join(linha.keys())

            question_marks = ','.join(list('?'*len(linha)))

            values = tuple(linha.values())

            # print(values)

            db.conn.execute('INSERT INTO cadastral ('+keys +
                            ') VALUES ('+question_marks+')', values)

            db.conn.commit()

        # os.remove(arquivo_zip_json)
        print('Leitura concluida.')

    except db.sq.OperationalError:

        ct.cadastral()

        db.conn.execute('INSERT INTO cadastral ('+keys +
                        ') VALUES ('+question_marks+')', values)

        db.conn.commit()

    except:

        # os.remove(arquivo_zip_json)

        print('Arquivo excluido. TypeERROR')


"""
Função que cria a tabela de dados complementares no DB.
"""
