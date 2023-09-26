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

    return $link

}

function createNewLink($text){
    /* Fait rentrer dans la base de données Lien un lien générer aléatoirement avec en information pour ce lien :
        - Une chaine de 8 caractères -> $link
        - Le text récupérer dans la textBox -> $text
        - Un sel pour augmenter la sécurité
        - booleen pour savoir si le lien a déjà été ouvert où non

        Le lien fait 6 caractères. En prenant l'alphabet minuscules, majuscules et les chiffres, nous avons 62 possibilités
        ce qui fait un total de lien possible à 218 340 105 584 896
    */

    
    $succes = false
    do {
        $link = createRandomLink()
        try{
            $mysql=connect();
	        $q="INSERT INTO Links VALUES ('$link', '$text','$salt',"false")";
	        $req=$mysql->prepare($q);
	        $req->execute();
            $succes = true
        }catch(Exception $e){
            die($e->getMessage());
        }
    } while (!$succes);
    
	
}

function getNewLink(){

}

function getTextBD($link){
    /* Permet de récupérer le text stocké dans la BD à partir de l'url
        Doit mettre le booleen à vrai
        Doit mettre le mot de passe à blanc pour augmenter la sécurité
    */

    // On crée un tableau pour récupérer uniquement le 6 caractères d'authentification
    $tabLink = explode("/",$link);
    $text = end($tabLink);

    // Connexion à la base de donnée
    $mysql=connect();
    $q='SELECT * FROM Links WHERE link = '$text'';
    $req=$mysql->prepare($q);
    $req->execute();
    $data=$req->fetchAll();
    
    // Si la BD ne trouve aucune correspondance, alors on affiche que le lien n'existe pas
    if ($data.IsEmpty()){
        header('location:../../web/error_404.html');
    }
    $isUses = $data[0]['usesLink'];
    if($isUses){
        echo "Le lien a expiré.";
    }
    else{
        echo "Le text caché est :";
        echo $data[0]['text'];

    }
}



?>