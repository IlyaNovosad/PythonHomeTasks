import Text
import View
import Model


def find_note():
    word = View.input_by_date(Text.input_search_date)
    result = Model.find_note(word)
    View.show_notes(result, Text.note_not_found(word))


def find_note_by_id():
    word = View.input_data(Text.input_search_data)
    result = Model.find_note(word)
    View.show_notes(result, Text.note_not_found(word))


def start_app():
    while True:
        choice = View.main_menu()
        match choice:
            case 1:
                Model.open_file()
                View.print_message(Text.load_successful)
            case 2:
                Model.save_file()
                View.print_message(Text.save_successful)
            case 3:
                notes_list = Model.notes_list
                View.show_notes(notes_list, Text.empty_notes)
            case 4:
                new_note = View.add_note(Text.new_notes)
                Model.new_note(new_note)
                View.print_message(Text.new_note_added_successful(new_note[0]))
            case 5:
                find_note()
            case 6:
                find_note_by_id()
                notes_list = Model.notes_list
                note_id = int(View.input_id(Text.input_id_change_notes))
                new_note = View.add_note(Text.change_notes, notes_list[note_id])
                Model.change_note(note_id, new_note)
                View.print_message(Text.note_change_successful(new_note[0]))
            case 7:
                notes_list = Model.notes_list
                View.show_notes(notes_list, Text.empty_notes)
                note_id = int(View.input_id(Text.input_id_deleted_note))
                name = Model.delete_contact(note_id)[0]
                View.print_message(Text.note_delete_successful(name))
            case 8:
                View.print_message(Text.good_bye)
                break
