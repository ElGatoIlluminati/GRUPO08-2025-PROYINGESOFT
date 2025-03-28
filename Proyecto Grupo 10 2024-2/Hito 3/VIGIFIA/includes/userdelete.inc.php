<?php 
session_start();
if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $username = $_SESSION["user_username"];
    $id = $_SESSION["user_id"];
    $id = (int)$id;
    try {
        require_once "dbh.inc.php";

        $query = "DELETE FROM users WHERE id= :id;";
        $stmt = $pdo->prepare($query);


        $stmt->bindParam(":id", $id);
    
        try {
            $stmt->execute();
        } catch (PDOException $e) {
            echo "No funciono". $e->getMessage();
        }
        $pdo = null;
        $stmt = null;

        header("Location: logout.inc.php");
        die();

    } catch (PDOException $e) {
        die("Query Failed". $e->getMessage());
    }

} else {
    header("Location: ../php/login.php");
    die();
}
?>