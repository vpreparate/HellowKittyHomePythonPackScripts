import os
import random
from pydub import AudioSegment

def split_song(song_path, output_folder, segment_durations):
    # Загрузка песни
    song = AudioSegment.from_file(song_path)

    # Создание папки для отрывков, если она не существует
    os.makedirs(output_folder, exist_ok=True)

    # Получение продолжительности песни
    song_duration = len(song)

    # Разделение песни на отрывки случайной продолжительности
    i = 1
    while song_duration > 0:
        # Выбор случайной продолжительности отрывка из списка
        duration = random.choice(segment_durations)

        # Убедитесь, что продолжительность отрывка не превышает продолжительность оставшейся песни
        if duration > song_duration:
            duration = song_duration

        # Получение отрывка из песни
        segment = song[:duration]

        # Обновление продолжительности оставшейся песни
        song = song[duration:]

        # Создание имени файла для отрывка
        segment_name = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(song_path))[0]}_{i}_{duration//1000}sec.mp3")

        # Сохранение отрывка в отдельный файл
        segment.export(segment_name, format="mp3")
        print(f"Отрывок {i} ({duration//1000} секунд) сохранен")

        # Обновление продолжительности оставшейся песни
        song_duration = len(song)

        # Увеличение счетчика отрывков
        i += 1

songs_folder = "new"
output_folder = "cuts"
segment_durations = [20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000]

for file_name in os.listdir(songs_folder):
    if file_name.endswith(".mp3") or file_name.endswith(".wav"):
        song_path = os.path.join(songs_folder, file_name)
        split_song(song_path, output_folder, segment_durations)
