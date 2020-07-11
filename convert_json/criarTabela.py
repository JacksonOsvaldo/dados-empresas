from convert_json import db


def cadastral():
    try:

        db.c.execute(
            "CREATE TABLE cadastral(CPF TEXT, nomePrimeiro TEXT, nomeMeio TEXT, nomeUltimo TEXT, nomeParentesco TEXT, sexo TEXT, dataNascimento TEXT, statusReceitaFederal TEXT, rgNumero TEXT, rgOrgaoEmissor TEXT, rgUf TEXT, tituloEleitoral TEXT, obito TEXT, nacionalidade TEXT, menorDeIdade TEXT, pep TEXT, estadoCivil TEXT, maeCPF TEXT, maeNomePrimeiro TEXT, maeNomeMeio TEXT, maeNomeUltimo TEXT, maeNomeParentesco TEXT, escolaridade TEXT, cns TEXT)"
        )

        # c.execute(
        #     "CREATE UNIQUE INDEX idx_nome_socio ON dados_socios (nome_socio);"
        # )
    except:
        print('\nOcorreu um erro ao criar a tabela. Verfique se já não está criada.')
