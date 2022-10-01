import input as inp
import add_to_db as adb
import short_db as sdb

def create_id():
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
            pb.write(f'{id_count} {inp.fs_name()}\n')


    print(f'{id_count} is id')
    return id_count
