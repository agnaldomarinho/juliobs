<?php
/*
   =============================================================
              Gerador de Curriculum Vitae
    Autor:  Julio Batista Silva
            Baseado no template de Jonathan Doe
    Data: 05-11-2009
   =============================================================
*/

// =============================================================
//               Define Variáveis
// =============================================================

    // 1 - Dados Pessoais
    $nome           =   $_POST['nome'];
    $sexo           =   $_POST['sexo'];
    $nascimento     =   $_POST['nascimento'];
    $est_civil      =   $_POST['est_civil'];
    $filhos         =   $_POST['filhos'];
    $naturalidade   =   $_POST['naturalidade'];
    $rua            =   $_POST['rua'];
    $numero         =   $_POST['numero'];
    $complemento    =   $_POST['complemento'];
    $bairro         =   $_POST['bairro'];
    $cidade         =   $_POST['cidade'];
    $estado         =   $_POST['estado'];
    $cep            =   $_POST['cep'];
    $pais           =   $_POST['pais'];
    $tel_ddd        =   $_POST['tel_ddd'];
    $telefone       =   $_POST['telefone'];
    $cel_ddd        =   $_POST['cel_ddd'];
    $celular        =   $_POST['celular'];
    $email          =   $_POST['email'];
    $lattes         =   $_POST['lattes'];

    // 2 - Objetivo Profissional
    $objetivos      =   $_POST['objetivos'];

    // 3 - Formação Acadêmica
    $escolaridade     =   $_POST['escolaridade'];
      
    $escola_em        =   $_POST['escola_em'];
    $ano_em           =   $_POST['ano_em'];
     
    $ies_gradua       =   $_POST['ies_gradua'];
    $ano_gradua       =   $_POST['ano_gradua'];
    $curso_gradua     =   $_POST['curso_gradua'];
    
    $ies_mestrado     =   $_POST['ies_mestrado'];
    $titulo_mestrado  =   $_POST['titulo_mestrado'];
    $area_mestrado    =   $_POST['area_mestrado'];
    $espec_mestrado   =   $_POST['espec_mestrado'];
    $ano_mestrado     =   $_POST['ano_mestrado'];
   
    $ies_doutorado    =   $_POST['ies_doutorado'];
    $titulo_doutorado =   $_POST['titulo_doutorado'];
    $area_doutorado   =   $_POST['area_doutorado'];
    $espec_doutorado  =   $_POST['espec_doutorado'];
    $ano_doutorado    =   $_POST['ano_doutorado'];
  
    $especializaco    =   $_POST['especializacao'];

    // 4 - Complementos
    $complementos     =   $_POST['complementos'];

    // 5 - Atividades Didáticas
    $ativ_didaticas   =   $_POST['ativ_didaticas'];

    // 6 - Atividades Científicas
    $ativ_cientificas = $_POST['ativ_cientificas'];

    // 7 - Experiência Profissional
    $exp1_empresa   =   $_POST['exp1_empresa'];
    $exp1_funcao    =   $_POST['exp1_funcao'];
    $exp1_detalhes  =   $_POST['exp1_detalhes'];
    $exp1_entrada   =   $_POST['exp1_entrada'];
    $exp1_saida     =   $_POST['exp1_saida'];

    $exp2_empresa   =   $_POST['exp2_empresa'];
    $exp2_funcao    =   $_POST['exp2_funcao'];
    $exp2_detalhes  =   $_POST['exp2_detalhes'];
    $exp2_entrada   =   $_POST['exp2_entrada'];
    $exp2_saida     =   $_POST['exp2_saida'];

    $exp3_empresa   =   $_POST['exp3_empresa'];
    $exp3_funcao    =   $_POST['exp3_funcao'];
    $exp3_detalhes  =   $_POST['exp3_detalhes'];
    $exp3_entrada   =   $_POST['exp3_entrada'];
    $exp3_saida     =   $_POST['exp3_saida'];

    // 8 - Viagens
    $viagem1        =   $_POST['viagem1'];
    $motivo1        =   $_POST['motivo1'];
    $v1_inicio      =   $_POST['v1_inicio'];
    $v1_fim         =   $_POST['v1_fim'];

    $viagem2        =   $_POST['viagem2'];
    $motivo2        =   $_POST['motivo2'];
    $v2_inicio      =   $_POST['v2_inicio'];
    $v2_fim         =   $_POST['v2_fim'];

    $viagem3        =   $_POST['viagem3'];
    $motivo3        =   $_POST['motivo3'];
    $v3_inicio      =   $_POST['v3_inicio'];
    $v3_fim         =   $_POST['v3_fim'];

    // 9 - Outras Atividades
    $outras_ativ    =   $_POST['outras_ativ'];

    // 10 - Data

    $formato_data   =   $_POST['formato_data'];

    // Modo 1: 06/11/2009
    $data           =   date("d/m/Y");

    // Modo 2: Sexta-feira, 06 de Novembro de 2009
    $mes["01"] = "Janeiro";
    $mes["02"] = "Fevereiro";
    $mes["03"] = "Março";
    $mes["04"] = "Abril";
    $mes["05"] = "Maio";
    $mes["06"] = "Junho";
    $mes["07"] = "Julho";
    $mes["08"] = "Agosto";
    $mes["09"] = "Setembro";
    $mes["10"] = "Outubro";
    $mes["11"] = "Novembro";
    $mes["12"] = "Dezembro";

    $diasemana["0"] = "Domingo";
    $diasemana["1"] = "Segunda-feira";
    $diasemana["2"] = "Terça-feira";
    $diasemana["3"] = "Quarta-feira";
    $diasemana["4"] = "Quinta-feira";
    $diasemana["5"] = "Sexta-feira";
    $diasemana["6"] = "Sábado";

    $dia = date('d');
    $diasemanan = date('w');
    $mesn = date('m');
    $ano = date('Y');

    // Cursando?
    
        // Graduação -> graduando(a) ou graduado(a) 
        if ($ano_gradua < $ano)
            $graduado = $sexo=="o"?"Graduado":"Graduada";
        else
            $graduado = $sexo=="o"?"Graduando":"Graduanda";

        // Mestrado -> Mestre(a) - Mestando(a)
        if ($ano_mestrado < $ano)
            $mestre = $sexo=="o"?"Mestre":"Mestra";
        else
            $mestre = $sexo=="o"?"Mestrando":"Mestranda";

        // Doutorado -> Doutor(a) - Doutorando(a)
        if ($ano_doutorado < $ano)
            $doutor = $sexo=="o"?"Doutor":"Doutora";
        else
            $doutor = $sexo=="o"?"Doutorando":"Doutoranda";

    // 11 - Idade
    function Idade( $data_nasc )
    {
        $data_nasc = explode("/", $data_nasc);

        $data = date("d/m/Y");
        $data = explode("/", $data);
        $anos = $data[2] - $data_nasc[2];
        
        if ( $data_nasc[1] >= $data[1] )
        {
            if ( $data_nasc[0] <= $data[0] )
            {
                return $anos;
            }
            else
            {
                return $anos-1;
            }
        }
        else
        {
            return $anos;
        }
    } 
    
// =============================================================
//               Imprime na tela
// =============================================================
?>

<html>
<head>

<title><?php echo $nome; ?></title>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />

    <link rel="stylesheet" type="text/css" href="curriculum_print.css" media="print" />
    <link rel="stylesheet" type="text/css" href="curriculum.css" media="screen" />

</head>
<body>

    <div id="pagina">
    
        <div id="cabecalho">
        <?php echo "
                <h1>$nome</h1>
            <div class=\"esquerda\">
                <h2>$naturalidade, $est_civil$sexo, ". Idade($nascimento) ." anos</h2>
                <h2>$rua, $numero</h2>
                <h2>$bairro, $cidade, $estado - $pais</h2>
                <h2>CEP: $cep</h2>
            </div>

            <div class=\"direita\">
                <h2>Telefone: ($tel_ddd) $telefone</h2>
                <h2>Email: $email</h2>
                <h2>Lattes: $lattes</h2>
            </div>
        "; ?>
        </div> <!-- Cabeçalho -->

<!-- Objetivo -->
<?php
    if($objetivos)
    {
        echo "
            <div class=\"categoria\">
                <h2>Objetivo</h2>
                    <pre>$objetivos</pre>
            </div>
        ";
    }
?>
<!-- Objetivo END -->
            
<!-- Formação -->
        <div class="categoria">
            <h2>Formação</h2>
            <ul> 
                <div class="formacao">
                    <li>Terminou o ensino médio no <?php echo "$escola_em, conlusão em $ano_em."; ?></li>
                </div>

            <?php
                if ($ies_gradua)
                {
                    // Verifica se ies_gradua  é a última
                    echo $ies_mestrado?"<div class=\"formacao\">":"<div class=\"formacao fim\">";

                    echo "
                            <li>$graduado em $curso_gradua. $ies_gradua, conclusão em $ano_gradua.</li>
                        </div>
                    ";
                }
                
                if ($ies_mestrado)
                {
                    // Verifica se ies_gradua  é a última
                    echo $ies_doutorado?"<div class=\"formacao\">":"<div class=\"formacao fim\">";

                    echo "
                            <li>$mestre em $espec_mestrado. $ies_mestrado, conclusão em $ano_mestrado.</li>
                        </div>
                    ";
                }

                if ($ies_doutorado)
                {
                    echo "
                        <div class=\"formacao fim\">
                            <li>$doutor em $espec_doutorado. $ies_doutorado, conclusão em $ano_doutorado.</li>
                        </div>
                    ";
                }
            ?>
            </ul>
        </div>
<!-- Formaçao END-->

<!-- Complementos -->
<?php
        if($complementos)
        {
            echo "
                <div class=\"categoria\">
                    <h2>Complementos</h2>
                    <pre>$complementos</pre>
                </div>
            ";
        }
?>
<!-- Complementos END -->

<!-- Atividades Científicas -->
<?php
        if($ativ_cientificas)
        {
            echo "
                <div class=\"categoria\">
                    <h2>Atividades Científicas</h2>
                    <pre>$ativ_cientificas</pre>
                </div>
                ";
        }
?>
<!-- Atividades Científicas END -->

<!-- Atividades Didáticas -->
<?php
        if($ativ_didaticas)
        {
            echo "
                <div class=\"categoria\">
                    <h2>Atividades Didáticas</h2>
                    <pre>$ativ_didaticas</pre>
                </div>
                ";
        }
?>
<!-- Atividades Didáticas END -->

<!-- Experiência Profissional -->
<?php
        if($exp1_funcao)
        {
            echo "
                <div class=\"categoria\">
                    <h2>Experiência Profissional</h2>
                ";

                // Verifica se exp1 é a última
                echo $exp2_funcao?"<div class=\"experiencia\">":"<div class=\"experiencia fim\">";

                echo "
                        <h3>$exp1_empresa</h3>
                        <h4>Função: $exp1_funcao</h4>
                        <h4>$exp1_detalhes</h4>
                        <h5>$exp1_entrada-$exp1_saida</h5>
                    </div>
            ";
        
                
            if($exp2_funcao)
            {
                // Verifica se exp2 é a última
                echo $exp3_funcao?"<div class=\"experiencia\">":"<div class=\"experiencia fim\">";

                echo "
                        <h3>$exp2_empresa</h3>
                        <h4>Função: $exp2_funcao</h4>
                        <h4>$exp2_detalhes</h4>
                        <h5>$exp2_entrada-$exp2_saida</h5>
                    </div>
                ";
            }
                    
            if($exp3_funcao)
            {
                echo "
                    <div class=\"experiencia fim\">
                        <h3>$exp3_empresa</h3>
                        <h4>Função: $exp3_funcao</h4>
                        <h4>$exp3_detalhes</h4>
                        <h5>$exp3_entrada-$exp3_saida</h5>
                    </div>
                ";
            }
                echo "</div>"; // Categoria Exp. Profissional
        }
?>

<!-- Experiência Profissional END -->

<!-- Viagens -->
<?php
        if($viagem1)
        {
            echo "
                <div class=\"categoria\">
                    <h2>Viagens</h2>
                ";

                // Verifica se viagem1 é a última
                echo $viagem2?"<div class=\"viagem\">":"<div class=\"viagem fim\">";

                echo "
                    <h3>$viagem1</h3>
                        <h4>Motivo: $motivo1</h4>
                        <h5>$v1_inicio - $v1_fim</h5>
                    </div>
                ";
                
            if($viagem2)
            {
                // Verifica se viagem2 é o último
                echo $viagem3?"<div class=\"viagem\">":"<div class=\"viagem fim\">";

                    echo "
                        <h3>$viagem2</h3>
                        <h4>Motivo: $motivo2</h4>
                        <h5>$v2_inicio - $v2_fim</h5>
                    </div>
                ";
            }

            if($viagem3)
            {
                echo "
                    <div class=\"viagem fim\">
                        <h3>$viagem3</h3>
                        <h4>Motivo: $motivo3</h4>
                        <h5>$v3_inicio - $v3_fim</h5>
                    </div>
                ";
            }
                echo "</div>"; // Categoria Viagens
        }
?>
<!-- Viagens END -->

<!-- Outras Atividades -->
<?php
        if($outras_ativ)
        {
            echo "
                <div class=\"categoria fim\">
                    <h2>Outras Atividades</h2>
                    <pre>$outras_ativ</pre>
                </div>
                ";
        }
?>
<!-- Outras Atividades END -->

<!-- Rodapé -->
<div id="rodape">
<?php
        if($formato_data)
            echo "<p>Atualizado $data</p>";
        else
            echo "<p>Atualizado $diasemana[$diasemanan], $dia de $mes[$mesn] de $ano</p>";
?>
</div>
<!-- Rodapé END -->

    </div> <!-- pagina -->

</body>
</html>
