import os
from moviepy import VideoFileClip

def split_video_by_size(input_file, max_size_mb):
    # Configurações
    max_size_bytes = max_size_mb * 1024 * 1024  # Tamanho máximo em bytes
    output_folder = "output_segments"
    os.makedirs(output_folder, exist_ok=True)

    # Carregar o vídeo
    clip = VideoFileClip(input_file)
    duration = clip.duration

    # Estimar o tamanho médio por segundo do vídeo
    estimated_bitrate = (max_size_bytes * 8) / duration  # Bitrate em bits por segundo
    estimated_size_per_second = estimated_bitrate / 8  # Tamanho por segundo em bytes
    segment_duration = max_size_bytes / estimated_size_per_second  # Duração máxima por segmento

    print(f"Bitrate estimado: {estimated_bitrate / 1000:.2f} kbps")
    print(f"Duração estimada por segmento: {segment_duration:.2f} segundos")

    # Dividir o vídeo em segmentos
    start = 0
    part = 1
    while start < duration:
        end = min(start + segment_duration, duration)
        segment = clip.subclipped(start, end)

        # Definir nome do arquivo de saída
        output_file = os.path.join(output_folder, f"segment_{part}.mp4")

        # Exportar o segmento
        segment.write_videofile(
            output_file,
            codec="libx264",
            audio_codec="aac",
            bitrate=f"{int(estimated_bitrate)}k",
            preset="ultrafast",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
            threads=8,
        )

        print(f"Segmento {part} salvo: {output_file}")
        start = end
        part += 1

    clip.close()
    print("Divisão concluída!")

# Solicitar o caminho do vídeo e o tamanho máximo por segmento
video_file = input("Path do vídeo: ")
max_size_mb = input("Tamanho máximo em megabytes por segmento (padrão: 10 MB): ")

if max_size_mb:
    max_size_mb = float(max_size_mb)
else:
    max_size_mb = 10  # Tamanho padrão de 10 MB

split_video_by_size(video_file, max_size_mb)
