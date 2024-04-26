import csv
from sys import exit
mrl = []

def main():
    print("First, let's choose a book!")
    while True:
        print("Do you want to search for a book by title or by author?\n'by title' - type 't'\n'by author' - type 'a'\n'exit' - type 'e'")
        answer = input("Your answer: ")
        if answer == "a":
            author = input("Author: ")
            if search_author(author):
                break
        elif answer == "t":
            title = input("Title: ")
            if search_title(title):
                break
        elif answer == "e":
            exit("For now, your list is empty")
        else:
            print("Please, check whether you've typed one of the letters: 'a', 't', 'n' without quotes")


    while True:
        print("Do you want to add or remove a book from your list?\n'add' - type 'a'\n'remove' - type 'r'\nsee my list and exit' - type 'e'")
        answer = input("Your answer: ")
        if answer == "a":
            title = input("Type in the title of the book you want to add: ")
            add_book(title)
        elif answer == "r":
            title = input("Type in the title of the book you want to remove: ")
            remove_book(title)
        elif answer == "e":
            break
        else:
            print("Please, check whether you've typed one of the following options: 'a', 'r', 's', 'n'")
    # Print out the reading list
    if mrl:
        print("Here's your reading list:")
        for book in mrl:
            print(f"{book['title']} by {book['author']}, year: {book['year']}, language: {book['language']}")


def search_author(author):
    books_from_author = []
    counter = 0
    with open("bks.csv") as bks:
        reader = csv.DictReader(bks)
        for row in reader:
            if author.lower() in row["author"].lower():
                books_from_author.append(row)
                counter = 1

        if counter > 0:
            print(f"Books by authors whose name contain '{author.title()}':")
            for book in books_from_author:
                print(f"{book['title']} by {book['author']} was published in {book['year']}. Language: {book['language']}")
            return True
        print(f"The author {author.title()} doesn't have any books on our list")
        return False


def search_title(title):
    books_with_title = []
    counter = 0
    with open("bks.csv") as bks:
        reader = csv.DictReader(bks)
        for row in reader:
            if title.lower() in row["title"].lower():
                books_with_title.append(row)
                counter = 1
        if counter > 0:
            print(f"Books that have '{title}' in their titles: ")
            for book in books_with_title:
                print(f"{book['title']} by {book['author']} published in {book['year']}. Language: {book['language']}")
            return True
        else:
            print(f"There're no books with the title containing '{title}' on our list")
        return False


def add_book(title):
    counter = 0
    with open("bks.csv") as bks:
        reader = csv.DictReader(bks)
        for row in reader:
            if title.lower() in row["title"].lower():
                mrl.append(row)
                counter += 1
                print(f"The book {row['title']} was added to your list!")

        if counter > 0:
            return True
        print("We haven't found the book with this title in our list")
        return False


def remove_book(title):
    with open("bks.csv") as bks:
        reader = csv.DictReader(bks)
        for row in reader:
            if title.lower() in row["title"].lower():
                try:
                    mrl.remove(row)
                    print(f"The book {row['title']} was removed from your list!")
                except ValueError:
                        print("We haven't found the book with this title in your reading list")
                else:
                    return True
        print("We haven't found the book with this title in our 'top books' list")
        return False


if __name__ == "__main__":
    main()