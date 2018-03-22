<?php
	include "conexao.inc";
	$nome = $_GET['nome'];
	$preco = $_GET['preco'];
	$sql = "INSERT INTO Produtos VALUES";
	$sql .= "('$nome','$preco')";
	if($con ->query($sql) === True){
		header('Location: criar.html');
	}else{
		echo 'Erro!';
	}
	$con->close();
?>
