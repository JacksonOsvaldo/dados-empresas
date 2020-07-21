# -*- coding: utf-8 -*-

import json
# import sqlite3 as sq
import os
from convert_socios_json import db
from convert_socios_json import criarTabela as ct


def lerJson(arquivo_zip_json):
    # Opening JSON file
    f = open(arquivo_zip_json, 'r')
    # print(f.name)

    # returns JSON object as dictionary
    data = json.load(f)

    # Iterating through the json
    # list

    try:
        print('Extraindo contatos: Endereco..')
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
                    db.conn.execute('INSERT INTO pf_contato_endereco (CPF,'+keys +
                                    ') VALUES ('+question_marks+')', values)

                    db.conn.commit()

                except ct.db.sq.OperationalError:
                    ct.contato_endereco()
                    db.conn.execute('INSERT INTO pf_contato_endereco (CPF,'+keys +
                                    ') VALUES ('+question_marks+')', values)

                    db.conn.commit()

        # f.close()
        # os.remove(arquivo_zip_json)
        # print('Leitura concluida.')

    except:

        # os.remove(arquivo_zip_json)

        print('Arquivo excluido. TypeERROR')


"""
Função que cria a tabela de dados complementares no DB.
"""
