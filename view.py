# view.py

def show_menu():
    print("\n📞 Телефонный справочник")
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Поиск контакта")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Сохранить и выйти")
    print("7. Выйти без сохранения")
    return input("Выберите действие (1-7): ").strip()


def display_contacts(contacts):
    if not contacts:
        print("Телефонный справочник пуст.")
        return
    for contact in contacts:
        print(str(contact))


def get_add_contact_input():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    return name, phone, comment


def get_edit_contact_input():
    contact_id = input("Введите ID контакта: ")
    name = input("Новое имя (оставьте пустым, чтобы не менять): ")
    phone = input("Новый телефон (оставьте пустым, чтобы не менять): ")
    comment = input("Новый комментарий (оставьте пустым, чтобы не менять): ")
    return int(contact_id), name, phone, comment


def get_search_query():
    return input("Введите поисковое слово: ")


def get_delete_contact_id():
    return int(input("Введите ID контакта для удаления: "))


def show_error(message):
    print(f"❌ Ошибка: {message}")


def show_success(message):
    print(f"✅ {message}")