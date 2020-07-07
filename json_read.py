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
    f = open('{}'.format(arquivo_zip_json), 'r')

    # returns JSON object as dictionary
    data = json.load(f)

    # Iterating through the json
    # list

    a = 0

    sqlite_insert_with_param = """INSERT INTO dados_socios(numIndex, cpf, nomePrimeiro, nomeMeio, nomeUltimo) VALUES (?,?,?,?,?)"""

    for v in data[1]:

        tuplaData = (str(a),
                     str(v.get('pessoa')['cadastral'].get('CPF')),
                     str(v.get('pessoa')['cadastral'].get('nomePrimeiro')),
                     str(v.get('pessoa')['cadastral'].get('nomeMeio')),
                     str(v.get('pessoa')['cadastral'].get('nomeUltimo')))

        a += 1

        conn.execute(sqlite_insert_with_param, tuplaData)

        conn.commit()

    f.close()
    os.remove(arquivo_zip_json)
    print('Leitura concluida. Arquivo excluido.')


def lendoArquivos():

    for i in listdir('teste'):
        # try:

        if zip.is_zipfile(join('teste', i)):

            with zip.ZipFile('teste/{}'.format(i), 'r') as meuZip:

                meuZip.extract(member=str(meuZip.filelist[0]), path='api/')
                print(meuZip.filelist)

        # except:
        #     # print('deu ruim')
        #     continue


def lerZip():

    with zip.ZipFile('teste/00000000004502-FABIO AUGUSTO CANTIZANI BARBOSA.zip') as myzip:
        a = myzip.filename
        print(a)
        # with myzip.open('socios_json/00000000004502-FABIO AUGUSTO CANTIZANI BARBOSA.json') as myfile:
        # print(myfile.fileno())


"""
Função que cria a tabela de dados complementares no DB.
"""


def createTable():
    try:
        c.execute(
            "CREATE TABLE dados_socios(numIndex TEXT, cpf TEXT, nomePrimeiro TEXT, nomeMeio TEXT, nomeUltimo TEXT, nome_socio TEXT)"
        )
        c.execute(
            "CREATE UNIQUE INDEX idx_nome_socio ON dados_socios (nome_socio);"
        )
    except:
        print('\nOcorreu um erro ao criar a tabela. Verfique se já não está criada.')


# lerZip()
lendoArquivos()
# createTable()
# lerJson()
