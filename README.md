# IMPORTANTE

En linux hay que adicionar esta configuracion para usar la ruta del soket de mysql XAMPP

<code>
DATABASES = {
    'default': {
        # MySQL engine. Powered by the mysqlclient module.
        #your credentiales
        'OPTIONS': {
            'unix_socket': '/opt/lampp/var/mysql/mysql.sock',
        },
    }
}
</code>

Comando para actualizar requirements.txt

<code>
pip freeze > requirements.txt
</code>

Comando para instalar

<code>
pip install -r requirements.txt
</code>

# TIPS FOR DIPLOYMENT WITH RALYWAY
## Conexion a base de datos mysql (XAMPP) local
**En linux**
ve al directorio

<code>/opt/lampp/bin</code>

luego ejecuta el comando de <a href="https://railway.app/">ralyway</a> añadiendo esto al inicio "./"

Ejemplo


<code>./mysql -hcontainers-us-west....//resto del codigo </code>


acto seguido pega el codigo sql generado por el backup en la terminal

## Salida a intenert

> Tenia un problema con el deploy, se me ejecutava de manera local en el servidor, para ello realizé lo liguiente

cree el archivo railway.yml y cambie el comando de inicio a:

<code>
python manage.py migrate && gunicorn API_VICTORIA.wsgi</code>



