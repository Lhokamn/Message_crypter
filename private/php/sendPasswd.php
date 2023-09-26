<?php session_start();
require_once('fonctions.php');
$text=$_POST['passwdText'];
createNewLink($text)
header('location:../../web/Password_diffusion.php');
?>

