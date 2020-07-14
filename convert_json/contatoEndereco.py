# -*- coding: utf-8 -*-

import json
# import sqlite3 as sq
import os
from convert_json import db
from convert_json import criarTabela as ct


def lerJson(arquivo_zip_json):
    # Opening JSON file
    f = open(arquivo_zip_json, 'r')
    print(f.name)

    # returns JSON object as dictionary
    data = json.load(f)

    # Iterating through the json
    # list

    try:
        print('Convertendo contatos')
        for v in data['result']:

            listaValores = v.get('pessoa').get('contato').get('endereco')

    # print(v.get('pessoa').get('cadastral').get('CPF'), len(linha))

            for valor in range(len(listaValores)):

                try:

                    linha = v.get('pessoa').get(
                        'contato').get('endereco')[valor]

                    keys = ','.join(linha.keys())

                    # print(keys)

                    values = tuple(linha.values())
                    values = (v.get('pessoa').get(
                        'cadastral').get('CPF'),) + values
                    question_marks = ','.join(list('?'*(len(values))))

                    # print(values)
                    db.conn.execute('INSERT INTO contato (CPF,'+keys +
                                    ') VALUES ('+question_marks+')', values)

                    db.conn.commit()

                except ct.db.sq.OperationalError:
                    ct.contato()
                    db.conn.execute('INSERT INTO contato (CPF,'+keys +
                                    ') VALUES ('+question_marks+')', values)

                    db.conn.commit()

        os.remove(arquivo_zip_json)
        print('Leitura concluida.')

    except ct.db.sq.OperationalError:

        ct.cadastral()

        db.conn.execute('INSERT INTO cadastral ('+keys +
                        ') VALUES ('+question_marks+')', values)

        db.conn.commit()

    except:

        os.remove(arquivo_zip_json)

        print('Arquivo excluido. TypeERROR')


"""
Função que cria a tabela de dados complementares no DB.
"""
