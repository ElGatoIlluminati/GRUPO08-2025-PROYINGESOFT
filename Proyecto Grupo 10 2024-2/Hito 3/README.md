## Sobre entrega Hito 3

Sólo para esta entrega, nuestro de avance de código ocupa el modelo MySQL para mostrar correctamente la previsualización de lo que será la interfaz del proyecto. En este, trabajamos con XAMPP, ya que ocupamos de base un trabajo anterior hecho en el ramo Base de Datos. Todo lo relacionado a este trabajo anterior será eliminado para futuras entregas, y se adaptará a la base de datos correspondiente (PostgresSQL). 

Para la correcta visualización de la página, se debe hacer lo siguiente:
* Se debe descargar la última versión de [XAMPP correspondiente](https://www.apachefriends.org/es/index.html)
* Se debe iniciar Apache y MySQL a través del panel de control de XAMPP.
* En el mismo panel de control, en el botón "Shell", pegar el siguiente código
    ```
    mysql -u root
    CREATE USER 'admin'@'localhost' IDENTIFIED BY '!dBeK8jy21r/3nMt';
    GRANT ALL PRIVILEGES ON primerabase.* TO 'admin'@'localhost';
    FLUSH PRIVILEGES;
    ```
* Se debe descargar y mover la carpeta "VIGIFIA" a la carpeta htdocs de la carpeta de XAMPP (La dirección en el explorador de archivos suele ser C:\xampp\htdocs)
* Se debe descargar el archivo "primerabase.sql", ir al panel de control de phpmyadmin y crear la base de datos "primerabase"
* Luego, en el mismo panel de control, seleccionar "importar" y subir el archivo "primerabase.sql"
* Finalmente, ir a la dirección "http://localhost/VIGIFIA/php/index.php"
