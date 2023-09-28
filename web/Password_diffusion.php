<!DOCTYPE html>
<html lang="fr">
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
        <div id="content">
                <div id="textACopier" class="wrapper">
                        <textarea rows="6" cols="50">
                        <?php
                                require_once("../private/php/fonctions.php");
                                getNewLink();
                        ?> 
                        </textarea>
                        <button id="boutonCopier">Copier</button>
                        <script src="../private/js/functions.js"></script>
                </div> 
        </div>
        <footer>
        </footer>
</body>
</html>