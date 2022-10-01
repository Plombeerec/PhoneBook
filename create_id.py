import add_to_db as adb


def create_id():
    '''
    Функция формирует ID строки. При первом запуске создает файл phonebook.txt в котором
    построчно отображается ID и фамилия, для упрощения поиска. Возможно, вместо файла .txt можно
    использовать .json файл, но, это сложнее, на мой взгялд.
    :return: ID, создает phonebook.txt при первом запуске.
    '''
    id_count = 1
    try:
        with open('phonebook.txt', 'r', encoding="utf-8") as pb:
            phonebook_dict = {}
            for line in pb:
                key, value = line.split()
                phonebook_dict[key] = value.rstrip('')
                if key in phonebook_dict.keys():
                    key = int(key)
                    key += 1
                    id_count += 1
    except:
        id_count =1
        with open('phonebook.txt', 'a', encoding="utf-8") as pb:
            pb.write(f'{id_count} {adb.person()}\n')

    return id_count
