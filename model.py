# model.py

import json
import os
from exceptions import FileReadError, FileWriteError, ContactNotFoundError, InvalidContactDataError


class Contact:
    def __init__(self, contact_id, name, phone, comment):
        self.id = contact_id
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "comment": self.comment
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            contact_id=data["id"],
            name=data["name"],
            phone=data["phone"],
            comment=data.get("comment", "")
        )

    def __str__(self):
        return f"[ID: {self.id}] {self.name} - {self.phone} ({self.comment})"


class PhoneBook:
    FILENAME = "contacts.json"

    def __init__(self):
        self.contacts = []

    def load_contacts(self):
        try:
            if not os.path.exists(self.FILENAME):
                self.contacts = []
                return
            with open(self.FILENAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.contacts = [Contact.from_dict(contact) for contact in data]
        except Exception as e:
            raise FileReadError(f"Ошибка при загрузке файла: {e}")

    def save_contacts(self):
        try:
            with open(self.FILENAME, "w", encoding="utf-8") as file:
                json.dump([contact.to_dict() for contact in self.contacts], file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise FileWriteError(f"Ошибка при сохранении файла: {e}")

    def get_all_contacts(self):
        return self.contacts

    def add_contact(self, name, phone, comment):
        if not name or not phone:
            raise InvalidContactDataError("Имя и телефон обязательны для заполнения.")
        new_id = max((c.id for c in self.contacts), default=0) + 1
        self.contacts.append(Contact(new_id, name, phone, comment))

    def find_contacts(self, query):
        query = query.lower()
        results = [
            contact for contact in self.contacts
            if query in contact.name.lower() or
               query in contact.phone.lower() or
               query in contact.comment.lower()
        ]
        return results

    def edit_contact(self, contact_id, name=None, phone=None, comment=None):
        for contact in self.contacts:
            if contact.id == contact_id:
                contact.name = name or contact.name
                contact.phone = phone or contact.phone
                contact.comment = comment or contact.comment
                return
        raise ContactNotFoundError(f"Контакт с ID {contact_id} не найден.")

    def delete_contact(self, contact_id):
        for i, contact in enumerate(self.contacts):
            if contact.id == contact_id:
                del self.contacts[i]
                return
        raise ContactNotFoundError(f"Контакт с ID {contact_id} не найден.")