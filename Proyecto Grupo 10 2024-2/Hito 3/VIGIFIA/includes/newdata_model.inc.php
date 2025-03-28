<?php
declare(strict_types= 1);

function new_get_user(object $pdo, string $username){
    $query = "SELECT * FROM users WHERE user_name = :username;";

    $stmt = $pdo->prepare($query);
    $stmt->bindParam(":username", $username);
    $stmt->execute();
    
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    return $result;
}


function new_update_user(object $pdo, string $username, string $pwd , int $id){
    $query = "UPDATE users SET user_name = :new_username, user_password= :new_pwd WHERE id =:old_id;";
    $stmt = $pdo->prepare($query);

    $options = [
        'cost' => 12
    ];

    $hashpwd = password_hash($pwd, PASSWORD_BCRYPT, $options);

    $stmt->bindParam(":new_username", $username);
    $stmt->bindParam(':new_pwd', $hashpwd);

    $stmt->bindParam(":old_id", $id);

    $stmt->execute();


}