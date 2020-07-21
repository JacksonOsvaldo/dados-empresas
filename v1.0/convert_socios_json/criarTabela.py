# -*- coding: utf-8 -*-


# import db
from convert_socios_json import db

# Criando a tabela de cadastro


def cadastral():
    try:

        db.c.execute(
            """
            CREATE TABLE pf_cadastral(CPF TEXT, nomePrimeiro TEXT, nomeMeio TEXT, nomeUltimo TEXT, nomeParentesco TEXT, sexo TEXT, dataNascimento TEXT, statusReceitaFederal TEXT, rgNumero TEXT, rgOrgaoEmissor TEXT, rgUf TEXT, tituloEleitoral TEXT, obito TEXT, nacionalidade TEXT, menorDeIdade TEXT, pep TEXT, estadoCivil TEXT, maeCPF TEXT, maeNomePrimeiro TEXT, maeNomeMeio TEXT, maeNomeUltimo TEXT, maeNomeParentesco TEXT, escolaridade TEXT, cns TEXT);
            """
        )

        db.c.execute(
            "CREATE INDEX idx_pf_cadastral_CPF ON pf_cadastral (CPF);"
        )

    except:
        print('\nOcorreu um erro ao criar a tabela pf_cadastral. Verfique se já não está criada.')

# Criando tabela das pessoas que beneficiarioProgramaSocial


def beneficiarioProgramaSocial():
    try:

        db.c.execute(
            "CREATE TABLE pf_beneficiarioProgramaSocial(CPF TEXT, bolsaFamilia TEXT)"
        )

        db.c.execute(
            "CREATE INDEX idx_pf_beneficiarioProgramaSocial_CPF ON pf_beneficiarioProgramaSocial(CPF);"
        )

    except:
        print('\nOcorreu um erro ao criar a tabela pf_beneficiarioProgramaSocial. Verfique se já não está criada.')

# Criando a tabela de endereço do objeto contato


def contato_endereco():

    try:

        db.c.execute(
            "CREATE TABLE pf_contato_endereco(CPF TEXT, tipoLogradouro TEXT, logradouro TEXT, numero TEXT, complemento TEXT, bairro TEXT, cidade TEXT, uf TEXT, cep TEXT, ordem TEXT)"
        )

        db.c.execute(
            "CREATE INDEX idx_pf_endereco_CPF ON pf_contato_endereco(CPF);"
        )

    except:
        print('\nOcorreu um erro ao criar a tabela pf_contato_endereco. Verfique se já não está criada.')

# Criando a tabela de email do objeto contato


def contato_email():
    try:

        db.c.execute(
            "CREATE TABLE pf_contato_email(CPF TEXT, email TEXT, ordem TEXT)"
        )

        db.c.execute(
            "CREATE INDEX idx_pf_email_CPF ON pf_contato_email(CPF);"
        )

    except:
        print('\nOcorreu um erro ao criar a tabela pf_contato_email. Verfique se já não está criada.')


def contato_telefones():
    try:

        db.c.execute(
            "CREATE TABLE pf_contato_telefones(CPF TEXT, ddd TEXT, numero TEXT, operadora TEXT, procon TEXT, whatsapp TEXT, tipoTelefone TEXT, ordem TEXT)"
        )

        db.c.execute(
            "CREATE INDEX idx_pf_telefones_CPF ON pf_contato_telefones(CPF);"
        )

    except:
        print(
            '\nOcorreu um erro ao criar a tabela telefones. Verfique se já não está criada.')
