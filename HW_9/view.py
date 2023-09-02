import text
from model import PhoneBook

def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f"\t{i}: {item}")
    while True:
        choice = input(text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)
            #main_menu()

def print_message(msg: str):
    print('\n' + '='*len(msg))
    print(msg)
    print('='*len(msg)+'\n')

def show_book(book: PhoneBook, msg: str):
    if book:
        print('\n' + '*'*(book.max_len("name")+book.max_len("phone")+book.max_len("comment")+9))
        for i, contact in book.phone_book.items():
            print(f'{i:>3}. {contact.name:.<{book.max_len("name")}} '
                f'{contact.phone:.<{book.max_len("phone")}} '
                f'{contact.comment:<{book.max_len("comment")}}')
        print('*'*(book.max_len("name")+book.max_len("phone")+book.max_len("comment")+9) + '\n')
    else:
        print_message(msg)

def input_contact(msg: str) -> list[str]:
    contact = []
    for input_text in msg:
        contact.append(input(input_text))
    return contact

def input_request(msg: str) -> str:
    return input(msg)