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

Depois de instalado o aria2, vamos fazer download de todo dataset. Para isso, vamos executar o seguinte comando:

```
bash download_dados.sh
```

Os arquivos serão armazenados no diretório *data/download*. Esse processo pode levar de 3 à mais horas. Por isso estamos utilizando o *aria2*. Caso ocorra algum erro durante o download, o gerenciador vai retomar o download do ponto onde parou.


### Decodificando os arquivos/dataset

Depois de feito todo download, precisamos decodificar nossa base de dados. Para isso, vamos utilizar um script feito em Python. Mas, antes de executarmos esse script, Precisamos configurar nosso ambiente.


#### Configurando o ambiente

Fazendo download do Python3.8

```
sudo apt-get install python3.8
```

Para executarmos esse projeto, vamos seguir as recomendações da comunidade Python no que diz respeito ao isolamento dos nossos ambientes. Então, vamos criar nossa virtualenv.

```
virtualenv -p python3.8 env
```

Depois de criada, precisamos ativar nosso ambiente:

```
source env/bin/activate
```

Depois de ativado nosso ambiente, vamos instalar as bibliotecas que usaremos.

```
pip install -U pip
pip install -r requirements.txt
```

### Decodificando nossos arquivos 


Para decodificar nosso dataset, vamos executar o seguinte comando:

```
python convert_cnpj.py data/download/ sqlite data/output/ --dir
```

Lembrando que essa execução deve ser feita com o ambiente ativado e com todas as dependências ativadas.

Será gerado um arquivo *.db* no diretório *data/output/* para posterior análise no sqlite3.
