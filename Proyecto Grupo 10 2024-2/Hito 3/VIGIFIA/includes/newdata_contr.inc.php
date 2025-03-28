<?php

declare(strict_types= 1);



function is_password_wrong(string $pwd, string $hashpwd){
    if (!password_verify($pwd, $hashpwd)) {
        return true;
    } else {
        return false;
    }
}


function new_input_vacio(string $username, string $pwd, string $pwd2){
    if (empty($username) || empty($pwd) || empty($pwd2)) {
        return true;
    } else {
        return false;
    }
}

function new_actualizar_login(object $pdo, string $username, string $pwd, int $id){
    new_update_user($pdo, $username, $pwd, $id);
}