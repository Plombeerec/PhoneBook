import create_id as id
import add_to_db as adb

def create_sdb():
    with open('phonebook.txt', 'a', encoding="utf-8") as pb:
        pb.write(f'{id.create_id()} {adb.person()}\n')