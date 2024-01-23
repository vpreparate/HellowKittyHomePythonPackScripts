import os
import random

# Путь к директории с файлами
path = "speech"

# Получаем список файлов в директории
files = os.listdir(path)

# Переименовываем файлы
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        filename, file_extension = os.path.splitext(file)
        if file_extension:  # Проверяем, что это файл с расширением
            random_numbers = f"{random.randint(100, 999)}-{random.randint(1000, 9999)}-{random.randint(100000, 999999)}"
            new_filename = f"{random_numbers}{file_extension}"
            os.rename(os.path.join(path, file), os.path.join(path, new_filename))
            print(f"Файл {file} переименован в {new_filename}")
