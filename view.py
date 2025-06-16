# view.py

def show_all_contacts(contacts):
    if not contacts:
        print("Телефонный справочник пуст.")
        return
    for contact in contacts:
        print(str(contact))


def input_contact_data():
    name = input("Введите имя: ").strip()
    phone = input("Введите номер телефона: ").strip()
    comment = input("Введите комментарий: ").strip()
    return name, phone, comment


def input_contact_id():
    try:
        return int(input("Введите ID контакта: "))
    except ValueError:
        raise ValueError("Неверный формат ID.")


def input_search_query():
    return input("Введите поисковое слово: ").strip()


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


def confirm_exit_without_saving():
    choice = input("У вас есть несохраненные изменения. Всё равно выйти без сохранения? (y/n): ").lower()
    return choice == 'y'


def show_error(message):
    print(f"\n❌ Ошибка: {message}")