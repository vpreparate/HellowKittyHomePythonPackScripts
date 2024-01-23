# Комментарий: Открываем файл "urls.txt" для чтения
with open("urls.txt", "r") as f:
    filename = input("Enter filename: ")  # Запрашиваем у пользователя название файла
    lines_limit = 100  # Устанавливаем лимит строк в 100
    k = 1  # Инициализируем счетчик
    text = []  # Создаем пустой список для текста
    for i, line in enumerate(f):  # Итерируем по строкам в файле
        text.append(line)  # Добавляем строку в список
        if i % lines_limit == lines_limit - 1:  # Проверяем, достигли ли лимита строк
            with open(f"{filename.split('.')[0]}_{k}.txt", "w") as f_out:  # Открываем файл для записи
                f_out.write("".join(text))  # Записываем текст из списка в файл
                text.clear()  # Очищаем список
                k += 1  # Увеличиваем счетчик
    if text:  # Проверяем, остались ли строки в списке
        with open(f"{filename.split('.')[0]}_{k}.txt", "w") as f_out:  # Открываем файл для записи
            f_out.write("".join(text))  # Записываем оставшийся текст из списка в файл
