## Sobre entrega Hito 4

Para la correcta revisión de esta entrega, se necesita **tener instalado Python y PostgreSQL** y seguir los siguientes pasos:
* Descargar el archivo _"hito_4.zip"_ del rspositorio de GitHub, descomprimirlo y abrir la carpeta _"VIGIFIA"_. 
* En dicha carpeta, haciendo click derecho en el espacio vacío de la carpeta, abrir Windows Powershell _(de no aparecer, buscar Windows Powershell en el buscador de archivos, y navegar hasta dicha carpeta)_. Es importante no cerrar jamás la ventana, para no cerrar el entorno.
* En WPS, crear un entorno virtual con el siguiente código: 
	```
	python -m venv nombre_del_entorno #"nombre_del_entorno" puede ser cualquier nombre a elección. 
	```
 * Luego, sin nunca salir del directorio anterior en el WPS, activar el entorno con el siguiente código:
	```
	nombre_del_entorno\Scripts.\activate

 	#De haber un error, intentar de nuevo, pero correr este código antes:
	Set-ExecutionPolicy RemoteSigned
 	# Y colocar "S" para aceptar.
	```
* Volver a la carpeta _VIGIFIA_ 	```cd .. #Comando para dirigirse a la carpeta padre en WPS```		
* Ejecutar en WPS:
	```
	pip install -r requirements.txt
	```
* Abrir la carpeta base _"VIGIFIA"_ (la que contiene todos los archivos, incluyendo otra carpeta del mismo nombre) en _Visual Studio Code_
* Ir a la otra carpeta _"VIGIFIA"_ que se encuentra en el interior, e ir a _"setting.py"_, y cambiar la contraseña de database por la propia de PostgreSQL.
* Abrir la aplicación ***PGAdmin4*** _(incluída con PostgreSQL)_ y crear una nueva base llamada _postgres_ que esté vacía (solo en caso de que no esté creada. En caso de que esté creada, verificar que esté vacía en Servers > Databases > postgres > Schemas > Public > Tables).
* Dirigirse donde se encuentra el archivo _"tester.dump"_ en Windows Powershell _(carpeta "VIGIFIA" padre)_ y ejecutar el siguiente código:
	```
	pg_restore -U postgres -h localhost -p 5432 -d postgres tester.dump # Y posteriormente colocar la contraseña que ocupamos en PostgreSQL.
 	```
* Luego, ejecutar el código:
	```
 	python manage.py runserver 
 	```
* Finalmente, dirigirse a la dirección que se muestra por consola con su navegador web (preferiblemente Chrome).

### Observaciones:
* **Si no funciona la conexión con la base de datos, hay que ir al path y colocar postgres.bin.**
* Si en algún momento cerramos el entorno en Windows Powershell, este tiene que volverse a abrir para que todos los pasos funcionen correctamente.
