#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para retorno do objeto que contém o CPF analisado.

"""

from pymongo import MongoClient

numero_CPF = input('CPF desejado: ')

client = MongoClient(
    'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')

# Criando filtro para busca do CPF
filter = {'result.pessoa.cadastral.CPF': {
    '$eq': '{}'.format(numero_CPF)}}

# Criando result do find.
result = client['dados']['socios'].find(filter=filter)

a = 0

# Varrendo o result
for i in result:

    # Procurando CPF
    for j in i.get('result'):

        if j['pessoa']['cadastral']['CPF'] == '{}'.format(numero_CPF):

            print('Documento: ', i['_id'], '\nObjeto: ', a)

        else:
            a += 1
