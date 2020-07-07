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

    sqlite_insert_with_param = """INSERT INTO dados_socios(numIndex, cpf, nomePrimeiro, nomeMeio, nomeUltimo) VALUES (?,?,?,?,?)"""

    try:
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
            "CREATE TABLE dados_socios(numIndex TEXT, cpf TEXT, nomePrimeiro TEXT, nomeMeio TEXT, nomeUltimo TEXT, nome_socio TEXT)"
        )
        c.execute(
            "CREATE UNIQUE INDEX idx_nome_socio ON dados_socios (nome_socio);"
        )
    except:
        print('\nOcorreu um erro ao criar a tabela. Verfique se já não está criada.')


def testeJson():
    # Opening JSON file
    f = open('teste/00000000004502-FABIO AUGUSTO CANTIZANI BARBOSA.json', 'r')
    # print(f.name)

    # returns JSON object as dictionary
    data = json.load(f)

    a = 0
    tabelas = ['cadastral', 'beneficiarioProgramaSocial',
               'contato', 'vinculo', 'patrimonio', 'socioDemografico']

    cadastralKeys = ['CPF', 'nomePrimeiro', 'nomeMeio', 'nomeUltimo', 'nomeParentesco', 'sexo', 'dataNascimento', 'statusReceitaFederal', 'rgNumero', 'rgOrgaoEmissor', 'rgUf',
                     'tituloEleitoral', 'obito', 'nacionalidade', 'menorDeIdade', 'pep', 'estadoCivil', 'maeCPF', 'maeNomePrimeiro', 'maeNomeMeio', 'maeNomeUltimo', 'maeNomeParentesco', 'escolaridade', 'cns']
    for v in data['result']:
        a += 1
        teste = ""
        b = 0
        # for tabel in tabelas:
        #     print(tabel)
        #     b += 1
        for item in cadastralKeys:
            print(v.get('pessoa')['cadastral'].get(item))
        # b += 1
        #     # teste += key + ','
        #     print(valor)
        # # print(teste)
        if a == 1:
            break


testeJson()
# lerZip()
# lendoArquivos()
# createTable()
# lerJson()
