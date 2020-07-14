import sqlite3 as sq

import json as js

conn = sq.connect(
    "data/CNPJ_full.db"
)

c = conn.cursor()

f = open('teste/00000000004502-FABIO AUGUSTO CANTIZANI BARBOSA.json', 'r')

# print(f.name)

# returns JSON object as dictionary

data = js.load(f)

a = int(0)

for v in data['result']:

    a += 1

    listaValores = v.get('pessoa').get('contato').get('endereco')

    # print(v.get('pessoa').get('cadastral').get('CPF'), len(linha))

    for valor in range(len(listaValores)):

        try:

            linha = v.get('pessoa').get('contato').get('endereco')[valor]

            keys = ','.join(linha.keys())

            print(keys)

            values = tuple(linha.values())
            values = (v.get('pessoa').get('cadastral').get('CPF'),) + values
            question_marks = ','.join(list('?'*(len(values))))

            print(values)
            conn.execute('INSERT INTO contato (CPF,'+keys +
                         ') VALUES ('+question_marks+')', values)

            conn.commit()

        except sq.OperationalError:

            c.execute(
                "CREATE TABLE contato(CPF TEXT, tipoLogradouro TEXT, logradouro TEXT, numero TEXT, complemento TEXT, bairro TEXT, cidade TEXT, uf TEXT, cep TEXT, ordem TEXT)"
            )

            # c.execute(
            #     "CREATE UNIQUE INDEX idx_CPF ON contato (CPF);"
            # )
            conn.execute('INSERT INTO contato (CPF,'+keys +
                         ') VALUES ('+question_marks+')', values)

            conn.commit()

    # if a == 1:

    #     break
