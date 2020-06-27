## Descrição do Projeto

A intenção primeira desse projeto é, de maneira ordenada:

1. Fazer download do dataset de empresas da Receita Federal;
2. Converter esse dataset em um arquivo legível (CSV ou sqlite);
3. Depois de feita sua conversão, iremos gerar uma ou mais views que relacionem e/ou correlacionem todas informações das empresas que encontramos por CNPJ, Sócios, CNAE;

### Detalhes Técnicos

Este projeto utiliza as seguintes tecnologias/ferramentas:

* [Python 3.8.0](https://www.python.org/dev/peps/pep-0569/);
* [aria2](https://aria2.github.io/);
* [sqlite3](https://sqlite.org/index.html);

## Como executar esse projeto?


Podemos dividir o processo de execução desse projeto em três etapas. Na primeira delas, nós precisamos fazer o download da base de dados. Na segunda, precisamos decodificar nossa base de dados. E, na terceira etapa, nós vamos analisar nossa base de dados.

Dito isso, vamos ao que interessa. 

### Instalando gerenciador de downloads aria2

#### Fazendo download do aria2

Vamos fazer o download da versão mais atual do aria2 a partir de seu [repositório](https://github.com/aria2/aria2/releases/tag/release-1.35.0)

```
wget https://github.com/aria2/aria2/releases/download/release-1.35.0/aria2-1.35.0.tar.gz
```

Depois de feito o download, vamos extrair e  acessar sua pasta.

```
tar -vzxf aria2-1.35.0.tar.gz && cd aria2-1.35.0
```

#### Compilando o aria2

Agora, vamos a compilação do aria2. Cetifiquesse de ter todas as libs C++  necessárias para realizarmos o processo de compilação.

Para compilar o código, já dentro do diretório, vamos rodar os seguintes comandos:

```
./configure

make

make install
```

Dependo do caso, você vai precisar executar os comandos *make* como superusuário.

Caso seu ambiente Linux esteja sem alguma das bibliotecas para compilação em C++, execute o seguinte comando:

```
sudo apt-get update


sudo apt-get install build-essential
```

Feito isso, tente reexecutar a compilação.

#### Fazendo download dos arquivos da Receita Federal

Feito o processo de compilação acima, já temos o aria2 instalado e podemos seguir para os próximos passos.



### Decodificando os arquivos/dataset


```
sudo apt-get install python3.8
```

Para executarmos esse projeto, vamos seguir as recomendações da comunidade Python no que diz respeito ao isolamento dos nossos ambientes. Então, vamos criar nossa virtualenv.

```
virtualenv -p python3.8 env
```

Caso não tenha a *virtualenv* instalada, execute o seguinte comando

```
sudo apt-get install virtualenv
```


