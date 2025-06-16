# controller.py

from model import PhoneBook
from view import *
from exceptions import *


class PhoneBookController:
    def __init__(self):
        self.phonebook = PhoneBook()
        self.changed = False
        try:
            self.phonebook.load_contacts()
        except FileReadError as e:
            show_error(e)

    def run(self):
        while True:
            choice = show_menu()

            match choice:
                case "1":
                    show_all_contacts(self.phonebook.get_all_contacts())
                case "2":
                    try:
                        name, phone, comment = input_contact_data()
                        self.phonebook.add_contact(name, phone, comment)
                        self.changed = True
                        print("Контакт успешно добавлен.")
                    except InvalidContactDataError as e:
                        show_error(e)
                case "3":
                    query = input_search_query()
                    results = self.phonebook.find_contacts(query)
                    if results:
                        print(f"Найдено {len(results)} совпадений:")
                        show_all_contacts(results)
                    else:
                        print("Контактов не найдено.")
                case "4":
                    try:
                        contact_id = input_contact_id()
                        name = input(f"Имя [{self.phonebook.contacts[contact_id - 1].name}]: ")
                        phone = input(f"Телефон [{self.phonebook.contacts[contact_id - 1].phone}]: ")
                        comment = input(f"Комментарий [{self.phonebook.contacts[contact_id - 1].comment}]: ")
                        self.phonebook.edit_contact(contact_id, name, phone, comment)
                        self.changed = True
                        print("Контакт успешно изменён.")
                    except ContactNotFoundError as e:
                        show_error(e)
                case "5":
                    try:
                        contact_id = input_contact_id()
                        self.phonebook.delete_contact(contact_id)
                        self.changed = True
                        print("Контакт успешно удалён.")
                    except ContactNotFoundError as e:
                        show_error(e)
                case "6":
                    try:
                        self.phonebook.save_contacts()
                        print("Контакты успешно сохранены.")
                    except FileWriteError as e:
                        show_error(e)
                    print("Выход из программы.")
                    break
                case "7":
                    if self.changed and not confirm_exit_without_saving():
                        continue
                    print("Выход без сохранения.")
                    break
                case _:
                    print("Неверный выбор. Попробуйте снова.")