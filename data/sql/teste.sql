SELECT *

from cnaes_secundarios left join empresas

where cnaes_secundarios.cnpj = empresas.cnpj and cnaes_secundarios.cnae = "6612605"

--limit 10