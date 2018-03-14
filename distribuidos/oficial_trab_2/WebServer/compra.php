<?php 
  $n=1;
  include "conexao.inc";
  $res = mysqli_query($con, "SELECT * FROM Produtos");
  while($list = mysqli_fetch_array($res)){
  	if($_GET["qnt_".$n] > 0){
      $nomes[] = $list['nome'];
      $quantidades[] = $_GET["qnt_".$n];
    }
    $n++;
  }
  $client = new SoapClient(NULL,
            array(
            "location" => "http://192.168.1.104:8080/",
            "uri"      => "lojao",
            "style"    => SOAP_RPC,
            "use"      => SOAP_ENCODED
            ));
  $a = new SoapParam($nomes,"produto");
  $b = new SoapParam($quantidades,"quantidade");
  $num_pedido =  $client->Comprar($a,$b);
  echo  "<script>alert('Compra efetuada!Número de Pedido:".$num_pedido."');</script>";

 
?>


