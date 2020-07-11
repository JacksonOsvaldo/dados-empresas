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

            db.conn.execute('INSERT INTO cadastral ('+keys +
                            ') VALUES ('+question_marks+')', values)

            db.conn.commit()
        os.remove(arquivo_zip_json)
        print('Leitura concluida.')

    except:

        os.remove(arquivo_zip_json)

        print('Arquivo excluido. TypeERROR')


"""
Função que cria a tabela de dados complementares no DB.
"""


# def createTable():
#     try:

#         c.execute(
#             "CREATE TABLE cadastral(CPF TEXT, nomePrimeiro TEXT, nomeMeio TEXT, nomeUltimo TEXT, nomeParentesco TEXT, sexo TEXT, dataNascimento TEXT, statusReceitaFederal TEXT, rgNumero TEXT, rgOrgaoEmissor TEXT, rgUf TEXT, tituloEleitoral TEXT, obito TEXT, nacionalidade TEXT, menorDeIdade TEXT, pep TEXT, estadoCivil TEXT, maeCPF TEXT, maeNomePrimeiro TEXT, maeNomeMeio TEXT, maeNomeUltimo TEXT, maeNomeParentesco TEXT, escolaridade TEXT, cns TEXT)"
#         )

#         # c.execute(
#         #     "CREATE UNIQUE INDEX idx_nome_socio ON dados_socios (nome_socio);"
#         # )
#     except:
#         print('\nOcorreu um erro ao criar a tabela. Verfique se já não está criada.')
