<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../private/css/main.css">
    <title>my passwd</title>
</head>
<body>
    <header>
                <a href="index.html">
                        <img src="../Assets/icone.png" alt="Logo">
                </a>
                <p>Protégeons nos mot de passe du crous</p>
        </header>
        <div>
            <?php
                require_once("../private/php/fonctions.php");
                $token = $_GET['token'];
                getTextBD($token);
                
            ?>
        </div>
        <footer>
        </footer>
</body>
</html>