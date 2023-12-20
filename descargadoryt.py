from pytube import YouTube
import os 

def descargar_video(url, output_path):
    try:
        yt = YouTube(url)
        print(f"Descargando video: {yt.title}...")
        yt.streams.get_highest_resolution().download(output_path=output_path)
        print(f"{yt.title} descargado exitosamente!")
    except Exception as e:
        print(f"No se ha descargado el video: {str(e)}")

def main():
    url = input("Introduce la URL del video de YouTube: ")
    project_directory = os.path.dirname(os.path.abspath(__file__))  # Corregir "__file__" con dos guiones bajos al principio y final
    output_path = os.path.join(project_directory, 'descargas')

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    print(f"El directorio del proyecto es: {project_directory}")
    print(f"Los archivos se guardan en: {output_path}")

    descargar_video(url, output_path)

if __name__ == "__main__":  # Corregir "__main__" con dos guiones bajos al principio y final
    main()