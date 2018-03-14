<?php 

  $client = new SoapClient(NULL,
        array(
        "location" => "http://localhost:8080/",
        "uri"      => "lojao",
        "style"    => SOAP_RPC,
        "use"      => SOAP_ENCODED
        ));
    $a = new SoapParam($_GET["num_pedido"],"num_pedido");
    echo $client->Pesquisar($a);

?>


