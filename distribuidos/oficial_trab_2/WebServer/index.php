<?php
	include "conexao.inc";
	$res = mysqli_query($con, "SELECT * FROM Produtos");
	$linhas = mysqli_num_rows($res);

?>
<!doctype html>
<head>
    <title>Lojão</title>
    <link rel="stylesheet" href="css/style.css">
		<script type="text/javascript" src="js/jquery-3.2.1.min.js"></script>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
</head>
<body>
<div id="wrap">
    <div id="top">
    	<h1 style="text-align: center;margin: 2px; font-size: 20px; ">Lojão</h1>
    	<form name="produto" style="text-align: right; margin:2px; " method="get" action="pesquisa.php">
    		<input type="text" name="num_pedido" style="text-align:center"/>
    		<input id="botao" type="submit" name="submit" value="Pesquisar Pedido"  />
    	</form>
    	<a href="criar.html" style="font-size:12px">Criar Produtos</a>
    </div>
    <div id="conteudo">
		<form name="produto" id="produto" method="get" action="compra.php">
			<table id="tabela">
				<tr>
					<th>Produtos</th>
					<th>Preço</th>
					<th>Quantidade</th>
				</tr>
				<?php
					$i=1;
					while($list = mysqli_fetch_array($res)){
						echo ("<tr>");
						echo ("<td>".$list['nome']."</td>");
						echo ("<td>".$list['preco']."</td>");
						echo ('<td><input type="text" name="qnt_'.$i.'" style="text-align: center" value="0" /></td>');
						echo ("</tr>");
						$i++;
					}
				?>
			</table>
			<p>
			<input id="botao" type="submit" name="submit" value="Efetuar Compra"  />
			
		</form>
	</div>
</div>

</body>
