<?php
require_once('pwd.php');

function connect(){
    # Permet de tester la connexion à une base de donnée
    try{
        $mysql = new PDO('mysql:host='.host.';dbname='.bd.';charset=utf8',user,pwd);
    }
    catch(Exception $e){
        die($e->getMessage());
    }
    return $mysql;
}

function createRandomLink(){
    /* Permet de générer un lien pour le partager
    */
    // Liste de tous les caractères possibles
    $caracteres = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

    // Mélange la chaîne de caractères
    $caracteresMelanges = str_shuffle($caracteres);

    // Extrait les 6 premiers caractères mélangés
    $link = substr($caracteresMelanges, 0, 8);

    return $link;
}

function createNewLink($text){
    /* Fait rentrer dans la base de données Lien un lien générer aléatoirement avec en information pour ce lien :
        - Une chaine de 8 caractères -> $link
        - Le text récupérer dans la textBox -> $text
        - Un sel pour augmenter la sécurité
        - booleen pour savoir si le lien a déjà été ouvert où non

        Le lien fait 8 caractères. En prenant l'alphabet minuscules, majuscules et les chiffres, nous avons 62 possibilités
        ce qui fait un total de lien possible à 218 340 105 584 896
    */
    $succes = false;
    $salt = "12345678"; // a changer pour être unique
    
    // PASSWORD_DEFAULT est l'algorithme de hachage basé sur bcrypt
    $hashText = openssl_encrypt($text,'aes-256-cbc',$salt);
    do {
        $link = createRandomLink();
        try{
            $mysql=connect();
	        $q="INSERT INTO Links VALUES (NUll,'$link', '$hashText','$salt',0)";
	        $req=$mysql->prepare($q);
	        $req->execute();
            $succes = true;
        }catch(Exception $e){
            die($e->getMessage());
        }
    } while (!$succes);
    
	
}

function getNewLink(){

    $dns=DNS;
    $startLink = "https://$dns/send_passwd/web/recuperer.php?token=";
    $mysql=connect();
    $q='SELECT * FROM Links ORDER BY id DESC LIMIT 1';
    $req=$mysql->prepare($q);
    $req->execute();
    $data=$req->fetchAll();
    $token=$data[0]['lien'];

    echo "$startLink$token";
    
}

function getTextBD($token){
    /* Permet de récupérer le text stocké dans la BD à partir de l'url
        Doit mettre le booleen à vrai
        Doit mettre le mot de passe à blanc pour augmenter la sécurité
    */

    // Connexion à la base de donnée
    $mysql=connect();
    $q="SELECT * FROM Links WHERE lien = '$token'";
    $req=$mysql->prepare($q);
    $req->execute();
    $data=$req->fetchAll();
    
    // Si la BD ne trouve aucune correspondance, alors on affiche que le lien n'existe pas
    if (empty($data)){
        header('location:../../web/error_404.html');
    }
    $isUses = $data[0]['useslink'];
    if($isUses){
        echo "Le lien a déjà été utilisés.";
    }
    else{

        $textChiffre = $data[0]['texte'];
        $salt = $data[0]['sel'];
        echo "Le text caché est : <br>";
        echo $textChiffre;

        // On modifie la base de donnée afin de supprimer le message, et on met le booleen à true
        $mysql=connect();
        $q="UPDATE Links SET texte = '', usesLink = 1  WHERE lien = '$token'";
        $req=$mysql->prepare($q);
        $req->execute();

    }
}



?>