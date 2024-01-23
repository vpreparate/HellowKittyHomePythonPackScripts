import os  #для работы с операционной системой
from moviepy.editor import *  #для обработки видеофайлов
from PIL import Image  #для работы с изображениями
# Параметры
audio_path = '1.mp3'  # Замени на реальный путь к музыкальному файлу
image_dir = '05.2022'  # Замени на путь к папке с картинками
output_video = 'magic_video.mp4'  # Название твоего будущего клипа
duration_per_image = 0.3  # Сколько секунд будет показываться каждая картинка
#изменяет размер и центрирует изображение
def resize_image(image_path, size):
    with Image.open(image_path) as img:
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(
            img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
        )
        return background


# Получаем список картинок
image_files = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('.jpg', '.jpeg', '.png'))]
resized_images = []
#Изменяем размер каждого изображения, сохраняем их в новый список resized_images
for i, image_file in enumerate(image_files):
        resized_image = resize_image(image_file, (1024, 768))
        resized_image_path = os.path.join(image_dir, f"resized_{i}.png")
        resized_image.save(resized_image_path, format="png")
        resized_images.append(resized_image_path)
# Получаем длительность аудио
audio_clip = AudioFileClip(audio_path)
audio_duration = audio_clip.duration

# Проверяем, чтобы суммарная длительность показа всех изображений была не меньше,
#чем длительность аудиофайла. Если она меньше,
#увеличиваем количество повторов видеоклипов
final_clips = []
for img_path in resized_images:
    img_clip = ImageClip(img_path).set_duration(duration_per_image)
    final_clips.append(img_clip)

# Убедимся, что картинки будут показываться весь аудиотрек
total_image_duration = duration_per_image * len(image_files)
if total_image_duration < audio_duration:
    repeat_factor = audio_duration // total_image_duration + 1
    repeat_factor = int(repeat_factor)
    final_clips = final_clips * repeat_factor

# Обрезаем, если последний повтор слишком длинный
final_clips = concatenate_videoclips(final_clips).set_duration(audio_duration)

#Ресайзим картинки под один размер (высокое разрешение, например 1080p)
#в два раза усложняет работу скрипта
#final_clips = final_clips.resize(newsize=(1920, 1080))

# Добавляем аудио
final_video = final_clips.set_audio(audio_clip)

# Экспортируем видео
final_video.write_videofile(output_video, codec='libx264', audio_codec='aac', fps=24)
# Удалим временные картинки
for img in resized_images:
        os.remove(img)
