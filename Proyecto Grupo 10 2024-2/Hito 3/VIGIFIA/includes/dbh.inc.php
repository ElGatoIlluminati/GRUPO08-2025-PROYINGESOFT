<?php

$servername="localhost";
$username_ad ="admin";
$password = "!dBeK8jy21r/3nMt";
$database = "primerabase";

try {
    $pdo = new PDO("mysql:host=$servername;dbname=$database", $username_ad, $password);

    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

} catch (PDOException $e) {
    die("Connection Failed: ". $e->getMessage());
}
?>