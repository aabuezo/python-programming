def greet():
    print('Hello')


# takes a function as an argument
def before_and_after(func):
    print('Before...')
    func()
    print('After...')


# pass the function by name
before_and_after(greet)


movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "A Beautiful Day", "director": "Heller"},
    {"name": "The Irishman", "director": "Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"}
]


def find_movie(expected, finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie


find_by = input('What property are we searching by? ')
looking_for = input('What are you looking for? ')
movie = find_movie(looking_for, lambda movie: movie[find_by])
print(movie or 'No movies found.')
