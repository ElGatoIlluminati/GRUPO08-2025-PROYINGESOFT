<?php

declare(strict_types= 1);

date_default_timezone_set('Etc/GMT-3');

function get_user(object $pdo, string $username){
    $query = "SELECT * FROM users WHERE user_name = :username;";

    $stmt = $pdo->prepare($query);
    $stmt->bindParam(":username", $username);
    $stmt->execute();
    
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    return $result;
}

function update_user(object $pdo, string $username, int $id){
    $tdate=date("Y-m-d");
    $ttime=date("H:i:s");

    $query = "UPDATE users SET users_login_date = :date, users_login_hour = :time WHERE user_name = :username";

    $stmt = $pdo->prepare($query);

    $stmt->bindParam(':date', $tdate);
    $stmt->bindParam(':time', $ttime);
    $stmt->bindParam(':username', $username);

    $stmt->execute();

    $query = "INSERT INTO users (id)
          SELECT :id_usuario
          WHERE NOT EXISTS (
              SELECT 1
              FROM users
              WHERE id = :id_usuario
          );";
    
    $stmt2 = $pdo->prepare($query);

    $stmt2->bindParam(":id_usuario", $id);
    $stmt2->execute();
}