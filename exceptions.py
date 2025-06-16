# exceptions.py

class FileReadError(Exception):
    """Ошибка чтения файла"""
    pass


class FileWriteError(Exception):
    """Ошибка записи файла"""
    pass


class ContactNotFoundError(Exception):
    """Контакт не найден"""
    pass


class InvalidContactDataError(Exception):
    """Некорректные данные контакта"""
    pass