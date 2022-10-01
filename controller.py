import logger as log
import check as ch
import short_db as sdb


def button_click():
    ver = ch.const()

    if ver == 0:
        print('Программа отменена')
        log.log_exit()
        exit()
    elif ver == 1:
        sdb.create_sdb()
        print(f'Added completed')
    elif ver ==2:
        '''запуск режима чтения из БД'''
        pass




