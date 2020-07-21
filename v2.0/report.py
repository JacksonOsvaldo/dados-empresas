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

result = client['dados']['empresas'].find(
    filter=filter
)

a = 0

for i in result:
    a += 1
    # b = i.get('result').get('')
    for j in i.get('result'):
        # print(j.get('empresa'))
        for k in j.get('empresa'):
            print(k['cadastral'])
            if a == 3:
                break
