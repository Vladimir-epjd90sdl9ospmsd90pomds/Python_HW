import model 
import view
import text
#
def search_contact():
    word = view.input_request(text.input_search_word)
    result = model.find_contact(word)
    view.show_book(result, text.not_find(word))
    if result:
        return True

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(text.load_successful)
            case 2:
                model.save_file()
                view.print_message(text.save_successful)
            case 3:
                view.show_book(model.phone_book, text.empty_book_error)
            case 4:
                new_contact = view.input_contact(text.input_contact)
                model.add_contact(new_contact)
                view.print_message(text.contact_action(new_contact[0], text.operation[0]))
            case 5:
                search_contact()
            case 6:
                c_id = int(view.input_request(text.input_edit_contact_id))
                new_contact = view.input_contact(text.input_edit_contact)
                name = model.edit_contact(c_id, new_contact)
                view.print_message(text.contact_action(name, text.operation[1]))
            case 7:
                if search_contact():
                    c_id = int(view.input_request(text.input_del_contact_id))
                    name = model.delete_contact(c_id)
                    view.print_message(text.contact_action(name, text.operation[2]))
            case 8:
                if model.phone_book != model.phone_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        model.save_file()
                        view.print_message(text.save_successful)                        
                view.print_message(text.exit_program)
                break


start()    