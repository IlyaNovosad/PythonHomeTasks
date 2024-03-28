import Text
import datetime


def main_menu() -> int:
    for n, item in enumerate(Text.main_menu):
        if n == 0:
            print(item)
        else:
            print(f'\t{n}. {item}')
    while True:
        choice = input(Text.main_menu_choice)
        if choice.isdigit() and 0 < int(choice) < len(Text.main_menu):
            return int(choice)
        print(f'Введите пункт меню от 1 до {len(Text.main_menu) - 1}')


def show_notes(notes_list: dict[int, list[str]], error_message: str):
    max_size = list(map(lambda x: len(max(x, key=len)), list(zip(*notes_list.values()))))
    if notes_list:
        print('\n' + '=' * (sum(max_size) + 10))
        for n, notes in notes_list.items():
            print(f'{n:>3}. {notes[0]:<{max_size[0]}} '
                  f'{notes[1]:<{max_size[1]}} '
                  f'{notes[2]:<{max_size[2]}} '
                  f'{notes[3]:<{max_size[3]}}')
        print('=' * (sum(max_size) + 10) + '\n')
    else:
        print_message(error_message)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def add_note(message: list[str], note: list[str] = None):
    note = note if note else ['', '', '', '']
    for n, mes in enumerate(message):
        field = input(mes)
        note[n] = field if field else note[n]
        if note[3] == 'date':
            note[3] = set_date()
        else:
            note[3] = ''
    return note


def input_by_date(message: str) -> str:
    return input(message)


def input_data(message: str) -> str:
    return input(message)


def input_id(message: int) -> str:
    return input(message)


def set_date():
    new_date = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    return new_date
