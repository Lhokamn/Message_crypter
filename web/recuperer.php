<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../private/css/main.css">
    <link rel="icon" type="image/png" sizes="16x16" href="Assets/icone.png">
    <title>my passwd</title>
</head>
<body>
    <header>
                <a href="index.html">
                        <img src="../Assets/icone.png" alt="Logo">
                </a>
                <p><strong>Protégeons nos mot de passe</strong></p>
        </header>
        <div>
            <p>Votre texte caché est le suivant</p>
            <textarea>
                <?php

                    // On test de mettre en place une sécurité pour vérifier que le lien est bien lu dan sun navigateur
                    // On récupère l'agent de la requête HTTP
                    $userAgent = $_SERVER['HTTP_USER_AGENT'];


                    // Liste de navigateurs possibles
                    $knownBrowsers = array(
                        'Firefox',
                        'Chrome',
                        'Edge',
                        'Safari',
                        'Opera',
                        'MSIE', // Internet Explorer
                        'Brave',
                        'Vivaldi',
                        'Yandex',
                        'Samsung',
                        'UC Browser',
                        'Maxthon',
                        'Mozilla',
                        'Midori',
                        'Pale Moon',
                        'Tor Browser'
                    );

                    // Vérifier si le User-Agent contient l'un des navigateurs connus
                    $detectedBrowser = 'Autre navigateur';
                    foreach ($knownBrowsers as $browser) {
                        if (strpos($userAgent, $browser) !== false) {
                            require_once("../private/php/fonctions.php");
                            $token = $_GET['token'];
                            $text = getTextBD($token);
                            echo $text; 
                            break;
                        }
                    }
                    
                ?>
            </textarea>
        </div>
        <footer>
        </footer>
</body>
</html>