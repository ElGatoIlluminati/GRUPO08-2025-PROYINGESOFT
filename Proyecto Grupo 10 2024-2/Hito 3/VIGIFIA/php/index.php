<?php 
/* Incrustar franja superior*/ 
include 'base_top.php';
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VIGIFIA</title>
    <style>
        /* Estilos generales de la página */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body, html {
            height: 100%;
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            height: 100vh;
            padding: 20px;
        }
        h1 {
            font-size: 4em;
            color: #333;
            font-weight: bold;
            letter-spacing: 2px;
        }
        p {
            font-size: 1.2em;
            color: #666;
            margin-top: 20px;
        }
        .btn {
            display: inline-block;
            margin-top: 30px;
            padding: 15px 30px;
            font-size: 1em;
            font-weight: bold;
            color: #fff;
            background-color: #007bff;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .btn:hover {
            background-color: #0056b3;
        }

        .quienes-somos {
            margin-top: 40px;
            max-width: 600px;
            text-align: left;
        }
        .quienes-somos h2 {
            font-size: 2em;
            color: #333;
            margin-bottom: 10px;
        }
        .editable-text {
            font-size: 1em;
            color: #666;
            line-height: 1.5;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>VIGIFIA</h1>
        <p>Plataforma de monitoreo estratégico.</p>
        <a href="#" class="btn">Explorar más</a>

        <!-- Sección "Quiénes somos" -->
        <div class="quienes-somos">
            <h2>Quiénes Somos</h2>
            <div contenteditable="false" class="text">
            En VIGIFIA, nuestra misión es promover procesos de innovación en el sector silvoagropecuario y la cadena agroalimentaria. 
            Nos dedicamos al desarrollo de capacidades y a la articulación de esfuerzos, así como a la provisión de información 
            estratégica que fomente la generación de innovaciones. Creemos firmemente que estas iniciativas son esenciales para 
            contribuir al desarrollo sostenible en todas las regiones del país.</div>
        </div>
    </div>
</body>
</html>

<?php include 'base_bottom.php' ?>
