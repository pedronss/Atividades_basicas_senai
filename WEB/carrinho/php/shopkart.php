<?php 
    session_start();

    if(isset($_GET['delete'])){
        unset($_SESSION['carrinho'][$_GET['delete']]);
        header('Location: shopkart.php');
    }
    if(isset($_GET['delete_all'])){
        unset($_SESSION['carrinho']);
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carrinho de compras!</title>
    <link rel="stylesheet" href="../css/kart.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap">
</head>
<body>
    <div class="nav-bar">
        <header>
            <nav class="navbar">
                <a class="nav-logo" href="../index.php"><img src="..//img/logo.png" alt=""></a>
                <ul class="nav-menu">
                </ul>
            </nav>
        </header>
    </div>

    <div class="container">
    <?php if(isset($_SESSION['carrinho'])){?>
        <div class="tabela-carrinho">
            <div class="carrinho">
                <form action="shopkart.php" method="get">
                    <?php 
                    $total_todos = 0;
                    if(isset($_SESSION['carrinho'])){
                        foreach($_SESSION['carrinho'] as $id=>&$items){
                            // Verifica se o parâmetro 'add' está presente na URL e se corresponde ao item atual
                            if(isset($_GET['add']) && $_GET['add'] == $items[0]) {
                                $items[3]++;
                                header("Location: \.\carrinho\php\shopkart.php");
                            }
                            if(isset($_GET['take']) && $_GET['take'] == $items[0] && $items[3]>0) {
                                if ($items[3]>1){
                                    $items[3]--;
                                    header("Location: \.\carrinho\php\shopkart.php");
                                }
                                
                            }

                            echo "<div class='carrinho-item'>";
                            echo "<img src='{$items[5]}' alt=''>";
                            echo "<div class='item-nome'> <p>{$items[1]} <br> {$items[2]} </div> </p>";
                            echo " <p>Quant. <br> <a href='?take={$items[0]}'><img src='../img/sub.png' alt='Subtração'></a>   {$items[3]} <a href='?add={$items[0]}'><img src='../img/add.png' alt='Adição'></a> </p>";
                            $total = $items[4] * $items[3];
                            echo "<p>Preço à vista no PIX: <br>{$total} </p>";
                            echo " <div class='lixeira'>  <a href='?delete={$id}'> <img src='\.\carrinho\img\lixo.png' alt=''> </a> </div>";
                            echo "</div>";
            
                            $total_todos += $total;

                            echo " 
                                  ";
                        }
                    }
                    ?>
                </form>
                <div class="delete">
                    <a href='?delete_all=true'>Apagar</a>
                </div>
            </div>

        </div>
        <div class="resumo">
             <div class="resumo-title">
                <img src="../img/arquivo.png" alt=""><h1>Resumo</h1>
             </div>
            <div class="total">
                    <p>Valor à vista no <strong>pix</strong></p>
                    <h1> <?php echo "R$ ".$total_todos; ?> </h1>
            </div>

            <div class ="botoes">
                <div class="pagar">
                        <a href="?delete_all=true"> <button>Pagar</button></a>
                </div>
                <div class="continuar">
                       <a href="../index.php"><button>Continuar comprando</button></a> 
                </div>
            </div>

        </div>
        <?php }else{?>
                <div class="vazio">
                    <h1>O carrinho está vazio!</h1>
                    <p>Confira nossos produtos na página principal!</p>
                    
                    <a href="\.\carrinho\index.php"><button>CONTINUAR COMPRANDO</button></a>
                </div>
        <?php } if(empty($_SESSION['carrinho'])){
                unset($_SESSION['carrinho']);
                }?>
    </div>
</body>
</html>
