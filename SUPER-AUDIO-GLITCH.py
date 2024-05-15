from moviepy.editor import VideoFileClip, concatenate_videoclips
import random

def glitch_effect(video_path, output_path):
    clip = VideoFileClip(video_path)
    clips = []
    current_time = 0
    duration = clip.duration

    while current_time < duration:
        next_time = current_time + random.uniform(2, 6)
        if next_time > duration:
            clips.append(clip.subclip(current_time, duration))
            break

        skip_ahead = random.uniform(0.2, 0.8)
        skip_time = current_time + skip_ahead if current_time + skip_ahead < duration else duration

        # Добавляем фрагмент от текущего времени до точки заикания
        clips.append(clip.subclip(current_time, skip_time))

        # Добавляем фрагмент с заиканием (перемещением вперед или назад)
        jump_back = random.choice([True, False])
        if jump_back:
            start_time = max(0, current_time - skip_ahead)
        else:
            start_time = min(duration, current_time + skip_ahead)
        end_time = start_time + skip_ahead
        clips.append(clip.subclip(start_time, end_time))

        # Возвращаемся к точке заикания и продолжаем
        current_time = skip_time

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Используй функцию так:
glitch_effect('1.mp4', 'glitch.mp4')
