#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ler JSONS e, com base na leitura, criar tabela no db
"""

from convert_socios_json import lendoArquivos
from convert_socios_json import criarTabela

if __name__ == "__main__":

    # criarTabela.cadastral()
    # criarTabela.beneficiarioProgramaSocial()
    # criarTabela.contato_endereco()
    # criarTabela.contato_email()
    criarTabela.contato_telefones()
    lendoArquivos.lendoArquivos()
