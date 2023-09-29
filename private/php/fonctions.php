<?php
require_once('config.php');

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

function encryptString($data, $password) {
    $key = openssl_digest($password, 'sha256', true);
    $iv = openssl_random_pseudo_bytes(16);
    $cipherText = openssl_encrypt($data, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);
    return base64_encode($iv . $cipherText);
}

function decryptString($data, $password) {
    $key = openssl_digest($password, 'sha256', true);
    $data = base64_decode($data);
    $iv = substr($data, 0, 16);
    $cipherText = substr($data, 16);
    $plainText = openssl_decrypt($cipherText, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);
    return $plainText;
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
    $encryptText = encryptString($text,privatepw);
    do {
        $link = createRandomLink();
        try{
            $mysql=connect();
	        $q="INSERT INTO Links VALUES (NUll,'$link', '$encryptText',0)";
	        $req=$mysql->prepare($q);
	        $req->execute();
            $succes = true;
        }catch(Exception $e){
            die($e->getMessage());
        }
    } while (!$succes);
    
    return $link;
}

function getFullLink($link){

    // Préparation de la génération du lien
    $dns=DNS;
    $startLink = "$dns/web/recuperer.php?token=";

    $mysql=connect();
    $q="SELECT * FROM Links WHERE Lien = '$link'";
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
    $isUses = $data[0]['usesLink'];
    if($isUses == true){
        echo "Le lien a déjà été utilisés.";
    }
    else{

        $textChiffre = $data[0]['texte'];
        #echo $textChiffre;
        $textDecrypt = decryptString($textChiffre,privatepw);
        echo $textDecrypt;

        // On modifie la base de donnée afin de supprimer le message, et on met le booleen à true
        $mysql=connect();
        $q="UPDATE Links SET texte = '', usesLink = 1  WHERE lien = '$token'";
        $req=$mysql->prepare($q);
        $req->execute();

    }
}



?>
