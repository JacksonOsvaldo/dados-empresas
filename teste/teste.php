<?php
  // $dir = 'sqlite:/var/www/html/con/banco.db';
  $str = str_replace("/", "", "S/A");

  echo $str;
  die;
  
  class MyDB extends SQLite3
  {
      function __construct()
      {
          $this->open('./data/CNPJ_full.db');
      }
  }

  $db = new MyDB();

  $nome_socio = "TEste 02";

  $db->query('INSERT INTO dados_socios(nome_socio) VALUES ("'.$nome_socio.'")');

  $result = $db->query('SELECT nome_socio from dados_socios where nome_socio = "'.$nome_socio.'" limit 1');
  $number_of_rows = 0;//for now
  while($row = $result->fetchArray()) {
        $number_of_rows += 1;

    }
    echo "Number of rows: $number_of_rows";

  
  // print_r($result->fetchArray());
  $results = [];
  while ($row = $result->fetchArray()) {
    $results[] = array(
      'nome_socio' => $row['nome_socio'],
    //   'email' => $row['email'],
    );
  }

  $jsonResult = json_encode($results);
  $fp = fopen('results.json', 'w');
  fwrite($fp, $jsonResult);
  fclose($fp);
?>