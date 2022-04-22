# API DAMN Server

API DAMN Server tiene como utilidad la búsqueda y opcionalmente la descarga de contenido de audio, inicialmente desde la plataforma *Youtube* a través de **youtube_dl**

## Dependencias
```
pip install flask youtube_dl
```

## Uso

Para ejecutar el servidor use
```
python __main__.py
```

***Utilizando postman o insomnia***

La API se ejecuta en http://localhost:4000

Para obtener una respuesta de búsqueda de algún video de youtube se usa la siguiente ruta.
```
/search/<Lo que quiera buscar>
```
La API devuelve un JSON con 10 resultados de búsqueda que incluyen titulo, url y vista previa.

Por ejemplo si deseamos buscar a *The Weeknd* la ruta completa quedaría así.

```
http://localhost:4000/search/The Weeknd
```

Y el resultado es el siguiente:
```json
{
	"results": [
		{
			"thumbnailURL": "https://i.ytimg.com/vi/2fDzCWNS3ig/hqdefault.jpg",
			"title": "The Weeknd - Out of Time (Official Video)",
			"url": "https://www.youtube.com/watch?v=2fDzCWNS3ig"
		},
		{
			"thumbnailURL": "https://i.ytimg.com/vi/XXYlFuWEuKI/hqdefault.jpg",
			"title": "The Weeknd - Save Your Tears (Official Music Video)",
			"url": "https://www.youtube.com/watch?v=XXYlFuWEuKI"
		},
		{
			"thumbnailURL": "https://i.ytimg.com/vi/waU75jdUnYw/hqdefault.jpg",
			"title": "The Weeknd - Earned It (from Fifty Shades Of Grey) (Official Video - Explicit)",
			"url": "https://www.youtube.com/watch?v=waU75jdUnYw"
		},
		{
			"thumbnailURL": "https://i.ytimg.com/vi/VafTMsrnSTU/hqdefault.jpg",
			"title": "The Weeknd - Sacrifice (Official Music Video)",
			"url": "https://www.youtube.com/watch?v=VafTMsrnSTU"
		},
		{
			"thumbnailURL": "https://i.ytimg.com/vi/4NRXx6U8ABQ/hqdefault.jpg",
			"title": "The Weeknd - Blinding Lights (Official Video)",
			"url": "https://www.youtube.com/watch?v=4NRXx6U8ABQ"
		},
		{
			"thumbnailURL": "https://i.ytimg.com/vi/yzTuBuRdAyA/hqdefault.jpg",
			"title": "The Weeknd - The Hills (Official Video)",
			"url": "https://www.youtube.com/watch?v=yzTuBuRdAyA"
		},
		{
			"thumbnailURL": "https://i.ytimg.com/vi/hWlYEaxubRY/hqdefault.jpg",
			"title": "The Weeknd - 103.5 DAWN FM",
			"url": "https://www.youtube.com/watch?v=hWlYEaxubRY"
		},
		{
			"thumbnailURL": "https://i.ytimg.com/vi/zuUNNu3z5Uk/hqdefault.jpg",
			"title": "The Weeknd, KAYTRANADA - Out of Time (KAYTRANADA Remix / Audio)",
			"url": "https://www.youtube.com/watch?v=zuUNNu3z5Uk"
		},
		{
			"thumbnailURL": "https://i.ytimg.com/vi/M4ZoCHID9GI/hqdefault.jpg",
			"title": "The Weeknd - Call Out My Name (Official Video)",
			"url": "https://www.youtube.com/watch?v=M4ZoCHID9GI"
		},
		{
			"thumbnailURL": "https://i.ytimg.com/vi/KEI4qSrkPAs/hqdefault.jpg",
			"title": "The Weeknd - Can&#39;t Feel My Face (Official Video)",
			"url": "https://www.youtube.com/watch?v=KEI4qSrkPAs"
		}
	]
```

Opcionalmente puede descargar el audio que desee...

Mediante el método POST en la ruta
```
/download
```

Envié un JSON con el titulo y el url del video que desee descargar. De ésta forma (sin los corchetes, claro):
```json
{
    "title": "<titulo>",
    "link": "<url>"
}
```

**Y la API descargará en el servidor el archivo de audio y posteriormente transferirá los bytes del archivo hacia la respuesta al cliente en un JSON con la siguiente estructura**


```json
{
    "file": {
        "<bytes>",
        "<title>"
    }
    "message": "File Transfer"
}
```

## Herramientas usadas.

![Lenguaje](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Libreria](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Plataforma](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)


*La API es con fines educativos y demostrativos para un proyecto escolar, no nos hacemos responsables de cualquier tipo de mal uso para el que pueda usarse.