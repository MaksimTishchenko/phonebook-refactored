# utils.py

import json
from pathlib import Path
from model import Contact
from exceptions import FileReadError, FileWriteError


DATA_FILE = "phonebook.json"


def load_contacts():
    path = Path(DATA_FILE)
    if not path.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Contact.from_dict(contact) for contact in data]
    except (json.JSONDecodeError, FileNotFoundError) as e:
        raise FileReadError(f"Ошибка чтения файла: {e}")


def save_contacts(contacts):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([contact.to_dict() for contact in contacts], f, ensure_ascii=False, indent=4)
    except Exception as e:
        raise FileWriteError(f"Ошибка записи в файл: {e}")