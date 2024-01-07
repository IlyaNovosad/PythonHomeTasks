# Открыть файл
# сохранить файл
# Создание контакта
# изм контакт
# Найти контакт
# Удалить контакт
# Показать контакт
# Выход
import file_opener_reader_writer as frw
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
    contacts = frw.convert_file_to_dict(file_name)

    while True:

        print_menu()  # done
        input_number = int(input())
        if input_number == 1:
            frw.create_new_contact(file_name)  # done
        elif input_number == 2:
            frw.change_contact_information(file_name)
        elif input_number == 3:
            frw.find_contact(contacts)  # done
        elif input_number == 4:
            frw.delete_contact(contacts)  # done
        elif input_number == 5:
            frw.show_contacts(contacts)  # done
        elif input_number == 6:
            break
        elif input_number == 7:
            frw.copy_line_in_another_file(file_name, second_file)


if __name__ == "__main__":
    main()