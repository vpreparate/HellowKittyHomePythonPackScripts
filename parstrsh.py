import requests
from bs4 import BeautifulSoup
print("""			XX
		       X--X
		     XXXXXXXX
		     
		    X        X
		     XXXXXXXX
		    XX   X   X
		    XX   X   X
		    XXXXxXXXxx
		    XXXXXXXXXX
		     XXXXXXXX
		    XXXXXXXXXX
		   XXXXXXXXXXXX
		  XX XXXXXXXXX XX
		 XX  XXXXXXXXX  XX
		 X   XXXXXXXXX   X
		     XXXXXXXXX
		     XX     XX
		     XX     XX
		     XX     XX
		     XX     XX
		     XX     XX
		     XX     XX
		   xXXX     XXXx  """)
# Открыть файл с URL-адресами для парсинга
with open('rslt.txt', 'r', encoding='utf-8') as file_in:
    urls = file_in.readlines()

# Открыть файл для записи
with open('data.txt', 'w', encoding='utf-8') as file_out:
    # Пройти по всем URL-адресам из файла
    for url in urls:
        url = url.strip()

        # Отправить HTTP-запрос и получить содержимое страницы
        try:
            response = requests.get(url)
            print('site:', url)
        except Exception as e:
            print(e)
            continue

        # Создать объект BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Получить все теги <p> с текстом
        p_tags = soup.find_all('p')

        # Записать текст из тегов <p> в файл
        for p in p_tags:
            file_out.write(p.text.strip() + '\n')
