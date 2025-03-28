<?php
/* Incrustar franja superior y conectarse a la base de datos */
include 'base_top.php';

$sql = "SELECT receta_id, receta_foto, Titulo, Descripcion, receta_type FROM boletines ";

$buscar = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $filter = "";
    $conector = "";

    // Filtro por búsqueda
    if (isset($_POST["buscar"])) {
        $buscar = $_POST["buscar"];    
        if (strlen($buscar) > 0) {
            $filter .= " (Titulo LIKE '%" . $_POST["buscar"] . "%' OR Descripcion LIKE '%" . $_POST["buscar"] . "%') ";
            $conector = " AND ";
        }
    }

    // Filtro por temas
    if (isset($_POST["temas"])) {
        $ftemas = "";
        $temas = $_POST["temas"];
        if (count($temas) > 0) {
            $cond = " ";
            $ftrType = "(";

            foreach ($temas as $tema) {        
                $ftrType .= $cond . " receta_type = " . $tema;
                $cond = " OR ";
            } 

            $ftrType .= ")";            
        }

        $filter .= $conector . $ftrType;
        $conector = " AND ";
    }



    // Si se agregan campos de fecha visual
    if (isset($_POST["fecha_desde"]) || isset($_POST["fecha_hasta"])) {
        $fechaDesde = $_POST["fecha_desde"];
        $fechaHasta = $_POST["fecha_hasta"];

        if (!empty($fechaDesde)) {
            $filter .= $conector . " fecha >= '" . $fechaDesde . "' "; // Cambia 'fecha' por el nombre real de tu columna de fecha
            $conector = " AND ";
        }
        if (!empty($fechaHasta)) {
            $filter .= $conector . " fecha <= '" . $fechaHasta . "' "; // Cambia 'fecha' por el nombre real de tu columna de fecha
        }
    }

    // Aplicar el filtro a la consulta SQL
    if (strlen($filter)) {
        $sql .= " WHERE " . $filter;  
    }
}

$sql .= " GROUP BY receta_id, receta_foto, Titulo, Descripcion, receta_type ";
$sql .= " ORDER BY receta_type";

$recetas = mysqli_query($conn, $sql);
?>

<style>
<?php include '../css/recetas.css'; ?>
</style>

<div class="cuerpo">
<h1>Boletínes estratégicos</h1>

<div class="busqueda">
    <form method="post" name="buscar" action="" style="display: flex; justify-content: space-between; align-items: center; margin-left: 75px; margin-right: auto;">
        <div>
            <label><input type="checkbox" name="temas[]" value="1"> Cambio climático</label>
            <label><input type="checkbox" name="temas[]" value="2"> Gestión de recursos</label>
            <label><input type="checkbox" name="temas[]" value="3"> Sistemas alimentarios</label>
            <input type="submit" value="Filtrar">
        </div>

        <!-- Filtros por fecha visual alineados a la derecha -->
        <div style="margin-left: 250px;margin-right: auto; display: flex; align-items: center;">
            <label>Desde:</label>
            <input type="date" name="fecha_desde">
            <label>Hasta:</label>
            <input type="date" name="fecha_hasta">
            <button type="button" onclick="alert('Filtro visual aplicado!')">Aplicar Filtro por Fecha</button>
        </div>
    </form>
</div>

<table>
    <tr>
        <th>Boletín</th>
        <th>Tema</th>
        <th>Titulo boletín</th>
        <th>Descripción</th>
        <th>Descarga</th>
        <?php if (isset($_SESSION["user_id"])) { ?>
            <th>Editar</th> <!-- Para el admin -->
        <?php } ?>
    </tr>

    <?php while ($row = mysqli_fetch_assoc($recetas)) { ?>
    <tr class="tfFila">
        <td class="tdFoto">
            <a title="Ingredientes" <?php echo "href=receta.php?id=" . $row['receta_id'] . " " ?>  >        
                <img src="data:image/jpg;charset=utf8;base64,<?php echo base64_encode($row['receta_foto']); ?>"  height=200px />
            </a>
        </td>
        <td class="tdNombre">
            <?php 
                if ($row['receta_type'] == 1) {
                    echo "Cambio climático";
                } elseif ($row['receta_type'] == 2) {
                    echo "Gestión de recursos";
                } elseif ($row['receta_type'] == 3) {
                    echo "Sistemas alimentarios";
                }
            ?> 
        </td>
        <td class="tdNombre"><?php echo $row['Titulo']; ?> </td>
        <td class="tdPreparacion"><?php echo $row['Descripcion']; ?> </td>
        <td class="tdOpcion">
            <button>Descargar</button>
        </td>
        <?php if (isset($_SESSION["user_id"])) { ?>
            <td class="tdCalificar">
                <a title="1" <?php echo "href=calificar.php?idReceta=" . $row['receta_id'] . "&calificacion=1" ?>  >
                    <img src='../images/editar.png' width="24" height="24"/>				
                </a>
            </td>
        <?php } ?>
    </tr>
    <?php } ?>
</table>
</div>

<?php
/* Incrustar franja inferior */
include 'base_bottom.php';
?>
