#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Código para consulta e listagem de CNPJs que tem informações incompletas ou espaços vazios.
"""

import sqlite3 as sq

conn = sq.connect(
    "data/CNPJ_full.db"
)

c = conn.cursor()


def cnpjEmpresas():

    cnpj = open("lista_cnpjs_vazios.csv", "w")

    print("Iniciando processamento da Tabela EMPRESAS...")

    for row in c.execute("SELECT * from empresas"):

        if any(i == '' for i in row[22:29]):

            cnpj.write((row[0] + ",\n"))

    print("Processamento da Tabela EMPRESAS Concluido")

    cnpj.close()


def nomeSocios():

    socios = open("lista_socios_vazios.csv", "w")

    print("Iniciando processamento da Tabela SOCIOS...")

    for row in c.execute("SELECT cnpj, nome_socio from socios"):

        socios.write("{}".format(row[0]) + ",{}".format(row[1]) + ",\n")

    print("Processamento da Tabela SOCIOS Concluido")

    socios.close()


cnpjEmpresas()
nomeSocios()
