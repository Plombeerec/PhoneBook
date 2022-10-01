import create_id as id
import input as inp
import short_db as sdb
import json


def person():
    '''
    Создаем отдельный .json файл для каждой новой записи.
    :return:
    '''
    count = id.create_id()
    person_dict = {'ID': count, 'Second name': inp.fs_name(), 'Phone number': inp.f_number()}
    # 'First_name': f_name, 'Phone number': number, "Patronymic" : patronymic,
    # 'Location': location,
    # 'Activity': activity}
    with open(f'{count}', 'a', encoding='utf8') as file:
        file.write(json.dumps(person_dict, ensure_ascii=False))



    return person_dict.get('Second name')









    # with open('PhoneBook.json', 'r', encoding= 'utf8') as PB:
    #     templates = json.load(PB)
    #
    #     for id, lastname in templates.items():
    #         print(id,lastname)
    #
    #         person_string = ':'.join(map(str,[int(count), s_name]))
    #         print(person_string)
    #         templates[str(count)] = s_name
    #         print(templates)
    #
    #
    # with open('PhoneBook.json', 'a', encoding='utf8') as PB:
    #     file.write(json.dumps(templates, ensure_ascii=False))
