import os
from PIL import Image # pip install pillow
from reportlab.lib.pagesizes import letter # pip install reportlab
from reportlab.pdfgen import canvas

def convert_images_to_pdf(input_folder, output_folder):
    # Создаем выходную папку, если ее нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Проходим по всем файлам входной папки
    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # Открываем изображение
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Создаем PDF файл для текущего изображения
            pdf_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")
            c = canvas.Canvas(pdf_path, pagesize=img.size)

            # Вставляем изображение на страницу PDF
            c.drawImage(img_path, 0, 0, img.size[0], img.size[1])

            # Завершаем создание PDF файла
            c.save()

if __name__ == "__main__":
    input_folder = input("Введите путь к папке с изображениями: ")
    output_folder = input("Введите путь к папке для сохранения PDF файлов: ")

    convert_images_to_pdf(input_folder, output_folder)
