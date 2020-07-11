import sqlite3 as sq

import json as js

conn = sq.connect(
    "data/CNPJ_full.db"
)

c = conn.cursor()

f = open('teste/00000000004502-FABIO AUGUSTO CANTIZANI BARBOSA.json', 'r')

print(f.name)

# returns JSON object as dictionary

data = js.load(f)

linha = dict()
row = list()
a = 0
for v in data['result']:

    # print(v.get('pessoa').get('contato'))
    # linha = v.get('pessoa').get('contato').get('endereco')
    # values = tuple(linha.values())

    print(v.get('pessoa').get('contato').get('endereco'))
    if a == 1:
        break


# for v in data['result']:

#     linha = v.get('pessoa').get('cadastral')

#     keys = ','.join(linha.keys())

#     question_marks = ','.join(list('?'*len(linha)))

#     values = tuple(linha.values())

#     print(values)

#     conn.execute('INSERT INTO contatos ('+keys +
#                  ') VALUES ('+question_marks+')', values)

#     conn.commit()
