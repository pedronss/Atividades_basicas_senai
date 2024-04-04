<?php
    session_start();
    
    $indice = $_GET['indice'];
    $nome = $_SESSION['produtos'][$indice]['nome'];
    $descricao = $_SESSION['produtos'][$indice]['desc'];
    $preco = $_SESSION['produtos'][$indice]['preco'];
    $caminho_img = $_SESSION['produtos'][$indice]['img'];
    $quantidade = 1;

    if (!isset($_SESSION['carrinho'])) {
        $_SESSION['carrinho'] = [];
    }

    $encontrado = false;
    foreach ($_SESSION['carrinho'] as &$item) {
        if ($item[0] == $indice) {
            $item[3]++;
            echo $item[3];
            $encontrado = true;
            break;
        }
    }

    if (!$encontrado) {
        $_SESSION['carrinho'][] = [$indice, $nome, $descricao, $quantidade, $preco, $caminho_img];
        $_SESSION['message'] = "Item adicionado com sucesso!";
    } else {
        echo "Item com ID repetido encontrado. Lidando com a situação...";
    }

    header("Location: \.\carrinho\index.php");

    echo "<pre>";
    print_r($_SESSION['carrinho']);
?>
