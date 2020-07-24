## Descrição do Projeto

Script para geração de relatórios com base em FIND/QUERY feitas em DB do MongoDB.

O objetivo é inserir um CNAE e, com base na cidade/estadO, retornar os valores correspondentes exportando-os para CSV.


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

### Executando

Configurando o ambiente:

```
virtualenv -p python3.8 env
source env/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Antes de executar o script *report.py*, certifique-se de mudar o URI do banco de dados.

Mude apenas o URI de:

```
client = MongoClient(URI)
```

Depois de feito isso, é só executar o script.

```
python report.py
```

Uma coisa importante de se comentar é que o cnae inserido deve ser no formato numérico, sem áspas. Assim, o nome da cidade deve ser inserido no formato string, sem áspas. Além disso, o nome da cidade deve ser inserido em caixa alta e sem caractéres especiais.