SELECT *

from cnaes_secundarios left join empresas

where cnaes_secundarios.cnpj = empresas.cnpj and cnaes_secundarios.cnae = "{}"
