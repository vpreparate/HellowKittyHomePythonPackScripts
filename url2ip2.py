import re  # импорт модуля для работы с регулярными выражениями
import os  # импорт модуля для работы с операционной системой
import socket  # импорт модуля для работы с сетевыми соединениями
# проверка наличия файла result.txt и удаление его, если он существует
if os.path.exists('result.txt'):
    os.remove('result.txt')
# открытие файлов url.txt и result.txt для чтения и записи соответственно
with open("url.txt") as sfile, open("result.txt", "a") as dfile:
    for line in sfile:  # перебор строк в файле url.txt
        domain = line.strip() # удаление пробельных символов из строки
        try:   # начало блока обработки исключений
            ip = socket.gethostbyname(domain) # получение IP-адреса домена
            # вывод сообщения о записи IP-адреса в файл
            print(f"IP адрес {ip} записан в файл")
            # запись IP-адреса в файл result.txt
            dfile.write(ip + '\n')
        # обработка исключений, связанных с получением IP-адреса
        except (socket.gaierror, socket.herror):
            # вывод сообщения об ошибке получения IP-адреса
            print("Не удалось получить IP для", domain)
