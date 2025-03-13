import os
import subprocess

input_directory = 'PICT'  # Директория входящих GIF
output_directory = 'anim'  # Директория для выходящих WEBM файлов
max_size_kb = 256  # Максимальный размер файла в килобайтах
canvas_size = (512, 512)  # Размер для стикеров 512x512
animation_length = 3  # Максимальная длительность анимации (в секундах)
fps = 30  # Частота кадров

# Создаем выходную директорию, если её нет
os.makedirs(output_directory, exist_ok=True)

def convert_gif_to_webm(gif_path, output_path):
    """Конвертация GIF в WEBM с использованием ffmpeg."""
    command = [
        "ffmpeg",
        "-i", gif_path,  # Входящий GIF файл
        "-vf", f"scale={canvas_size[0]}:{canvas_size[1]},fps={fps}",  # Изменить размер и частоту кадров
        "-t", str(animation_length),  # Ограничить длительность
        "-an",  # Убедиться, что звуковая дорожка отсутствует
        "-c:v", "libvpx-vp9",  # Использование кодека VP9
        "-b:v", "150k",  # Устанавливаем битрейт
        output_path  # Путь для увеличенного файла
    ]
    
    print(f'Запускаем команду: {" ".join(command)}')
    subprocess.run(command, check=True)

def optimize_file_size(output_path):
    """Проверка и оптимизация размера файла, если он превышает лимит."""
    if os.path.getsize(output_path) > max_size_kb * 1024:
        print(f'Файл {output_path} превышает 256 KB. Оптимизация...')
        command = [
            "ffmpeg",
            "-i", output_path,
            "-c:v", "libvpx-vp9",
            "-b:v", "100k",  # Уменьшить битрейт для оптимизации
            "-an",
            output_path
        ]
        subprocess.run(command, check=True)

# Основной процесс конвертации 
for root, dirs, files in os.walk(input_directory):
    for file in files:
        if file.lower().endswith('.gif'):
            gif_path = os.path.join(root, file)
            output_file = os.path.splitext(file)[0] + '.webm'
            output_path = os.path.join(output_directory, output_file)

            print(f'Конвертируем: {gif_path} -> {output_path}...')
            convert_gif_to_webm(gif_path, output_path)
            optimize_file_size(output_path)

print('Конвертация завершена!')
