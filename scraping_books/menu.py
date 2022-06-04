from app import books_list


USER_CHOICE = """Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to quit

Enter your choice: """


def print_best_books():
    best_books = sorted(books_list, key=lambda x: (x.rating * -1, x.price))[:5]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books_list, key=lambda x: x.price)[:5]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books_list)


def get_next_book():
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)


if __name__ == '__main__':
    menu()
