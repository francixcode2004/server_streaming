# Video Streaming Server - README

## Descripción
Este proyecto implementa un servidor y un cliente para el streaming de videos usando Pyro4. El servidor proporciona una lista de videos que pueden ser solicitados por el cliente. El cliente puede seleccionar un video de la lista y reproducirlo en su máquina local.

### Autores
- Francisco López franciscoricardo293@gmail.com
- Alexandro Mendoza amendoza@est.ups.edu.ec
- Michael Merino maikijunior9@gmail.com
- Bryan Barrera  stivendp01@gmail.com

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes dependencias:

- Python 3.x
- Pyro4
- OpenCV
- Otros módulos de Python (que se instalarán automáticamente con los requisitos)

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install Pyro4 opencv-python
```

## Estructura del Proyecto

```
/project-root
├── serverVideo.py      # Código del servidor de video
├── clienteVideo.py     # Código del cliente de video
└── videos/             # Carpeta que contiene los videos (Asegúrate de agregar los videos aquí)
```

## Uso

### 1. Ejecutar el Servidor

El servidor de video debe ejecutarse primero. Para ello, navega a la carpeta donde se encuentra `serverVideo.py` y ejecuta el siguiente comando:

```bash
python serverVideo.py
```

Este servidor estará disponible para aceptar peticiones de los clientes. Asegúrate de que los videos estén en la carpeta `./videos` y que la lista de videos (`self.videos`) contenga nombres de archivo válidos.

### 2. Ejecutar el Cliente

Una vez que el servidor esté en funcionamiento, ejecuta el cliente en otra terminal o en otro dispositivo que tenga acceso al servidor. Para hacerlo, navega a la carpeta donde se encuentra `clienteVideo.py` y ejecuta el siguiente comando:

```bash
python clienteVideo.py
```

El cliente se conectará al servidor, mostrará la lista de videos disponibles y permitirá al usuario seleccionar un video para reproducir.

### Interfaz del Cliente

1. El cliente verá una lista de videos disponibles en el servidor.
2. Puede elegir un video ingresando el número correspondiente o salir eligiendo `0`.
3. Si elige un video, el cliente solicitará el video al servidor y lo reproducirá localmente utilizando OpenCV.
4. Si se selecciona un video inválido o hay un error, se mostrará un mensaje de error.

### 3. Detalles Técnicos

#### Servidor (`serverVideo.py`)

- El servidor usa Pyro4 para crear un daemon que espera conexiones.
- Los videos disponibles se encuentran en la lista `self.videos` y se almacenan en la carpeta `./videos`.
- El servidor ofrece dos métodos:
  - `obtener_lista_videos`: Devuelve la lista de videos disponibles.
  - `leer_video(video_nombre)`: Devuelve el video solicitado en formato base64 para su reproducción en el cliente.

#### Cliente (`clienteVideo.py`)

- El cliente se conecta al servidor utilizando Pyro4 y solicita la lista de videos.
- Después de elegir un video, el cliente solicita el video al servidor, decodifica los datos base64 y lo guarda temporalmente en su máquina.
- Usa OpenCV para reproducir el video guardado temporalmente.
- El cliente también elimina el archivo temporal después de la reproducción.

## Repositorio

Puedes encontrar el proyecto en GitHub:

[https://github.com/francixcode2004/server_streaming](https://github.com/francixcode2004/server_streaming)

## Notas

- Asegúrate de que el servidor y el cliente estén ejecutándose en la misma red o que el servidor sea accesible desde la máquina del cliente.
- Los videos deben estar en la carpeta `./videos` en el servidor con los nombres correctos.
- El cliente utiliza OpenCV para la reproducción de videos, por lo que el rendimiento puede depender del hardware y la red.

## Contribuciones

Si deseas contribuir, siéntete libre de hacer un fork del repositorio, realizar los cambios y enviar un pull request.

