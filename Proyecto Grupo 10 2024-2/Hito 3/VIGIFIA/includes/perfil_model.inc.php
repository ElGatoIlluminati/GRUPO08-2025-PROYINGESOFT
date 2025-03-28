<?php

//trampa antiweones (yo)
declare(strict_types= 1);

function getDatosPerfil(object $pdo, string $username){
    $query = "SELECT * FROM users WHERE user_name = :username;";

    $stmt = $pdo->prepare($query);
    $stmt->bindParam(":username", $username);
    $stmt->execute();

    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    return $result;
}
?>