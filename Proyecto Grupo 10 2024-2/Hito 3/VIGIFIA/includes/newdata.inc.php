<?php 
session_start();
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $old_username = $_SESSION["user_username"];
    $username = $_POST["newusername"];
    $pwd = $_POST["newpwd"];
    $pwd2 = $_POST["newpwd2"];

    try {
        require_once "dbh.inc.php";
        require_once "newdata_model.inc.php";
        
        require_once "newdata_contr.inc.php";
        

        $errors = [];

        if (new_input_vacio($username, $pwd, $pwd2)) {
            $errors["input_vacio"] = "Por favor llenar todos los campos";
        }

        
        

        //require_once("config_session.inc.php");

        if ($errors){
            $_SESSION["errors_login"] = $errors;
            header("Location: ../php/perfil.php");
            die();
        }


        $result = new_get_user($pdo, $old_username);
        $aux = $_SESSION["user_id"];


        new_actualizar_login($pdo,$username,$pwd,$aux);

        
        

        $newSessionId = session_create_id();
        $sessionId = $newSessionId . "_" . $result["id"];
        session_id($sessionId);

        $_SESSION["user_id"] = $result["id"];
        $_SESSION["user_username"] = $username;
        $_SESSION["email"] = $result["email"];
        $_SESSION["login_date"] = $result["users_login_date"];
        $_SESSION["login_time"] = $result["users_login_hour"];
        $_SESSION["delete"] = 0;

        
        $_SESSION["ultimo_valor"] = time();

        


        header("Location: ../php/login.php");
        
        $pdo = null;
        $statement = null;
        die();

    } catch (PDOException $e) {
        die("Query Failed". $e->getMessage());
    }

} else {
    header("Location: ../php/login.php");
    die();
}