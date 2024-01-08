# Открыть файл
# сохранить файл
# Создание контакта
# изм контакт
# Найти контакт
# Удалить контакт
# Показать контакт
# Выход
import functions as func

count_id = 0


def print_menu():
    print("1. Create contact")
    print("2. Change contact")
    print("3. Find contact")
    print("4. Delete contact")
    print("5. Show contacts")
    print("6. Exit")
    print("7. Copy line in another file")
    print("8. Save changes")


def main():
    file_name = "phones.txt"
    second_file = "another_file.txt"
    contacts = func.convert_file_to_dict(file_name)

    while True:

        print_menu()  # done
        input_number = int(input())
        if input_number == 1:
            func.create_new_contact(file_name)
        elif input_number == 2:
            func.change_contact_information(file_name)
        elif input_number == 3:
            func.find_contact(contacts)
        elif input_number == 4:
            func.delete_contact(contacts)
        elif input_number == 5:
            func.show_contacts(contacts)
        elif input_number == 6:
            break
        elif input_number == 7:
            func.copy_line_in_another_file(file_name, second_file)


if __name__ == "__main__":
    main()
