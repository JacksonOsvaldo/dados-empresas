#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para geração de relatórios com base em FIND/QUERY feitas em DB do MongoDB.

O objetivo é inserir um CNAE e, com base na cidade/estadO, retornar os valores correspondentes exportando-os para CSV.


A planilha precisa ter os seguintes campos:

- CNPJ,
- RAZÃO SOCIAL,
- DATA DE ABERTURA,
- CNAE CÓDIGO,
- CNAE DESCRIÇÃO,
- PORTE,
- FAIXA DE FUNCIONÁRIOS,
- FAIXA DE FUNCIONÁRIOS FATURA,
- UF,
- CIDADE,
- LOGRADOURO,
- E-MAIL,
- TELEFONE.

"""

from pymongo import MongoClient

client = MongoClient(
    'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
filter = {
    '$and': [
        {
            'result.empresa.firmografico.cnae.cnae_codigo': {
                '$eq': '6911701'
            }
        },
        {
            'result.empresa.contato.endereco.cidade': {
                '$eq': 'ARARAQUARA'
            }
        }
    ]
}

result = client['dados']['empresas'].find(filter=filter)

a = 0

for i in result:

    for j in i.get('result'):

        a += 1

        item = j.get('empresa')

        # keys = ','.join(item.keys())

        values = tuple(item.values())
        print(j)

        # if j['empresa']['firmografico']['cnae'][0]['cnae_codigo'] == '6911701':

        #     print(j)
