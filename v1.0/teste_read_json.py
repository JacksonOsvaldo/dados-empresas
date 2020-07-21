# -*- coding: utf-8 -*-

import json
from convert_socios_json import db

f = open('./teste/socios_json/TEREZINHA FURTADO GUEDES.json', 'r')
print(f.name)

# returns JSON object as dictionary
data = json.load(f)

a = 0

for v in data['result']:

    # listaValores = v.get('pessoa').get('vinvulo')

    a += 1

    linha = v.get('pessoa').get('vinculo')

    for i in linha:
        print(i)

    keys = ','.join(linha.keys())

    print(linha, '\n', keys)

    question_marks = ','.join(list('?'*len(linha)))

    values = tuple(linha.values())
    print(values)

    if a == 1:
        break

    # for valor in range(len(listaValores)):

    #     linha = v.get('pessoa').get(
    #         'contato').get('telefone')[valor]

    #     keys = ','.join(linha.keys())

    #     print(keys)

    #     values = tuple(linha.values())
    #     values = (v.get('pessoa').get(
    #         'cadastral').get('CPF'),) + values
    #     question_marks = ','.join(list('?'*(len(values))))

    #     print(values)
    #     db.conn.execute('INSERT INTO pf_contato_telefones (CPF,'+keys +
    #                     ') VALUES ('+question_marks+')', values)

    #     db.conn.commit()

    # print(values)
