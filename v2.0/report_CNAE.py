#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para geração de relatórios com base em FIND/QUERY feitas em DB do MongoDB.

O objetivo é inserir um CNAE e, com base na cidade/estado, retornar os valores correspondentes exportando-os para CSV.


A planilha precisa ter os seguintes campos:

- CNPJ,
- RAZÃO SOCIAL,
- SITUAÇÃO CADASTRAL,
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

numero_cnae = input('CNAE desejado: ')

client = MongoClient(
    'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')

filter = {'result.empresa.firmografico.cnae.cnae_codigo': {
    '$eq': '{}'.format(numero_cnae)}}

result = client['dados']['empresas'].find(filter=filter)

empresas = open("lista_empresas_{}.csv".format(
    numero_cnae), "w")  # Arquivo .csv gerado

a = 0

valores = tuple()


def pegarValores(valor):

    for item in valor:

        valores = tuple(item.values())

        return str(valores).replace('(', '').replace(')', '')


encon = 0
nao_encon = 0
erro_dados = 0

for i in result:

    try:

        a += 1

        if a == 1:

            empresas.write(
                'CNPJ;RAZÃO SOCIAL;SITUAÇÃO CADASTRAL;DATA DE ABERTURA;CNAE CÓDIGO;CNAE DESCRIÇÃO;PORTE;FAIXA DE FUNCIONÁRIOS;FAIXA DE FUNCIONÁRIOS FATURA;UF;CIDADE;LOGRADOURO;E-MAIL;TELEFONE\n')

        for j in i.get('result'):

            if j['empresa']['firmografico']['cnae'][0]['cnae_codigo'] == '{}'.format(numero_cnae):

                email = pegarValores(j['empresa']['contato']['email'])

                telefone = pegarValores(j['empresa']['contato']['telefone'])

                empresas.write(str(j['empresa']['cadastral']['CNPJ']) +
                               ';' + str(j['empresa']['cadastral']['razaoSocial']) +
                               ';' + str(j['empresa']['cadastral']['situacaoCadastral']) +
                               ';' + str(j['empresa']['cadastral']['dataAbertura']) +
                               ';' + str(j['empresa']['firmografico']['cnae'][0]['cnae_codigo']) +
                               ';' + str(j['empresa']['firmografico']['cnae'][0]['cnae_descricao']) +
                               ';' + str(j['empresa']['firmografico']['porte']) +
                               ';' + str(j['empresa']['firmografico']['faixaFuncionario']) +
                               ';' + str(j['empresa']['firmografico']['faixaFaturamento']) +
                               ';' + str(j['empresa']['contato']['endereco'][0]['uf']) +
                               ';' + str(j['empresa']['contato']['endereco'][0]['cidade']) +
                               ';' + str(j['empresa']['contato']['endereco'][0]['tipoLogradouro']) +
                               ' ' + str(j['empresa']['contato']['endereco'][0]['logradouro']) +
                               ', nº ' + str(j['empresa']['contato']['endereco'][0]['numero']) +
                               ', Bairro ' + str(j['empresa']['contato']['endereco'][0]['bairro']) +
                               ', CEP: ' + str(j['empresa']['contato']['endereco'][0]['cep']) +
                               ';'+str(email)+';'+str(telefone) + ';\n')
                encon += 1

            else:

                nao_encon += 1

    except:
        erro_dados += 1

print('Informações encontradas: {}\nInformações não-válidas: {}\nDocumentos sem CNAE (ERROR): {}\nDocumento salvo como: lista_empresas_{}.csv'.format(encon,
                                                                                                                                                      nao_encon, erro_dados, numero_cnae))
empresas.close()
