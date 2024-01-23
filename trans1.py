# задаем русский алфавит в формате Unicode
ru_alphabet = u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

# задаем соответствующий каждой букве английский символ (транслитерационную таблицу)
en_translit = ['a', 'b', 'v', 'g', 'd', 'e', 'e', 'zh', 'z', 'i', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', "", 'y', "", 'ya', 'yu', 'e']

# открываем файл для чтения
with open("5000.txt", encoding="utf-8") as source_file:
    # читаем текст из файла
    source_text = source_file.read()
    
    # создаем пустой список для хранения транслитерированного текста
    translit_list = []

    # проходим по всем символам в исходном тексте
    for char in source_text:
        # если символ есть в русском алфавите, заменяем его на соответствующий английский символ
        if char in ru_alphabet:
            char_index = ru_alphabet.find(char)
            translit_char = en_translit[char_index]
            translit_list.append(translit_char)
        else:
            # если символ не найден в русском алфавите, оставляем его без изменений
            translit_list.append(char)

    # формируем транслитерированный текст
    translit_text = ''.join(translit_list)
    
    # выводим результат в консоль
    print(f"Transliterated string: {translit_text}")
    
    # сохраняем результат в файл
    with open("good.txt", mode="w", encoding="utf-8") as out_file:
        out_file.write(translit_text)
    
    # выводим сообщение об окончании работы
    print("Done!")
