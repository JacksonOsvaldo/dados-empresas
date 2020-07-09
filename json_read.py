#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ler JSONS e, com base na leitura, criar tabela no db
"""
import os
import json
import zipfile as zip
import sqlite3 as sq
from os import listdir
from os.path import isfile, join


conn = sq.connect(
    "data/CNPJ_full.db"
)

c = conn.cursor()


def lerJson(arquivo_zip_json):
    # Opening JSON file
    f = open(arquivo_zip_json, 'r')
    print(f.name)

    # returns JSON object as dictionary
    data = json.load(f)

    # Iterating through the json
    # list

    a = 0

    sqlite_insert_with_param = """INSERT INTO cadastral(CPF, nomePrimeiro, nomeMeio, nomeUltimo, nomeParentesco) VALUES (?,?,?,?,?)"""

    try:
        for v in data['result']:

            tuplaData = (str(v.get('pessoa')['cadastral'].get('CPF')),
                         str(v.get('pessoa')['cadastral'].get('nomePrimeiro')),
                         str(v.get('pessoa')['cadastral'].get('nomeMeio')),
                         str(v.get('pessoa')['cadastral'].get('nomeUltimo')),
                         str(v.get('pessoa')['cadastral'].get('nomeParentesco')))
            print(tuplaData)

            a += 1

            conn.execute(sqlite_insert_with_param, tuplaData)

            conn.commit()

            f.close()

            continue
        os.remove(arquivo_zip_json)
        print('Leitura concluida.')

    except:

        os.remove(arquivo_zip_json)

        print('Arquivo excluido. TypeERROR')


def lendoArquivos():

    for i in listdir('teste'):

        if zip.is_zipfile(join('teste', i)):

            with zip.ZipFile('teste/{}'.format(i), 'r') as meuZip:

                meuZip.extractall(path='api/')

                teste = listdir('api/socios_json/')

                lerJson('api/socios_json/'+teste[0])


"""
Função que cria a tabela de dados complementares no DB.
"""


def createTable():
    try:

        c.execute(
            "CREATE TABLE cadastral(CPF TEXT, nomePrimeiro TEXT, nomeMeio TEXT, nomeUltimo TEXT, nomeParentesco TEXT, sexo TEXT, dataNascimento TEXT, statusReceitaFederal TEXT, rgNumero TEXT, rgOrgaoEmissor TEXT, rgUf TEXT, tituloEleitoral TEXT, obito TEXT, nacionalidade TEXT, menorDeIdade TEXT, pep TEXT, estadoCivil TEXT, maeCPF TEXT, maeNomePrimeiro TEXT, maeNomeMeio TEXT, maeNomeUltimo TEXT, maeNomeParentesco TEXT, escolaridade TEXT, cns TEXT)"
        )

        # c.execute(
        #     "CREATE UNIQUE INDEX idx_nome_socio ON dados_socios (nome_socio);"
        # )
    except:
        print('\nOcorreu um erro ao criar a tabela. Verfique se já não está criada.')


# def testeJson():
#     # Opening JSON file
#     f = open('teste/00000000004502-FABIO AUGUSTO CANTIZANI BARBOSA.json', 'r')
#     # print(f.name)

#     # returns JSON object as dictionary
#     data = json.load(f)

#     a = 0

#     for v in data['result']:
#         a += 1

#         for key in v.get('pessoa')['cadastral']:
#             # coluna = list(key)
#             valor = tuple(v.get('pessoa')['cadastral'].get(key))
#             print(valor)

#             # conn.execute(
#             #     'INSERT INTO cadastral({}) VALUES ({})'.format(coluna, valor))
#             # conn.commit()
#             continue

#         if a == 10:
#             break

def testeJson():

    f = open('teste/00000000004502-FABIO AUGUSTO CANTIZANI BARBOSA.json', 'r')
    print(f.name)

    # returns JSON object as dictionary
    data = json.load(f)

    colunas = list()
    linha = list()
    a = 0
    b = ('')
    for v in data['result']:

        # print(v.values())

        a += 1

        for t in v.get('pessoa')['cadastral']:

            if v.get('pessoa')['cadastral'].get(t) == None:
                b = "''"+','+b
            else:
                b = v.get('pessoa')['cadastral'].get(t)+','+b

        print(tuple(b))
        if a == 1:
            break

        # sql = 'INSERT INTO cadastral ({}) VALUES (?)'.format(t)
        # conn.execute(sql, [v.get('pessoa')['cadastral'].get(
        #     t)] + [v.get('pessoa')['cadastral'].get(t)])
        # conn.commit()


testeJson()
# lerZip()
# lendoArquivos()
# createTable()
# lerJson()
