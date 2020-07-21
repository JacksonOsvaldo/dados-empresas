<?php

	$filename = "../lista_socios_vazios.csv";
	$handle = fopen($filename, "r");
	$contents = fread($handle, filesize($filename));

    $dados = explode(",\n", $contents);
    // print_r($dados);

    $i = 0;
    $nomes = array();
    $nomes_file = array();
	foreach($dados as $key => $val) {
        $dado = explode(",", $val);
        $cnpj = $dado[0];
        $nome = $dado[1];

		$nome_file = "$nome";

		if (file_exists("socios_json/$nome_file.json")){
			$zip = new ZipArchive();
			$filename = "socios_json/$nome_file.zip";

			echo "$filename\n";

			if ($zip->open($filename, ZipArchive::CREATE)!==TRUE) {
			    exit("cannot open <$filename>\n");
			}
			echo "socios_json/$nome_file.json\n";
			$zip->addFile("socios_json/$nome_file.json");
			echo "numfiles: " . $zip->numFiles . "\n";
			echo "status:" . $zip->status . "\n";
			$zip->close();

			unlink("socios_json/$nome_file.json");
			continue;
		}

		if (file_exists("socios_json/$nome_file.zip")){
			// echo "Ja existe $nome_json\n";
			continue;
		}

        array_push($nomes_file, $nome_file);

        // $payload = "Jose Roberto de Oliveira";
        // $payload = "\"$dado[1]\",\"Jose Roberto de Oliveira\"";
        // $payload = ["IVANDRE MONTIEL DA SILVA","Jose Roberto de Oliveira"';
        // $payload = ["Pedro Sousa Mendes"];
        // $payload = [$dado[1],'Anna Karolyne de Goes Menezes'];
        // $payload = array($dado[1]);
        array_push($nomes, $dado[1]);
        // $payload[] = $dado[1];
        // Anna Karolyne de Goes Menezes,Pedro Sousa Mendes
        // $payload = json_encode([$dado[1],"Jose Roberto de Oliveira"]);
        $payload = json_encode($nomes);
        // echo $payload;
        // die;
        // print_r($dado);
        // die;

        $i++;

		// if ($i > 2){
		// 	die;
		// }
		if ($i < 50){
			continue;
		}

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

		echo "$payload\n";
		// die;

		curl_setopt($curl, CURLOPT_POSTFIELDS, $payload);
	
		$json_response = curl_exec($curl);
		curl_close($curl);
		
		// $resposta = json_decode($json_response, true);
	
		$salvar_json = 1;
		foreach($nomes_file as $key => $val) {
			// echo "$val\n";

			if ($salvar_json) {
				$salvar_nome = $val;
				$fp = fopen("socios_json/$val.json", 'w');
				// $fp = fopen("socios_json/00000000020389-IVANDRE MONTIEL DA SILVA.json", 'w');
				fwrite($fp, $json_response);
				fclose($fp);
				$salvar_json = 0;	
			} else {
				$fp = fopen("socios_json/$val.json", 'w');
				// $fp = fopen("socios_json/00000000020389-IVANDRE MONTIEL DA SILVA.json", 'w');
				fwrite($fp, json_encode($salvar_nome));
				fclose($fp);
				// die;		
			}

			$zip = new ZipArchive();
			$filename = "socios_json/$val.zip";

			// echo "$filename\n";

			if ($zip->open($filename, ZipArchive::CREATE)!==TRUE) {
			    exit("cannot open <$filename>\n");
			}
			// echo "socios_json/$val.json\n";
			$zip->addFile("socios_json/$val.json");
			// echo "numfiles: " . $zip->numFiles . "\n";
			// echo "status:" . $zip->status . "\n";
			$zip->close();

			unlink("socios_json/$val.json");
			
		}

		$i = 0;
		unset ($nomes);
		unset($nomes_file);
	    $nomes = array();
	    $nomes_file = array();
	}

	fclose($handle);
	
	// die;	
	
	print($json_response);
	
?>
