from os import listdir
import os
import json
import zipfile as zip
import shutil
import glob

from pymongo import MongoClient


def movendoArquivo(nome_do_arquivo_zip):

    fileName_absolute = os.path.basename(nome_do_arquivo_zip)

    pasta = fileName_absolute.replace('.zip', '')[0:2]
    sub_pasta = fileName_absolute.replace('.zip', '')[2:5]

    try:
        shutil.move('{}'.format(nome_do_arquivo_zip),
                    '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/CNPJ/{}/{}/'.format(pasta, sub_pasta))
        print('ZIP lido e movido para /data/JSON/CNPJ')
    except:
        os.makedirs(
            '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/CNPJ/{}/{}/'.format(pasta, sub_pasta))
        shutil.move(nome_do_arquivo_zip,
                    '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/CNPJ/{}/{}/'.format(pasta, sub_pasta))
        print('ZIP lido e movido para /data/JSON/CNPJ')


def importMongo(nome_arquivo, collection_db):

    try:

        with open('{}'.format(nome_arquivo)) as f:
            file_data = json.load(f)
        # if pymongo >= 3.0 use insert_one() for inserting one document
        collection_db.insert_one(file_data)
        print('Arquivo importado.')

    except:

        print('Erro no aquivo')


def lendoArquivos():

    path = '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/teste/*/*/'
    pasta_extrair = '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/api'

    # Criando conexão com DB
    print('\nIniciando conexão com servidor')
    client = MongoClient(
        'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    db = client.dados
    collection_currency = db.empresas

    for filename in glob.glob(os.path.join(path, '*.zip')):

        print('\nLendo: ', filename)

        with zip.ZipFile(filename, 'r') as meuZip:

            # Extraindo ZIP para o caminho indicado na variável pasta_extrair
            meuZip.extractall(path=pasta_extrair)

            # Diretório para onde os JSON Foram extraídos.
            json_folder = listdir(
                '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/api/cnpjs_json')

            # Caminho do JSON extraído.
            json_file = '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/api/cnpjs_json/' + \
                json_folder[0]

            # Importando JSON para o mongo.
            importMongo(json_file, collection_currency)

            # Removendo JSON
            os.remove(json_file)
            print('Arquivo JSON excluido')

            # Movendo ZIP para outra pasta.
            try:
                movendoArquivo(meuZip.filename)
                # shutil.rmtree(os.path.dirname(meuZip.filename))
            except:
                print('Arquivo já existe')
                os.remove(meuZip.filename)

    # Fechando cliente do servidor depois de realizado processo de inserção dos JSON

    print('\nProcesso concluído\nFechando conexão...')
    client.close()
    print('Conexão encerrada.')


if __name__ == "__main__":

    lendoArquivos()
