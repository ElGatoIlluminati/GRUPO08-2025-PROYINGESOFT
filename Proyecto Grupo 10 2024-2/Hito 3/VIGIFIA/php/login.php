
<?php include 'base_top.php' ?>

    <div class="cuerpo">

        <div id="loginbox">
        <form action="../includes/login.inc.php" method="post">
            <h1> Login </h1>
            <?php if (isset($_GET['error'])) { ?> 
                <p class= "error"> <?php echo $_GET['error']; ?> </p>
            <?php } ?>
            
            
            <input type="text" name = "username" placeholder="Nombre y Apellido"> <br>            
            <input type="password" name = "pwd" placeholder="Contraseña"> <br>

            <button>Iniciar sesión</button>
        </form>
      
        <?php 
        check_login_errors();
        ?>
        </div>

    </div>
    
<?php include 'base_bottom.php' ?>