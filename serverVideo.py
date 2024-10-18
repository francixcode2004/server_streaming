# serverVideo.py
'''
francisco lopez
alexandro mendoza
michael merino
bryan barrera
'''
import Pyro4
import os
import base64

@Pyro4.expose
class VideoServer(object):
    def __init__(self):
        self.videos = ['eldiablo.mp4', 'elgallo.mp4', 'elhombre.mp4', 'messirve.mp4']
        self.video_directory = "./videos"  # Asegúrate de que los videos estén en este directorio

    def obtener_lista_videos(self):
        # Devuelve la lista de videos disponibles
        return self.videos

    def leer_video(self, video_nombre):
        # Verifica si el video está en la lista y existe en el directorio
        if video_nombre in self.videos:
            video_path = os.path.join(self.video_directory, video_nombre)
            if os.path.exists(video_path):
                # Codifica los datos binarios del video en base64
                with open(video_path, 'rb') as f:
                    video_data = f.read()
                video_base64 = base64.b64encode(video_data).decode('utf-8')  # Codifica a base64 y convierte a string
                return video_base64
            else:
                return "Error: El archivo de video no se encuentra en el servidor."
        else:
            return "Error: Video no encontrado en la lista de disponibles."

# Creación del servidor Pyro
daemon = Pyro4.Daemon()  # Crea el daemon para el servidor Pyro
ns = Pyro4.locateNS()  # Encuentra el nombre del servidor
uri = daemon.register(VideoServer)  # Registra el servidor
ns.register("streaminig.video_server", uri)  # Lo registra en el NameServer

print("Servidor de video listo.")
daemon.requestLoop()  # Inicia el bucle de espera por peticiones
