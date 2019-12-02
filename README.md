# Ejemplo de Dashboard para perfiles de Twitter

Prueba de frontal para consultar estadísticas relativas al engagement y sentimientos de un perfil de Twitter o asociado a una cierta terminología.
* El diseño del fontal se ha realizado mediante [Bootstrap](https://bootstrapstudio.io)
* Para el scrapping de Twitter s eha usado la librería [twitterscraper](https://github.com/taspinar/twitterscraper).
* La representación de las keywords más relevantes se hace con [word_cloud](https://github.com/amueller/word_cloud).
* El análisis de sentimiento corre a cargo de la librería [TextBlob](https://github.com/sloria/textblob).


## Uso rápido de la herramienta
Clone este repositorio mediante:
```bash 
$ git clone https://github.com/eblancoh/twitter-panel.git
```

Créese un entorno virtual con Python 3.6.9 e instale los paquetes en `requirements.txt`:

```bash 
$ conda create -n myenv python=3.6.9
```
Para posteriormente:
```bash
$ source activate myenv
$ pip install -r requirements.txt
```
Una vez acabado el proceso de instalación, se puede levantar el server en local.

```python
python app.py
```
Tras ejecutar este comando se levantará un servidor al que se puede acceder a través de la ruta:

```bash
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Levantando la página web en Heroku

[**Heroku**](https://dashboard.heroku.com/apps) es una Plataforma como servicio (PaaS) que nos abstrae de tratar con servidores, todo lo que tenemos que hacer es registrarnos, descargar algunas herramientas y luego cargar nuestro código en la plataforma sin esfuerzo.
### Instalando un servicio web llamado **gunicorn**

```bash 
$ pip install gunicorn
```
### Creamos un fichero `requirements.txt`

```bash 
$ pip freeze > requirements.txt
```
El cual ya está incluido en el actual repositorio.

### Creando un fichero `Procfile`

Debemos crear el fichero `Procfile` sin extensión y con la P mayúscula e incluir lo siguiente:

```bash 
web: gunicorn app:app
```
Aquí Heroku usa la web para iniciar un servidor web para la aplicación; `app:app` indica que el módulo y el nombre de la aplicación en nuestro caso.
Recomendamos hacer un fork del presente repo para posteriormente crear una app en Heroku.

### Creando una app en Heroku
Antes de crear una aplicación, hay que asegurarse de que su cuenta de GitHub esté conectada con la cuenta de Heroku. Conectamos con la cuenta de GitHub y desplegamos la rama `master`.

El servicio está actualmente disponible en la siguiente [url]().


## Tips de uso

* El número máximo de tweets se establece en `1000` y sólo un mes hacia atrás. Puede anular esta opción en el archivo `twitterdash/scraper.py`.
* Cambiar el `poolsize` en `twitterdash/scraper.py` afectará la velocidad de scrapping, pero también el rendimiento.
