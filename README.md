
# PIG Grupo 17

Este repositorio contiene el proyecto integrador grupal del grupo 17 con temática de alquiler de películas para el curso Python Avanzado con Django de Codo a Codo 2024.



## Requisitos

Instalarse :

 - Python
 - Git
 - PostgreSQL (pgAdmin recomendado)

 ## Clonar el repositorio

 Primero, clona el repositorio en algún directorio:

 ```bash
  git clone https://github.com/danielrozas/PIG_Grupo17.git
```
 ## Configuración del entorno virtual

 Crea un entorno virtual en el directorio donde se encuentra el repositorio del proyecto:

  ```bash
  python -m venv PIG_Grupo17Venv
```
 
Activa el entorno virtual:

 ```bash
  PIG_Grupo17Venv\Scripts\activate
```

## Instalación de dependencias

Instala las dependencias del proyecto:

```bash
  PIG_Grupo17Venv\Scripts\pip install django psycopg2 pillow
```
## Configuración de PostgreSQL

Para gestionar la base de datos, vamos a usar pgAdmin.

### Creación de la base de datos

1. Abre pgAdmin y conéctate a tu servidor de PostgreSQL.

2. Crea una nueva base de datos llamada 'pig_grupo17'.

## Configuración del proyecto

Antes de ejecutar el proyecto, tenemos que configurar la conexión a la base de datos. Abre el archivo **settings.py** del proyecto y busca la sección DATABASES. Modifica la configuración de la base de datos para incluir tu usuario y contraseña de PostgreSQL:

```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pig_grupo17',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
## Migraciones de la base de datos

Ahora necesitas aplicar las migraciones existentes a tu base de datos. Ejecuta el siguiente comando:

```bash
 PIG_Grupo17\python manage.py migrate
```

## Ejecución del proyecto

Finalmente podemos correr el proyecto con el siguiente comando, tener en cuenta que el entorno virtual debe estar activado:

```bash
 PIG_Grupo17\python manage.py runserver
```