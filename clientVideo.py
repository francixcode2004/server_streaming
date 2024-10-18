# clienteVideo.py
'''
francisco lopez
alexandro mendoza
michael merino
bryan barrera
'''
import Pyro4
import cv2
import os
import base64

def reproducir_video(video_data, video_nombre):
    # Guarda el video temporalmente en el cliente para su reproducción
    video_path = f"temp_{video_nombre}"
    
    # Decodifica los datos base64 y escribe los datos binarios en un archivo
    with open(video_path, 'wb') as f:
        f.write(base64.b64decode(video_data))

    # Reproduce el video guardado
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"No se pudo abrir el video {video_nombre}.")
        return

    # Obtiene el fps (frames por segundo) del video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define el nombre de la ventana solo una vez
    ventana_nombre = "Reproducción de video"
    cv2.namedWindow(ventana_nombre, cv2.WINDOW_NORMAL)  # Se crea la ventana una vez
    
    # Reproduce el video cuadro por cuadro
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(ventana_nombre, frame)  # Muestra el video en la misma ventana

        # Calcula el tiempo de espera en milisegundos basado en el fps
        tiempo_espera = int(1000 / fps)  # Tiempo en milisegundos entre cuadros
        
        # Espera entre cuadros para controlar la velocidad de reproducción
        if cv2.waitKey(tiempo_espera) & 0xFF == ord('q'):
            break

    # Libera el objeto de video y cierra las ventanas correctamente
    cap.release()
    cv2.destroyWindow(ventana_nombre)
    os.remove(video_path)  # Borra el archivo temporal después de reproducirlo

# Conéctate al servidor Pyro y obtén la lista de videos
def main():
    while True:
        # Conecta con el servidor de videos
        video_server = Pyro4.Proxy("PYRONAME:streaminig.video_server")

        # Obtén la lista de videos disponibles en el servidor
        lista_videos = video_server.obtener_lista_videos()
        print("Videos disponibles:")
        print("0. Salir")
        for i, video in enumerate(lista_videos, 1):
            print(f"{i}. {video}")

        # Elige un video para reproducir
        opcion = int(input("Seleccione el número del video que desea reproducir: "))
        video_nombre = lista_videos[opcion - 1]
        if opcion==0:
            break
        # Solicita el video al servidor
        print(f"Solicitando video '{video_nombre}'...")
        video_data = video_server.leer_video(video_nombre)
        
        if isinstance(video_data, str):  # Si los datos son una cadena (base64 codificada)
            reproducir_video(video_data, video_nombre)
        else:
            print(video_data)  # Mensaje de error si no se pudo obtener el video

if __name__ == "__main__":
    main()
