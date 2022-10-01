import create_id as id
import short_db as sbd
def fs_name():
    s_name = input('Введите фамилию').lower().title()
    return s_name

def f_number():
    number = int(input('Введите номер телефона'))
    return number
def count():
    count = id.create_id()

    return count
    # f_name = input('Введите имя').lower().title()
    # patronymic = input('Введите отчество')
    # location = input('Введите адрес').lower().title()

    # activity = input('Введите описание').lower().title()

