#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Código para consulta e listagem de CNPJs e de Sócios que tem informações incompletas ou espaços vazios. O programa gera um .csv para leitura em PHP.
"""

import sqlite3 as sq

#Conectando ao banco de dados
conn = sq.connect(
    "../dataset_receita/DB/CNPJ_full.db"
)

c = conn.cursor()


# Lendo as informações de empresas.
def cnpjEmpresas():

    cnpj = open("lista_cnpjs_vazios.csv", "w") # Arquivo .csv gerado

    print("Iniciando processamento da Tabela EMPRESAS...")

    # Verificando a existência de campos vázios.
    for row in c.execute("SELECT * from empresas"):

        if any(i == '' for i in row[22:29]):

            cnpj.write((row[0] + ",\n")) # Salvando empresa com informações vazias no .csv

    print("Processamento da Tabela EMPRESAS Concluido")

    cnpj.close() # Fechando arquivo


def nomeSocios():

    socios = open("lista_socios_vazios.csv", "w") # Arquivo .csv gerado

    print("Iniciando processamento da Tabela SOCIOS...")

    # Verificando a existência de campos vázios.
    for row in c.execute("SELECT cnpj, nome_socio from socios"):

        socios.write("{}".format(row[0]) + ",{}".format(row[1]) + ",\n") # Salvando sócio com informações vazias no .csv

    print("Processamento da Tabela SOCIOS Concluido")

    socios.close() # Fechando o arquivo


cnpjEmpresas()
nomeSocios()
