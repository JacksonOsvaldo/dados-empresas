#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import glob
import shutil


print('\nOrganizando pastas. Aguarde...')

a = 0

# first get full file name with directores using for loop
for fileName_relative in glob.glob("/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/PF/*.zip", recursive=True):

    # Now get the file name with os.path.basename
    fileName_absolute = os.path.basename(fileName_relative)

    nomeArquivo = fileName_absolute.replace('.zip', '')
    nomesPastas = nomeArquivo.split(' ')

    a += 1
    print('\nArquivo: ', fileName_absolute, '\nNúmero: ', a)

    try:
        os.makedirs('/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/PF/{}/{}/'.format(
            nomesPastas[0][0], nomesPastas[1][0]), exist_ok=True)
        shutil.move(fileName_relative, '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/PF/{}/{}/'.format(
            nomesPastas[0][0], nomesPastas[1][0]))
        print('Movido para: ', nomesPastas[0][0], '/', nomesPastas[1][0])

    except shutil.Error:

        os.remove(fileName_relative)

    except IndexError:
        os.makedirs('/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/PF/{}/{}/'.format(
            nomesPastas[0][0], nomesPastas[0][0]), exist_ok=True)
        shutil.move(fileName_relative, '/home/jacksonosvaldo/Documentos/GitHub_Projetos/dados-empresas/v1.0/data/JSON/PF/{}/{}/'.format(
            nomesPastas[0][0], nomesPastas[0][0]))
        print('Movido para: ', nomesPastas[0][0], '/', nomesPastas[0][0])

print('Processo concluido.')
