import check as check
import json


def person():
    '''
    Создаем отдельный .json файл для каждой новой записи.
    :return:
    '''
    s_name = input('Введите фамилию').lower().title()
    # f_name = input('Введите имя').lower().title()
    # patronymic = input('Введите отчество')
    # location = input('Введите адрес').lower().title()
    number = int(input('Введите номер телефона'))
    # activity = input('Введите описание').lower().title()
    count = 1





    '''
    создаем краткий справочника id, фамилия, который поможет в создании id
    '''
    try:
        with open('phonebook.txt', 'r', encoding="utf-8") as pb:
            phonebook_dict = {}
            for line in pb:
                key, value = line.split()
                phonebook_dict[key] = value.rstrip('')
                if key in phonebook_dict.keys():
                    key = int(key)
                    key +=1
                    count+=1
        with open('phonebook.txt', 'a', encoding="utf-8") as pb:
            pb.write(f'{count} {s_name}\n')

    except:
        with open('phonebook.txt', 'a', encoding="utf-8") as pb:
            pb.write(f'{count} {s_name}\n')




    person_dict = {'ID': count, 'Second name': s_name,
                   }  # 'First_name': f_name, 'Phone number': number, "Patromymic" : patronymic,
    # 'Location': location,
    # 'Activity': activity}
    with open(f'{count}.json', 'a', encoding= 'utf8') as file:
        file.write(json.dumps(person_dict, ensure_ascii=False))






    #
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




