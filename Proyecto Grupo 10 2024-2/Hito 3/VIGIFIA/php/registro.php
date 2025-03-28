<?php

/* Incrustar franja superior y conectarse a la base de datos */
include 'base_top.php';

?>

<div class="cuerpo">

    <h1>Registrarse</h1>

        <form action="../includes/signup.inc.php", method = "post">

            <?php
            signup_inputs();
            ?>
            <button>Crear cuenta nueva</button>

        </form>

        <?php
        check_signup_errors();
        ?>

</div>

<?php
/* Incrustar franja inferior */
include 'base_bottom.php' 
?>