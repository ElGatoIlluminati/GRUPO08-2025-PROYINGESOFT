
# Proyecto VigiFIA - Hito 5: Versión Final

## Tecnologías Utilizadas

- **Backend:** Python 3.11, Django 5.2
- **Base de Datos:** PostgreSQL 15
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Editor de Contenido:** Django Summernote (Editor WYSIWYG)
- **Contenerización:** Docker y Docker Compose

---

## Guía de Instalación y Ejecución Local

Siga estos pasos en orden para levantar el proyecto. Se asume que tiene **Docker Desktop** instalado y en ejecución.

### 1. Clonar el Repositorio

Primero, clonar este repositorio en la máquina local y navegar a la carpeta correcta.

```bash
# Clonar el repositorio desde GitHub
git clone https://github.com/ElGatoIlluminati/GRUPO08-2025-PROYINGESOFT.git

# Navegar a la carpeta del Hito 5
cd "GRUPO08-2025-PROYINGESOFT/Hito 5/"
````

### 2\. Configurar las Variables de Entorno

El proyecto necesita un archivo `.env` para cargar las credenciales y configuraciones. Se incluyó una plantilla para facilitar el proceso.

```bash
# En Windows (usando PowerShell), Mac o Linux
cp .env.example .env
```

> **Nota:** No se necesita modificar este archivo. Los valores por defecto están diseñados para funcionar con la configuración de Docker Compose.

### 3\. Construir y Levantar los Contenedores

Ahora, se leerá el archivo `docker-compose.yml`, construirá la imagen de Python/Django con todas las dependencias y levantará los servicios de la aplicación (`web`) y la base de datos (`db`).

```bash
docker-compose up --build -d
```

  - `--build`: Fuerza la reconstrucción de la imagen para asegurar que se usen las últimas versiones de los archivos.
  - `-d`: (Detached mode) Ejecuta los contenedores en segundo plano, dejando su terminal libre.

### 4\. Preparar la Base de Datos

Con los contenedores ya corriendo, se necesita inicializar la base de datos.

1.  **Aplicar Migraciones:** Este comando crea toda la estructura de tablas que Django necesita.

    ```bash
    docker-compose exec web python manage.py migrate
    ```

2.  **Crear un Superusuario (Opcional, pero recomendado):** Para tener acceso total al panel de administración de Django, se puede crear una cuenta propia de superusuario.

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

    Seguir las instrucciones en pantalla para elegir un nombre de usuario, correo y contraseña.

3.  **Cargar Datos de Prueba:** Este es el paso más importante. Ejecutar el script que crea los usuarios, categorías y boletines de ejemplo.

    ```bash
    docker-compose exec web python manage.py crear_usuarios_prueba
    ```

### 5\. Final

Ahora la aplicación ya está completamente funcional.

  - **Acceder a la Página Web:** Abrir el navegador e ir a **[http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)**
  - **Acceder al Panel de Administración:** Se puede ir a **[http://localhost:8000/admin/](https://www.google.com/search?q=http://localhost:8000/admin/)** y usar las credenciales del superusuario que se crearon en el paso anterior.

### Credenciales de Acceso (Usuarios de Prueba)

Para facilitar la revisión, se pueden usar las siguientes cuentas pre-cargadas en la página de "Iniciar Sesión":

| Rol | Usuario | Contraseña |
| :--- | :--- | :--- |
| **Administrador** | `admin` | `admin123` |
| **Editor** | `editor` | `editor123` |
| **Lector** | `lector` | `lector123` |

-----

### Cómo Detener la Aplicación

Cuando se haya terminado de revisar, se pueden detener todos los servicios de Docker con el siguiente comando:

```bash
docker-compose down
```

> **Nota:** Si se desea borrar también la base de datos para empezar de cero la próxima vez, se debe usar:

```bash
docker-compose down -v
```


¡Por supuesto\! Lamento mucho que el bloque anterior no se haya mostrado correctamente. A veces la interfaz puede tener problemas.

Aquí tienes el texto completo del `README.md` en formato Markdown para que puedas copiarlo y pegarlo directamente en tu archivo `Hito 5/README.md`.

-----

````md
# Proyecto VigiFIA - Hito 5: Versión Final

¡Bienvenido a la versión final del proyecto VigiFIA! Este documento contiene todas las instrucciones necesarias para configurar, ejecutar y revisar la aplicación web en un entorno de desarrollo local utilizando Docker.

## 📜 Descripción del Proyecto

VigiFIA es una plataforma web desarrollada en Django para la gestión y visualización de boletines de vigilancia tecnológica. Permite a los administradores y editores crear, gestionar y publicar boletines que pueden incluir contenido enriquecido y archivos PDF. Los usuarios pueden registrarse, ver los boletines y acceder a funcionalidades según su rol asignado (administrador, editor o lector).

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3.11, Django 5.2
- **Base de Datos:** PostgreSQL 15
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Editor de Contenido:** Django Summernote (Editor WYSIWYG)
- **Contenerización:** Docker y Docker Compose

---

## 🚀 Guía de Instalación y Ejecución Local

Siga estos pasos en orden para levantar el proyecto. Se asume que tiene **Docker Desktop** instalado y en ejecución.

### 1. Clonar el Repositorio y Preparar el Entorno

```bash
# 1. Clonar el repositorio desde GitHub
git clone [https://github.com/ElGatoIlluminati/GRUPO08-2025-PROYINGESOFT.git](https://github.com/ElGatoIlluminati/GRUPO08-2025-PROYINGESOFT.git)

# 2. Navegar a la carpeta del Hito 5
cd GRUPO08-2025-PROYINGESOFT/Hito\ 5/

# 3. Crear el archivo de entorno a partir del ejemplo
cp .env.example .env
````

> **Nota:** No necesita modificar el archivo `.env`. Los valores por defecto funcionarán.

### 2\. Construir e Iniciar los Contenedores

Este comando levantará todos los servicios necesarios en segundo plano.

```bash
docker-compose up --build -d
```

### 3\. Preparar la Base de Datos

Con los contenedores corriendo, necesitamos inicializar la base de datos con toda la estructura y los datos de prueba.

1.  **Aplicar Migraciones:** Crea la estructura de tablas.

    ```bash
    docker-compose exec web python manage.py migrate
    ```

2.  **Cargar Datos de Prueba:** Este es el paso más importante. Ejecuta el script que crea los usuarios, categorías y boletines de ejemplo.

    ```bash
    docker-compose exec web python manage.py crear_usuarios_prueba
    ```

### 4\. ¡Proyecto Listo\!

¡Felicidades\! La aplicación ya está completamente funcional.

  - **Acceda a la Página Web:** Abra su navegador y vaya a 👉 **[http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)**
  - **Acceda al Panel de Administración:** Puede ir a 👉 **[http://localhost:8000/admin/](https://www.google.com/search?q=http://localhost:8000/admin/)** y usar las credenciales de la cuenta de administrador.

### 🔑 Credenciales de Acceso

Puede usar las siguientes cuentas pre-cargadas para probar los diferentes roles en la página:

| Rol | Usuario | Contraseña |
| :--- | :--- | :--- |
| 🧑‍💻 **Administrador** | `admin` | `admin123` |
| ✍️ **Editor** | `editor` | `editor123` |
| 📖 **Lector** | `lector` | `lector123` |

-----

### 🛑 Cómo Detener la Aplicación

Cuando haya terminado de revisar, puede detener todos los servicios de Docker con:

```bash
docker-compose down
```

> **Para empezar de cero**, use `docker-compose down -v` para borrar también el volumen de la base de datos.

```
```