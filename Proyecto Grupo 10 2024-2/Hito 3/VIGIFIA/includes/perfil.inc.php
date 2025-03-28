<?php
// login.inc.php

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = htmlspecialchars(trim($_POST["username"]));
    $password = trim($_POST["pwd"]);

    if (empty($username) || empty($password)) {
        header("Location: ../php/login.php?error=Please fill in all fields");
        exit();
    }

    try {
        require_once "dbh.inc.php";
        
        $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->bindParam(':username', $username, PDO::PARAM_STR);
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        
        if ($user && password_verify($password, $user['password'])) {
            session_start();
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            $_SESSION['role'] = $user['role'];

            if ($user['role'] === 'admin') {
                header("Location: ../php/admin_dashboard.php");
            } else {
                header("Location: ../php/user_dashboard.php");
            }
            exit();
        } else {
            header("Location: ../php/login.php?error=Invalid credentials");
            exit();
        }
    } catch (PDOException $e) {
        die("Query failed: " . $e->getMessage());
    } finally {
        $pdo = null;
    }
} else {
    header("Location: ../php/login.php");
    exit();
}
?>
