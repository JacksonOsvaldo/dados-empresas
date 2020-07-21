<?php

	$filename = "../lista_socios_vazios.csv";
	$handle = fopen($filename, "r");
	$contents = fread($handle, filesize($filename));

    $dados = explode(",\n", $contents);
    // print_r($dados);


	foreach($dados as $key => $val) {

        $dado = explode(",", $val);
        $cnpj = $dado[0];
        $nome = $dado[1];
        // print_r($dado);
        // die;

		$nome_json = "$cnpj-$nome.json";

		if (@fopen("socios_json/$nome_json", 'r')){
			echo "Ja existe $nome_json\n";
			continue;
		}
		// echo $val.' - ';
		$curl = curl_init('https://targetdatasmart.com/api/PF/NOME');

		curl_setopt($curl, CURLOPT_HEADER, false);
		curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
		curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($curl, CURLOPT_POST, true);
		curl_setopt($curl, CURLOPT_HTTPHEADER, array(
			"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjRjYzhhMzlhOGJmMTYzZTdiMDcwOWQ4MDJjOWVhNTIwNjJmOGJiN2NmODFmODQ5NGRiYjgwZGU3ZDdjOWU1NjM5NzllMzExMDg4MmVlNWZmIn0.eyJhdWQiOiIyIiwianRpIjoiNGNjOGEzOWE4YmYxNjNlN2IwNzA5ZDgwMmM5ZWE1MjA2MmY4YmI3Y2Y4MWY4NDk0ZGJiODBkZTdkN2M5ZTU2Mzk3OWUzMTEwODgyZWU1ZmYiLCJpYXQiOjE1NzA3OTAwNzYsIm5iZiI6MTU3MDc5MDA3NiwiZXhwIjoxODg2NDA5Mjc2LCJzdWIiOiI4Iiwic2NvcGVzIjpbXX0.o6fdYDYg7A8rMOaj6YljC3EISII7MtRE6rViSQdYMA_eTPqR6xIuD3bDJJ3sLPjq40oItq04O5dIjf8GHipy31olXJw2e-PispV2qiov9HiNmuZOqhFB66mDs0UXUFerGX755-vnzzDxGaoDxF7ak-2TcfsGueT_latYTp8RNFyV1ncUFWK_6i9VPSDA2LLDoAYXPXcVYycgP50-wWe32AZkxf5IhrrFv9wRL245jJXmYW4VWAE-H5wMCgsuMl-RvBTndUlxzEg-8anwsTU7nLDkjsKZsrepHyEfROrKWD3Lu9rYehfqsaaOrMWH7r93r_5Bdmk9kF0ejqG-C6S89cZEr7utLRdHCBc69HfhrmJXVvzhhnJJsfZ172jePSd5-dj0eAxjd6fim-hpnPgjaD_m2gjdTWMxYbltr7hANA-j4YdoNwEBEQ9TLCCT7XUFKB630GnTGC0ZUV5UDDdDp9LdrvhcD0U613E1X7QasEeKTRB419XYhUmegrOPdRaFbWPQ0q8o-kJVTtkAgWqHQAybjl0iHsPG5LgFAf_5eys_8kt5n21pYI5NYAcK7X9pgjFC6e3GlAK3tDMrGf3lBWy2p9k9dUZZM3dOKtmJLHBOWokMjykDAKepTdSxglPrKTb30r51YTz0sLTzdmq5ajlRYEVPl-duCnI7n82E6Dw",
			"Content-Type: application/json",
			"Accept: application/json"
		  ));
		curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode([$nome]));
		
		$fp = fopen("socios_json/$nome_json", 'w');
	
		$json_response = curl_exec($curl);
		curl_close($curl);
		
		$resposta = json_decode($json_response, true);
	
		fwrite($fp, $json_response);
		fclose($fp);
	}

	fclose($handle);
	
	die;
	
	
	print($json_response);
	
?>
