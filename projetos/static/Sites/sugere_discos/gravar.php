<?php
    // Coleta dados do formulario
    $nome       = $_POST["nome"]; 
    $genero     = $_POST["genero"]; 
    $artista    = $_POST["artista"]; 
    $titulo     = $_POST["titulo"]; 
    $formato    = $_POST["formato"]; 
    $bitrate    = $_POST["bitrate"]; 
    $ano        = $_POST["ano"]; 
    $info       = $_POST["info"]; 

    // Formata conteudo 
    $conteudo = "Nome: $nome\n\tGenero: $genero\n\tArtista: $artista\n\tTitulo: $titulo\n\tFormato: $formato\n\tBitrate: $bitrate\n\tAno: $ano\n\tInfo: $info\n\n---------------------\n\n"; 

    // Nome do arquivo 
    $arquivo = "discos.txt"; 

    // Tenta abrir o arquivo 
    if (!$abrir = fopen($arquivo, "a"))
    { 
        echo "Erro abrindo arquivo ($arquivo)"; 
        exit; 
    } 

    // Escreve no arquivo 
    if (!fwrite($abrir, $conteudo))
    { 
        print "Erro ao escrever no arquivo ($arquivo)"; 
        exit; 
    }
    
    // Fecha o arquivo  
    fclose($abrir);  

    // Espera 3s e Redireciona
    echo 'Sugestao gravada com Sucesso!';
    echo '<meta http-equiv="refresh" content="3;url=discos.txt"/>';

?>
