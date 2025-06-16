# controller.py

from view import (
    show_menu,
    display_contacts,
    get_add_contact_input,
    get_edit_contact_input,
    get_search_query,
    get_delete_contact_id,
    show_error,
    show_success
)
from utils import load_contacts, save_contacts
from exceptions import ContactNotFoundError, InvalidContactDataError, FileReadError, FileWriteError
from model import Contact


class PhoneBookController:
    def __init__(self):
        self.contacts = []
        try:
            self.contacts = load_contacts()
        except FileReadError as e:
            show_error(str(e))

    def run(self):
        while True:
            choice = show_menu()

            match choice:
                case "1":
                    display_contacts(self.contacts)
                case "2":
                    self.add_contact()
                case "3":
                    self.search_contact()
                case "4":
                    self.edit_contact()
                case "5":
                    self.delete_contact()
                case "6":
                    self.save_and_exit()
                    break
                case "7":
                    print("Выход без сохранения.")
                    break
                case _:
                    print("Неверный выбор. Попробуйте снова.")

    def add_contact(self):
        name, phone, comment = get_add_contact_input()
        if not name or not phone:
            raise InvalidContactDataError("Имя и телефон обязательны для заполнения.")
        contact_id = len(self.contacts) + 1
        contact = Contact(contact_id, name, phone, comment)
        self.contacts.append(contact)
        show_success("Контакт успешно добавлен.")

    def edit_contact(self):
        contact_id, new_name, new_phone, new_comment = get_edit_contact_input()
        found = False
        for contact in self.contacts:
            if contact.id == contact_id:
                contact.name = new_name or contact.name
                contact.phone = new_phone or contact.phone
                contact.comment = new_comment or contact.comment
                found = True
                show_success("Контакт обновлён.")
                break
        if not found:
            raise ContactNotFoundError(f"Контакт с ID {contact_id} не найден.")

    def delete_contact(self):
        contact_id = get_delete_contact_id()
        for i, contact in enumerate(self.contacts):
            if contact.id == contact_id:
                del self.contacts[i]
                show_success("Контакт удалён.")
                return
        raise ContactNotFoundError(f"Контакт с ID {contact_id} не найден.")

    def search_contact(self):
        query = get_search_query().lower()
        results = [
            contact for contact in self.contacts
            if query in contact.name.lower() or
               query in contact.phone.lower() or
               query in contact.comment.lower()
        ]
        if results:
            display_contacts(results)
        else:
            show_error("Контакты не найдены.")

    def save_and_exit(self):
        try:
            save_contacts(self.contacts)
            show_success("Данные сохранены. Выход.")
        except FileWriteError as e:
            show_error(str(e))