En caso de no funcionar la Base de Datos, correr los siguientes códigos en la terminal:
```
del main\migrations\0*.py
pip install -r requirements.txt 
psql -U postgre -d postgre 
```
Salir de psql con \q y ejecutar en terminal (fuera de psql):
```
rm db.sqlite3   
python manage.py flush
```
Esto borra todos los datos y reinicia todo, incluyendo los permisos.

Luego:
```
python manage.py makemigrations
python manage.py migrate
```

Si se quiere probar los botones de los boletines, simplemente crear un boletin con el boton "Crear boletin".
Se debe iniciar sesión con un perfil de editor para crear un boletin.
Cualquier duda con la base de datos, consultar por discord.
