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
    with open(f'{count}.json', 'a', encoding='utf8') as file:
        file.write(json.dumps(person_dict, ensure_ascii=False))

    return person_dict.get('Second name')