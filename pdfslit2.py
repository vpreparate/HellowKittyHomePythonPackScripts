import os
from PIL import Image  #pip install pillow
from reportlab.lib.pagesizes import letter # pip install reportlab
from reportlab.pdfgen import canvas

def images_to_one_pdf(input_folder, output_file):
    # Создаем пустой PDF файл
    c = canvas.Canvas(output_file, pagesize=letter)

    # Проходим по всем файлам входной папки
    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # Открываем изображение
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Получаем размеры изображения
            width, height = img.size

            # Добавляем страницу в PDF файл
            c.setPageSize((width, height))
            c.drawImage(img_path, 0, 0, width, height)  # Вставляем изображение на текущую страницу PDF
            c.showPage()  # Переходим к следующей странице

    # Завершаем создание PDF файла
    c.save()

if __name__ == "__main__":
    input_folder = input("Введите путь к папке с изображениями: ")
    output_file = input("Введите путь для сохранения PDF файла c именем самого файла\n в формате папка/файл.pdf: ")

    images_to_one_pdf(input_folder, output_file)
