"""
Library System Description:

The developed library system allows for managing books and users. With it, you can register books, search for them by title, genre, or author, register users, keep track of books 
a user has borrowed, as well as make recommendations based on genres and sort books by title.

Integrated Concepts:

    Object-Oriented Programming (OOP): We use classes and objects to model entities like Book, User, and Library. These classes encapsulate data for each entity and provide methods 
    to interact with those data.

    Data Structures:
        Lists/ArrayList: Used to store collections of books and books borrowed by users.
        Hashmaps/Dictionaries: Employed to store registered users, allowing for quick retrieval based on the username.

    Search Functions: Methods were developed to search for books based on various criteria, like title, genre, and author.

    Sorting: A function is provided to sort books by title, implying the use of sorting algorithms and lambda (in Python) to specify the sort criterion.

    Flow Control: Conditional structures (like if) and loops (like for) are used to iterate through lists and perform searches.

    Encapsulation: The member data of the classes are protected (they're private by default in Java and protected in Python). The class methods are used to access and modify these data.

    Class Relationships: The User class has a relationship with the Book class as a user can have multiple books borrowed.

    Simple Recommendations: Though basic, the system has a function to recommend books based on genres, demonstrating an initial approach toward recommendation systems.

This library system, despite its simplicity, showcases a range of fundamental concepts in programming and software design. It can be extended to include more advanced features and serve 
as a foundation for a more complex library management system.
"""

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class User:
    def __init__(self, username):
        self.username = username
        self.borrowed_books = []
        self.fine = 0

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def search_by_genre(self, genre):
        return [book for book in self.books if book.genre.lower() == genre.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def register_user(self, user):
        self.users[user.username] = user

    def get_user(self, username):
        return self.users.get(username, None)

    def recommend_books(self, genre):
        # Simple recommendation based on genre. Can be enhanced.
        return self.search_by_genre(genre)

    def sort_books_by_title(self):
        self.books.sort(key=lambda x: x.title)

# Testing can be done below this
