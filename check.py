import logger as log



def const():
    ver = check_regime('\nКакие едйствия вы желаете предпринять?\n0 - закрыть программу;'
                          '\n1 - записать в справочник;\n2 - открыть в режиме чтения;\nВвод ')
    return ver

def check_regime(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            if number in [0, 1, 2]:
                is_OK = True
            else:
                print("Определитесь с режимом работы приложения. 0 - закрыть программу; "
                      "1 - запись в справочник; 2 - чтение справочника")
                log.log_error('Некорректный ввод режима работы (некорректная цифра)')
        except ValueError:
            print("Некорректный ввод. Повторите попытку")
            log.log_error('Некорректный ввод режима работы (введена не цифра)')
    return number


def check_input_string(text):
    pass

def check_number():
    pass


