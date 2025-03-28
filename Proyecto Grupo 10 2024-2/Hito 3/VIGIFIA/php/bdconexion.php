<?php
$servername="localhost";
$username ="admin";
$password = "!dBeK8jy21r/3nMt";
$database = "primerabase";
$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>