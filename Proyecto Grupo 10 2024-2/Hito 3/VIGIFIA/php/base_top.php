<?php 
require_once("../includes/signup_view.inc.php");
require_once("../includes/config_session.inc.php");
require_once("../includes/login_view.inc.php");
include 'bdconexion.php';
?>

<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="../css/estilo.css">

  <!-- Contenido de la pestaña -->
  <link rel="icon" type="images/png" href="../images/descarga.webp" />
  <title> Prototipo VIGIFIA </title>

</head>

<body>

    <!-- Cabecera/Menú -->
    <div class="cabeza">
        <div class = "Boton Logo">
        <a href="index.php" >
            <img title="AAAA" src="../images/VIGIFIA.png" width="170px">
        </a>
        </div>

        <div class = "Boton Boletines">
        <a class="FullBoton" title="Lista de Boletines Disponibles" href="boletines.php">Boletines</a>
        </div>
        
        <div class = "Boton Usuario">
            <?php
            //Esto significa que estamos logeados
            if (isset($_SESSION["user_id"])) { ?>
                <a class="FullBoton" title="Perfil de Usuario" href="perfil.php">Perfil</a>
                <?php 
            } else { ?>
                <a class="FullBoton" title="Inicio de Sesión" href="login.php">Inicia Sesión</a>
                <?php
            } ?>
        
        </div>
    </div>
    <!-- Contenido de la página, cuerpo completo de la página -->
</body>