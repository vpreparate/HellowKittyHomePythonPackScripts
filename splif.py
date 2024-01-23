import os
import random
from pydub import AudioSegment

# Подмигиваю 😉 и начинаю творить магию кода для тебя, солнышко!

# Путь к твоей директории с музыкой
music_dir = 'oMRandom2017'

# Получаем список всех mp3 файлов в директории
mp3_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

# Выбираем случайные 100 треков
selected_tracks = random.sample(mp3_files, 100)
print(selected_tracks)
# Первый трек, который будет основой для микса
final_mix = AudioSegment.from_file(os.path.join(music_dir, selected_tracks[0]))
print("Соединение выполняется")
# Соединяем остальные 99 треков с первым
for track in selected_tracks[1:]:
    track_path = os.path.join(music_dir, track)
    current_track = AudioSegment.from_file(track_path)
    final_mix += current_track

# Экспортируем наш уникальный микс в файл
final_mix.export("final_mix.mp3", format="mp3")

print("Готово, дорогой! Теперь у тебя есть суперский микс из 100 треков! 💃🕺")
