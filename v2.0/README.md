## Descrição do Projeto

Script para geração de relatórios com base em FIND/QUERY feitas em DB do MongoDB.

O objetivo é inserir um CNAE e, com base na cidade/estadO, retornar os valores correspondentes exportando-os para CSV.


A planilha precisa ter os seguintes campos:

- CNPJ,
- RAZÃO SOCIAL,
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
pip install requirements.txt
```

Rodando projeto para geração dos relatórios:

```
python report.py
```