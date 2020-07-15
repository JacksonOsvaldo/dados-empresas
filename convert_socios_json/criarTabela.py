from convert_socios_json import db


def cadastral():
    # try:

    db.c.execute(
        """
        CREATE TABLE cadastral(CPF TEXT, nomePrimeiro TEXT, nomeMeio TEXT, nomeUltimo TEXT, nomeParentesco TEXT, sexo TEXT, dataNascimento TEXT, statusReceitaFederal TEXT, rgNumero TEXT, rgOrgaoEmissor TEXT, rgUf TEXT, tituloEleitoral TEXT, obito TEXT, nacionalidade TEXT, menorDeIdade TEXT, pep TEXT, estadoCivil TEXT, maeCPF TEXT, maeNomePrimeiro TEXT, maeNomeMeio TEXT, maeNomeUltimo TEXT, maeNomeParentesco TEXT, escolaridade TEXT, cns TEXT);
        """
    )

    db.c.execute(
        "CREATE INDEX idx_cadastral_CPF ON cadastral (CPF);"
    )

    # except:
    #     print('\nOcorreu um erro ao criar a tabela. Verfique se já não está criada.')


def contato_endereco():

    try:

        db.c.execute(
            "CREATE TABLE contato_endereco(CPF TEXT, tipoLogradouro TEXT, logradouro TEXT, numero TEXT, complemento TEXT, bairro TEXT, cidade,uf,cep,ordem)"
        )

        db.c.execute(
            "CREATE INDEX idx_endereco_CPF ON contato_endereco(CPF);"
        )

    except:
        print('\nOcorreu um erro ao criar a tabela. Verfique se já não está criada.')
