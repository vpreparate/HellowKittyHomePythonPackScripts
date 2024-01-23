import tkinter as tk
from tkinter import filedialog  # Импорт модуля для диалоговых окон файловой системы

def open_file():
    file_path = filedialog.askopenfilename()  # Открытие диалогового окна для выбора файла для открытия
    with open(file_path, 'r') as file:  # Открытие выбранного файла для чтения
        text = file.read()  # Чтение текста из файла
        text_box.delete("1.0", "end")  # Очистка текстового поля
        text_box.insert("1.0", text)  # Вставка текста из файла в текстовое поле

def save_file():
    text = text_box.get("1.0", "end-1c")  # Получение текста из текстового поля
    # Открытие диалогового окна для выбора файла для сохранения результатов
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")  
    with open(file_path, 'w') as file:  # Открытие выбранного файла для записи
        file.write(text)  # Запись текста в файл

def replace_text():
    search_text = entry_search.get()  # Получение текста для поиска
    replace_text = entry_replace.get()  # Получение текста для замены
    text = text_box.get("1.0", "end-1c")  # Получение текста из текстового поля
    new_text = text.replace(search_text, replace_text)  # Замена текста
    text_box.delete("1.0", "end")  # Очистка текстового поля
    text_box.insert("1.0", new_text)  # Вставка измененного текста в текстовое поле

root = tk.Tk()  # Создание главного окна приложения
root.title("Text Replacement")  # Установка заголовка окна

label_search = tk.Label(root, text="Найти :")  # Создание метки для текстового поля "Найти"
label_search.pack()  # Размещение метки на форме

entry_search = tk.Entry(root)  # Создание текстового поля для ввода текста для поиска
entry_search.pack()  # Размещение текстового поля на форме

label_replace = tk.Label(root, text="Заменить на:")  # Создание метки для текстового поля "Заменить на"
label_replace.pack()  # Размещение метки на форме

entry_replace = tk.Entry(root)  # Создание текстового поля для ввода текста для замены
entry_replace.pack()  # Размещение текстового поля на форме

button_replace = tk.Button(root, text="Заменить", command=replace_text)  # Создание кнопки для выполнения замены
button_replace.pack()  # Размещение кнопки на форме

button_open = tk.Button(root, text="Открыть файл", command=open_file)  # Создание кнопки для открытия файла
button_open.pack()  # Размещение кнопки на форме

button_save = tk.Button(root, text="Сохранить файл", command=save_file)  # Создание кнопки для сохранения файла
button_save.pack()  # Размещение кнопки на форме

text_box = tk.Text(root)  # Создание текстового поля для отображения и редактирования текста
text_box.pack()  # Размещение текстового поля на форме

root.mainloop()  # Отображение окна и запуск главного цикла обработки событий
