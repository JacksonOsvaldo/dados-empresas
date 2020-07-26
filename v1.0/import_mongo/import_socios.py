from os import listdir
import os
import json
import zipfile as zip
import shutil
import glob

from pymongo import MongoClient


def movendoArquivo(nome_do_arquivo_zip):

    shutil.move('{}'.format(nome_do_arquivo_zip),
                '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/PF')

    print('ZIP lido e movido para /data/JSON/PF')


def importMongo(nome_arquivo):

    client = MongoClient('localhost', 27017)
    db = client.dados
    collection_currency = db.socios

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
    pasta_extrair = '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/api'

    for filename in glob.glob(os.path.join(path, '*.zip')):

        print('\nLendo: ', filename)

        with zip.ZipFile(filename, 'r') as meuZip:

            # Extraindo ZIP para o caminho indicado na variável pasta_extrair
            meuZip.extractall(
                path=pasta_extrair)

            # Diretório para onde os JSON Foram extraídos.
            json_folder = listdir(
                '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/api/socios_json/')

            # Caminho do JSON extraído.
            json_file = '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/api/socios_json/' + \
                json_folder[0]

            # Importando JSON para o mongo.
            importMongo(json_file)

            # Removendo JSON
            os.remove(json_file)
            print('Arquivo JSON excluido')

            # Movendo ZIP para outra pasta.
            try:

                movendoArquivo(meuZip.filename)

            except shutil.Error as e:

                print('Arquivo já existe: ', e)

                os.remove(meuZip.filename)


if __name__ == "__main__":

    lendoArquivos()
