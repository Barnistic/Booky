import json

library = [] #the library itself


def addb(name):
    if name.lower() not in library: #checks if the book's name with lower characters is in the library
        library.append(name.lower())
    else:
        print("That book is already in the library!")


def remb(name):
    if name.lower() in library: #checks if the book's name with lower characters is in the library
        library.remove(name.lower())
    else:
        print("There is no such book in the library!")


def save():
    try:
        answer = input("Are you sure you want to overwrite the save?(y for yes, n for no)")
        if answer is "y":
            with open("books.json", "w") as write_file:
                if len(library) > 0:
                    json.dump(library, write_file, indent=4)
                    print("Saved!")
                else:
                    print("There is nothing to save!")
        else:
            print("")
    except TypeError:
        print("Invalid input")


def load():
    data = json.load(open("books.json", "r")) #sets the json's variables into a variable
    for book in data:
        library.append(book)
    print("Loaded!")


def show():
    for books in library:
        print(books.title(), end=", ")
