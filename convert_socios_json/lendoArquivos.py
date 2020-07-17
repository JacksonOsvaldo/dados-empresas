from os.path import isfile, join
from os import listdir
import os
import json
import zipfile as zip
import shutil

from pymongo import MongoClient


def movendoArquivo(nome_do_arquivo_zip):

    shutil.move('{}'.format(nome_do_arquivo_zip), './data/JSON/PF')

    print('Arquivo lido e movido para /data/JSON/PF')


def importMongo(nome_arquivo):

    client = MongoClient('localhost', 27017)
    db = client.dados
    collection_currency = db.socios

    print(collection_currency)

    with open('{}'.format(nome_arquivo)) as f:
        file_data = json.load(f)

    # if pymongo >= 3.0 use insert_one() for inserting one document
    collection_currency.insert_one(file_data)
    client.close()
    print('Arquivo importado.')


def lendoArquivos():

    for i in listdir('./teste'):

        if zip.is_zipfile(join('teste', i)):

            with zip.ZipFile('teste/{}'.format(i), 'r') as meuZip:

                # print(meuZip.filename)

                meuZip.extractall(path='api/')

                teste = listdir('api/socios_json/')

                importMongo('api/socios_json/'+teste[0])
                movendoArquivo(meuZip.filename)
                # os.remove('api/socios_json/'+teste[0])


lendoArquivos()
