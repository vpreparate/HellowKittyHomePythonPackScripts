from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

#имитируем браузер
ua = UserAgent()
# Создает экземпляр класса UserAgent из библиотеки fake-useragent.
#Этот класс позволяет генерировать поддельные строки User-Agent, которые представляют собой строки,
#идентифицирующие браузер и операционную систему, используемые для доступа к веб-сайту.
headers = {  
    'User-Agent': ua.random,  
    'Accept-Language': 'en-US,en;q=0.5'
}
#Создает словарь headers, который содержит заголовки, которые будут отправляться вместе с запросами HTTP.
#устанавливает случайную строку User-Agent с помощью атрибута random экземпляра ua.
#Это делается для имитации использования реального браузера и предотвращения обнаружения бота.
#указывает, что клиент принимает ответы на английском языке (США) в первую очередь,
#а на английском языке в целом – в качестве второй приоритетной опции.


# Функция для скачивания файла с отображением прогресса
def download_file(url): # download_file с одним параметром – url (адрес файла для загрузки)
    response = requests.get(url, stream=True)
    #Использует библиотеку requests для отправки GET-запроса по указанному url.
    #Опция stream=True позволяет загружать файл постепенно, блок за блоком.
    total_size = int(response.headers.get('content-length', 0))
    #Получает общий размер файла (в байтах) из заголовков ответа сервера.
    #Если заголовок content-length отсутствует, устанавливает значение по умолчанию 0.
    block_size = 1024
    # Определяет размер блока для загрузки, равный 1024 байтам (1 КБ).
    with open(url.split('/')[-1], 'wb') as file:
        #Открывает файл для записи в двоичном режиме с именем,
        #полученным из последнего сегмента url (обычно это имя файла).
        for data in tqdm(response.iter_content(block_size), total=total_size//block_size, unit='KB', unit_scale=True):
            #Использует библиотеку tqdm для отображения индикатора выполнения загрузки.
            #response.iter_content(block_size) возвращает итератор, который считывает данные файла блоками.
            #total=total_size//block_size устанавливает общий прогресс в килобайтах,
            #unit='KB' задает единицу измерения,
            #а unit_scale=True включает масштабирование единиц (например, от МБ до ГБ).
            file.write(data)
            #Записывает загруженные данные в открытый файл.

# Начальная страница
page_num = 12
page_info = 1

while page_num < 1464:
    print(f'******Страница {page_info}***********') #Вывод страницы которую обходит
    url = f'https://nasms.ru/category/trap_{page_num}_date.html' #адрес страницы на которой ищет песни
    response = requests.get(url, headers=headers) #подключается к сайту и передаёт хэдэры
    soup = BeautifulSoup(response.content, 'html.parser') #анализирует полученую страницу
    
    elements = soup.find_all('div', class_='tracks_item_doc')  # ищет все элементы с классом 'tracks_item_doc'
    
    for element in elements: #для каждого найденого элемента выполняется цикл
        perehod = element.find_all('a') #ищет ссылку для перехода по песне
        download_link = perehod[0]['href'] #выдёргивает путь
        download_url = f'https://nasms.ru{download_link}' #подставляет путь к сайту
        print(f'переход на скачивание {download_url}') #выводит полученый урл
        
        # Переход по ссылке с классом 'tracks_item_doc' для обновления страницы
        response = requests.get(download_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        elements2 = soup.find('div', class_='iftrack_download') #ищет все элементы с классом 'iftrack_download'
        
        download_link2 = elements2.find('a')['href'] #получает адрес нахождения файла
        
        if download_link2.endswith('.mp3'): #если файл заканчивается на .mp3
        	print(f'Downloading {download_link2}') #говорит что будет его скидывать
        	download_file(download_link2) #запускает функцию скачивания файла передавая его адрес
    
    # Переход на следующую страницу
    page_num += 12
    page_info += 1
