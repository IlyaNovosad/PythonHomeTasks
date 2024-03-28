notes_list = {}
path = 'notes.csv'
SEPARATOR = ';'


def open_file():
    global notes_list
    with open(path, 'r', encoding='utf-8') as file:
        notes_list = {i: item for i, item in
                      enumerate(sorted(list(map(lambda x: x.strip().split(SEPARATOR), file.readlines()))), 1)}


def save_file():
    global notes_list
    data = []
    for note in notes_list.values():
        data.append(SEPARATOR.join(note))
    data = '\n'.join(data)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(data)


def next_id():
    global notes_list
    return (max(notes_list) + 1) if notes_list else 1


def new_note(note: list[str]):
    global notes_list
    notes_list[next_id()] = note


def find_note(word: str) -> dict[int, list[str]]:
    global notes_list
    result = {}
    for u_id, note in notes_list.items():
        if word.lower() in str(note).lower():
            result[u_id] = note
    return result


def change_note(note_id: int, n_note: list[str]):
    global notes_list
    notes_list[note_id] = n_note


def delete_contact(note_id: int) -> list[str]:
    global notes_list
    return notes_list.pop(note_id)
