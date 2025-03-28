<?php
include 'base_top.php';
require_once 'bdconexion.php';

$idUser = 0;
$comentarios = "";

if (isset($_SESSION["user_id"])) {
    $idUser = $_SESSION["user_id"];
}

$query = "SELECT receta_id, Titulo, Descripcion FROM boletines";
$result = $conn->query($query);

if (!$result) {
    die("Error al obtener boletines: " . $conn->error);
}

$idRecetaSeleccionada = isset($_GET['idReceta']) ? $_GET['idReceta'] : null;
$descripcion = "";

if ($idRecetaSeleccionada) {
    $stmt = $conn->prepare("SELECT Descripcion FROM boletines WHERE receta_id = ?");
    $stmt->bind_param("i", $idRecetaSeleccionada);
    $stmt->execute();
    $stmt->bind_result($descripcion);
    $stmt->fetch();
    $stmt->close();
}

?>

<style>
<?php include '../css/recetas.css'; ?>
</style>

<div class="cuerpo">
    <br>
    <h1>Gestión de Boletines</h1>

    <button style="margin-bottom: 10px;" onclick="alert('Función de subir tema')">Subir Tema Boletín Estratégico</button>

    <form method="get" name="calificar" action="calificar.php"> 
        <table id="Semanal">

            <tr>
                <th style="width: 100px; text-align:left;">
                    Boletín
                </th>
                <td>
                    <!-- Desplegable con boletines -->
                    <select name="idReceta" onchange="this.form.submit()">
                        <option value="">Seleccionar Boletín</option>
                        <?php while ($receta = $result->fetch_assoc()) { ?>
                            <option value="<?php echo $receta['receta_id']; ?>" <?php if ($receta['receta_id'] == $idRecetaSeleccionada) echo 'selected'; ?>>
                                <?php echo htmlspecialchars($receta['Titulo']); ?>
                            </option>
                        <?php } ?>
                    </select>  
                </td>
            </tr>

            <tr>
                <th style="width: 100px; text-align:left;">
                    Descripción
                </th>
                <td>
                    <p><?php echo htmlspecialchars($descripcion); ?></p>                   
                </td>
            </tr>

            <tr>
                <th style="width: 100px; text-align:left;">
                    Comentarios
                </th>
                <td>
                    <input class="comentarios" type="text" name="comentarios" />
                </td>
            </tr>

            <tr>
            <th style="width: 100px; text-align:left;">
                    Opciones
                </th>
                <td>
                    <!-- Opciones CRUD (solo visuales) -->
                    <button type="button" onclick="alert('Función para Ver boletín')">Ver</button>
                    <button type="button" onclick="alert('Función para Editar boletín')">Editar</button>
                    <button type="button" onclick="alert('Función para Eliminar boletín')">Eliminar</button>
                </td>
            </tr>
        </table>
    </form>
</div>

<?php
include 'base_bottom.php';
$conn->close();
?>
