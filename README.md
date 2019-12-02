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

## Tips de uso

* El número máximo de tweets se establece en `1000` y sólo un mes hacia atrás. Puede anular esta opción en el archivo `twitterdash/scraper.py`.
* Cambiar el `poolsize` en `twitterdash/scraper.py` afectará la velocidad de scrapping, pero también el rendimiento.

## LICENSE
This is free and unencumbered software released into the public domain.
Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.
In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.