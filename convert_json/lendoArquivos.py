from os.path import isfile, join
from os import listdir
import json
import zipfile as zip

from convert_json import cadastral as cds


def lendoArquivos():

    for i in listdir('./teste'):

        if zip.is_zipfile(join('teste', i)):

            with zip.ZipFile('teste/{}'.format(i), 'r') as meuZip:

                meuZip.extractall(path='api/')

                teste = listdir('api/socios_json/')

                cds.lerJson('api/socios_json/'+teste[0])
