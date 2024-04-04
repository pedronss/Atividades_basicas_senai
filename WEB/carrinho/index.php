<?php
session_start();

$_SESSION['produtos'] = [
    ['id' => 0, 'categoria'=>'perif', 'nome' => 'Teclado', 'desc' => 'Preto, Switch Red', 'preco' => 164.99, 'img' => '../img/teclado.png'],
    ['id' => 1, 'categoria'=>'perif', 'nome' => 'Mouse Teleshop', 'desc' => 'LightSpeed, 1000DPI', 'preco' => 32.99, 'img' => '../img/mouse.png'],
    ['id' => 2, 'categoria'=>'peri', 'nome' => 'Gabinete para Computador', 'desc' => 'Lateral em Vidro Fumê, Preto', 'preco' => 200.00, 'img' => '../img/gabinete-pc.png'],
    ['id' => 3, 'categoria'=>'perif', 'nome' => 'Impressora HP', 'desc' => 'Laser Preta, DCP-2334DR', 'preco' => 420.00, 'img' => '../img/impressora.png'],
    ['id' => 4, 'categoria'=>'hardware', 'nome' => 'Memória Ram', 'desc' => '(1x4GB), DDR4, 2666MHz', 'preco' => 205.85, 'img' => '../img/memoria-ram-notebook.png'],
    ['id' => 5, 'categoria'=>'elec', 'nome' => 'Samsung Book', 'desc' => 'Core  i5 8GB 256GB SSD', 'preco' => 3499.99, 'img' => '../img/notebook.png'],
    ['id' => 6, 'categoria'=>'perif', 'nome' => 'Monitor Mancer', 'desc' => 'HDMI/VGA, 60Hz', 'preco' => 259.99, 'img' => '../img/monitor-pc.png'],
    ['id' => 7, 'categoria'=>'elec', 'nome' => 'Tablet', 'desc' => 'Câmera 8MP e 2MP - Prata', 'preco' => 899.99, 'img' => '../img/tablet.png'],
    ['id' => 8, 'categoria'=>'hardware', 'nome' => 'Placa Mãe', 'desc' => 'DDR4 Socket LGA 1151', 'preco' => 249.99, 'img' => '../img/placa-mae.png'],
    ['id' => 9, 'categoria'=>'elec', 'nome' => 'Smartphone Nokia', 'desc' => '256GB, 8GB RAM - Preto', 'preco' => 1259.90, 'img' => '../img/smartphone.png']
];
    
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bem-vindo!</title>
    <link rel="stylesheet" href="css/stylesheet.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap">
</head>

<body>
    <div class="nav-bar">
        <header>
            <nav class="navbar">
                <a class="nav-logo" href="#"><img src="img/logo.png" alt=""></a>
                <ul class="nav-menu">
                    <li class="nav-item"><input class="nav-input" placeholder="O que você procura?"  type="text"></li>
                </ul>
                <ul class="carrinho">
                    <a href="php/shopkart.php"><li class="nav-item"><img src="img/carrinho.svg" alt=""></a></li>
                </ul>
            </nav>
        </header>
    </div>
    <div class="container">
        <div class="itens">
            <div class="itens-content">
                <img src="img/teclado.png" alt="">
                <p>Teclado Gamer Soup Rainbow, <br> Preto, Switch Red</p>
                <p id="titulo">R$164.99</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=0"><input type="button" value="ADICIONAR"></a>'; ?>
            </div>
            <div class="itens-content">
                <img src="img/mouse.png" alt="">
                <p>Mouse Logitech G562 <br> LightSpeed, 1000DPI</p>
                <p id="titulo">R$32.99</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=1"><input type="button" value="ADICIONAR"></a>'; ?>
            </div>
            <div class="itens-content">
                <img src="img/gabinete-pc.png" alt="">
                <p>Gabinete Gamer Mid-Tower,<br>Lateral em Vidro Fumê, Preto</p>
                <p id="titulo">R$200,00</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=2"><input type="button" value="ADICIONAR"></a>'; ?>
            </div>
            <div class="itens-content">
                <img src="img/impressora.png" alt="">
                <p>Impressora Soup Multifuncional <br> Laser Preta, DCP-2334DR</p>
                <p id="titulo">R$420,00</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=3"><input type="button" value="ADICIONAR"ae"></a>'; ?>
            </div>
            <div class="itens-content">
                <img src="img/memoria-ram-notebook.png" alt="">
                <p>Memoria Notebook Soup, <br>(1x4GB), DDR4, 2666MHz</p>
                <p id="titulo">R$205,85</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=4"><input type="button" value="ADICIONAR"></a>'; ?>
            </div>
            <div class="itens-content">
                <img src="img/notebook.png" alt="">
                <p>Notebook Soup Aspire 5 Intel <br> Core  i5 8GB 256GB SSD</p>
                <p id="titulo">R$3.423,51</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=5"><input type="button" value="ADICIONAR"></a>'; ?>
            </div>
            <div class="itens-content">
                <img src="img/monitor-pc.png" alt="">
                <p>Monitor VX190Z, 19 Pol, <br> HDMI/VGA, 60Hz</p>
                <p id="titulo">R$259,99</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=6"><input type="button" value="ADICIONAR"></a>'; ?>
            </div>
            <div class="itens-content">
                <img src="img/tablet.png" alt="">
                <p>Tablet Soup M9,64GB, Wi-Fi,<br> Câmera 8MP e 2MP - Prata</p>
                <p id="titulo">R$899,99</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=7"><input type="button" value="ADICIONAR"></a>'; ?>
            </div>
            <div class="itens-content">
                <img src="img/smartphone.png" alt="">
                <p>Smartphone Soup G54 5G <br> 256GB, 8GB RAM - Preto</p>
                <p id="titulo">R$1259,90</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=9"><input type="button" value="ADICIONAR"></a>'; ?>
            </div>
            <div class="itens-content">
                <img src="img/placa-mae.png" alt="">
                <p>Placa Mae Soup H310CM-HG4 <br> DDR4 Socket LGA 1151</p>
                <p id="titulo">R$249,99</p>
                <p id="subtitulo">À vista no pix</p>
                <?php echo '<a href="php/calc.php/?indice=8"><input type="button" value="ADICIONAR"></a>'; ?>
            </div>         
        </div>
</body>

</html>

