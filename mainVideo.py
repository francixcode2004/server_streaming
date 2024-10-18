import yt_dlp
import cv2
import os

def descargar_video(url):
    opciones = {
        'format': 'best',  # Mejor calidad disponible
        'outtmpl': 'video_descargado.mp4'  # Nombre del archivo descargado
    }
    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("Video descargado correctamente.")
    except Exception as e:
        print(f"Hubo un error al intentar descargar el video: {e}")

def reproducir_video(video_path):
    # Verifica si el archivo existe
    if not os.path.exists(video_path):
        print("El archivo de video no existe.")
        return
    
    # Abre el archivo de video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error al abrir el archivo de video.")
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

def main():
    url = input("Introduce la URL del video: ")
    descargar_video(url)
    
    # Reproducir el video descargado
    reproducir_video('video_descargado.mp4')

if __name__ == "__main__":
    main()
