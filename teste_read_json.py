from os.path import isfile, join
from os import listdir
import os
import zipfile as zip
import shutil


def lendoArquivos():

    for i in listdir('teste'):

        if zip.is_zipfile(join('teste', i)):

            with zip.ZipFile('teste/{}'.format(i), 'r') as meuZip:

                meuZip.extractall(path='api/')
                shutil.move(meuZip.filename(), 'teste/dados')
                teste = listdir('api/socios_json/')
                print(meuZip.filename())

                # os.remove('api/socios_json/'+teste[0])


lendoArquivos()
