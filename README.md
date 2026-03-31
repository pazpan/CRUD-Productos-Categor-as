Sistema de Gestión de Productos y Categorías

Aplicación web desarrollada con Django que permite la gestión de productos y categorías mediante operaciones CRUD, incorporando autenticación de usuarios (registro e inicio de sesión).


Funcionalidades

-Registro de usuarios
-Inicio de sesión (login)
-Gestión de productos (crear, editar, eliminar, listar)
-Gestión de categorías (crear, editar, eliminar, listar)
-Relación entre productos y categorías
-Visualización de listados de productos y categorías


Tecnologías utilizadas
-Python
-Django
-HTML / CSS
-SQL (SQL Server / SQLite)

Capturas de pantalla
![ed](https://github.com/user-attachments/assets/6224226b-1947-4a82-8a17-8e3958aa12b8)
![p](https://github.com/user-attachments/assets/718cfeed-497b-4fa0-828a-9a414cdd2313)
![log](https://github.com/user-attachments/assets/85ed392f-90aa-4050-aeb1-401778af914b)
![re](https://github.com/user-attachments/assets/18c3bfd7-486f-4faa-92fa-b7c064666b9f)


Instalación y ejecución

1. Clonar el repositorio:

git clone https://github.com/pazpan/CRUD-Productos-Categor-as

2. Acceder al proyecto:

cd CRUD-Productos-Categor-as

3. Crear entorno virtual:

python -m venv venv

4. Activar entorno virtual:

En Windows:
venv\Scripts\activate

En Linux/Mac:
source venv/bin/activate

5. Instalar dependencias:

pip install -r requirements.txt

6. Ejecutar migraciones:

python manage.py migrate

7. Ejecutar servidor:

python manage.py runserver

8. Abrir en navegador:

http://127.0.0.1:8000/


Autor

Desarrollado por Camila Vasquez

Descripción

Este proyecto fue desarrollado como práctica para reforzar conocimientos en desarrollo web con Django, manejo de bases de datos y lógica de negocio en aplicaciones CRUD.


