#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import shutil

a = 0

print('\nOrganizando pastas. Aguarde...')
# first get full file name with directores using for loop
for fileName_relative in glob.glob("/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/CNPJ/*.zip", recursive=True):

    # Now get the file name with os.path.basename
    fileName_absolute = os.path.basename(fileName_relative)

    pasta = fileName_absolute.replace('.zip', '')[0:2]
    sub_pasta = fileName_absolute.replace('.zip', '')[2:5]

    a += 1
    print('\nArquivo: ', fileName_absolute, '\nNúmero: ', a)

    try:
        shutil.move(fileName_relative,
                    '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/CNPJ/{}/{}/'.format(pasta, sub_pasta))
        print('Movido para: ', pasta, '/', sub_pasta)
    except:
        os.makedirs(
            '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/CNPJ/{}/{}/'.format(pasta, sub_pasta))
        shutil.move(fileName_relative,
                    '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/CNPJ/{}/{}/'.format(pasta, sub_pasta))
        print('Movido para: ', pasta, '/', sub_pasta)
        continue

print('Processo concluido.')
