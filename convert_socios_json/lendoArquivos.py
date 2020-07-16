from os.path import isfile, join
from os import listdir
import os
import json
import zipfile as zip
import shutil

from convert_socios_json import cadastral as cds
from convert_socios_json import beneficiarioProgramaSocial as bps
from convert_socios_json import contatoEndereco as ce
from convert_socios_json import contatoEmail
from convert_socios_json import contatoTelefones


def movendoArquivo(nome_do_arquivo_zip):

    shutil.move('{}'.format(nome_do_arquivo_zip), './data/JSON/PF')

    print('Arquivo lido e movido para /data/JSON/PF')


def lendoArquivos():

    for i in listdir('./teste'):

        if zip.is_zipfile(join('teste', i)):

            with zip.ZipFile('teste/{}'.format(i), 'r') as meuZip:

                # print(meuZip.filename)

                meuZip.extractall(path='api/')

                teste = listdir('api/socios_json/')

                # cds.lerJson('api/socios_json/'+teste[0])
                # bps.lerJson('api/socios_json/'+teste[0])
                # ce.lerJson('api/socios_json/'+teste[0])
                # contatoEmail.lerJson('api/socios_json/'+teste[0])
                contatoTelefones.lerJson('api/socios_json/'+teste[0])

                movendoArquivo(meuZip.filename)
                # os.remove('api/socios_json/'+teste[0])
