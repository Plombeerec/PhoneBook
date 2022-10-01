import logger as log
import check as ch
import add_to_db as adb
import short_db as sdb


def button_click():
    ver = ch.const()

    if ver == 0:
        print('Программа отменена')
        log.log_exit()
        exit()
    elif ver == 1:
        person = adb.person()
        print(f'Added completed')

    return sdb.create_sdb()



#
# button_click()