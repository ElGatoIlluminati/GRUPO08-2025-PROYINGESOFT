<?php 
require_once("../includes/perfil_view.inc.php");
?>
<?php include 'base_top.php' ?>
<html>
    <style>
        table {
            width: 60.7%;
            display: grid;
            grid-template-columns: repeat(3,1fr);
            grid-gap: 10px;
            border: 1px solid grey;
        }
        th,td {
            border: 1px solid grey;
            padding: 10px;
        }
        .pill-mass{
            font-size: 12px;
            font-family: "Raedex Pro", sans-serif;
            padding: 0.25em 1em;
            margin: 0.25em;
            border-radius: 1em;
        }
        .pill-log{
            font-size: 12px;
            font-family: "Raedex Pro", sans-serif;
            padding: 1.25em 1em;
            margin: 0.25em;
            border-radius: 1em;
            
        }
        .container {
        }
        .listafav{
            width: 1100px;
            height: 480px;
            float: right;
            margin: 90px;
            
        }

        
        .card {
            width: 350px;
            height: 480px;
            float: left;
            margin: 90px;
            
        }

        .card-inner, .fav-card{
            background: #f0eee9;
            
            text-align: justify;
            -moz-text-align-last: center;
            text-align-last: center;
            
            width: 100%;
            height: 100%;
            --position: relative;
            border-radius: 15px;
            box-shadow: 10px 20px 50px;
            padding: 10px;
        }
        .divleft {
            text-align: center;
            --background-color: lightblue;
            min-height: 50vh;
            width: 50%;
            float: left;
        }
        .divright {
            text-align: center;
            --background-color: lightblue;
            width: 50%;
            float: right;
        }
        .divcenter {
            text-align: center;
            float: center;
        }
        .card_profile {
            
            text-align: center;
            background-clip: padding-box;
            box-shadow: 0 1px 4px rgba(24,28,33,0,012);
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 20px;
            width: 30%;
            height: 47%;
            margin: 0 auto;
        }


    </style>
    <div class="container">
        <div class="card">
            <div class="card-inner">
                <form action="../includes/perfil_view.inc.php" method="post">

                    <p style="text-align: justify;"> Nombre de Usuario: <?php echo getName(); ?>  </p>
                    <p style="text-align: justify;"> Tipo de usuario: Administrador  </p>
                    <p style="text-align: justify;"> Correo: <?php echo getMail(); ?> </p>
                    <p style="text-align: justify;"> Ultima Fecha de Sesion: <?php echo getLoginDate(); ?> </p>
                    <p style="text-align: justify;"> Ultima Hora de Sesion: <?php echo getLoginTime(); ?> </p>
                    <p style="text-align: justify;"> <?php // echo '<pre>' . print_r($_SESSION, TRUE) . '</pre>';?> </p>

                </form>
                <div class="divcenter">
                    <form action="../includes/newdata.inc.php" method="post">
                        <h4>Modificar Cuenta</h4>
                        <input type="text" name = "newusername" placeholder="Nombre y Apellido">            
                        <input type="password" name = "newpwd" placeholder="Nueva Contraseña"> 
                        <input type="password" name = "newpwd2" placeholder="Confirmar Contraseña"> <br>
                        <button class="pill-mass"> enviar</button>
                    </form>
                </div>
                <div class="divleft">
                    <h3>Logout</h3>
                    <form action="../includes/logout.inc.php" method="post">
                        <button class="pill-log">Cerrar la Sesion</button>
                    </form>
                </div>
                <div class="divright">
                    <form action="../includes/userdelete.inc.php" method="post">
                        <h3>Delete Account</h3>
                        <button class="pill-log" onclick="return borrar_cuenta_click()">Borrar Cuenta</button>
                        <p id="demo"></p>
                    </form>
                    <script>
                        function borrar_cuenta_click() {
                            var r = confirm("¿Estas Seguro De Querer Borrar tu Cuenta?");
                            if (r == true) {
                                var form = document.getElementById("delete-form");
                                <?php $_SESSION["delete"] = 1; ?>
                                form.submit();
                            } else {
                                <?php $_SESSION["delete"] = 0; ?>
                                return false;
                            }
                        }
                    </script>
                </div>

                
                
            </div>
        </div>
        
    </div>
</html> 
    
<?php include 'base_bottom.php' ?>