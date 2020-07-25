from os import listdir
import os
import json
import zipfile as zip
import shutil
import glob

from pymongo import MongoClient


def movendoArquivo(nome_do_arquivo_zip):

    shutil.move('{}'.format(nome_do_arquivo_zip),
                '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/CNPJ')

    print('ZIP lido e movido para /data/JSON/CNPJ')


def importMongo(nome_arquivo):

    client = MongoClient('localhost', 27017)
    db = client.dados
    collection_currency = db.empresas

    try:
        with open('{}'.format(nome_arquivo)) as f:
            file_data = json.load(f)
        # if pymongo >= 3.0 use insert_one() for inserting one document
        collection_currency.insert_one(file_data)
        client.close()
        print('Arquivo importado.')

    except:

        print('Erro no aquivo')


def lendoArquivos():

    path = '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/teste'

    for filename in glob.glob(os.path.join(path, '*.zip')):

        print('\nLendo: ', filename)

        with zip.ZipFile(filename, 'r') as meuZip:

            meuZip.extractall(
                path='/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/api')

            json_folder = listdir(
                '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/api/cnpjs_json')

            json_file = '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/api/cnpjs_json/' + \
                json_folder[0]

            importMongo(json_file)

            os.remove(json_file)

            print('Arquivo JSON excluido')

            movendoArquivo(meuZip.filename)


if __name__ == "__main__":

    lendoArquivos()
