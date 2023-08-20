from datetime import datetime, timedelta # importing datetime and timedelta for due date calculation

class Book: # Book class
    __title = "" # private attributes for storing title of book
    __author = "" # private attributes for storing author of book
    __isbn = "" # private attributes for storing ISBN of book
    __total_copies = 0 # private attributes for storing total copies of book
    __available_copies = 0 # private attributes for storing available copies of book
    __reserved_by = None # private attributes for storing reserved by of book

    def __init__(self, title, author, isbn, total_copies, available_copies): # constructor for Book class
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.reserved_by = None

    def __str__(self): # string method for Book class to display book details
        return f"{self.title} by {self.author}"


class Patron: # Patron class
    __name = "" # private attributes for storing name of patron
    __patron_id = "" # private attributes for storing patron id of patron
    __books_borrowed = [] # private attributes for storing books borrowed by patron

    def __init__(self, name, patron_id): # constructor for Patron class
        self.name = name
        self.patron_id = patron_id
        self.books_borrowed = []

    def __str__(self): # string method for Patron class to display patron details
        return f"{self.name} with ID {self.patron_id}"


class Library: # Library class
    __books = [] # private list for storing books in library
    __patrons = [] # private list for storing patrons in library

    def __init__(self): # constructor for Library class
        self.books = []
        self.patrons = []

    def add_book(self, book): # method for adding book to library
        self.books.append(book) # append book to books list
        print("Book added.")

    def add_patron(self, patron): # method for adding patron to library
        self.patrons.append(patron) # append patron to patrons list
        print("Patron added.")

    def borrow_book(self, patron, book): # method for borrowing book from library
        if book.available_copies > 0: # if book is available
            due_date = datetime.now() + timedelta(days=14)  # Due date is set to 14 days from borrowing
            book.available_copies -= 1 # Reduce available copies by 1
            patron.books_borrowed.append((book, due_date))  # Store the book and due date as a tuple
            print(f"{patron.name} borrowed {book.title}. Due date: {due_date.strftime('%Y-%m-%d')}") # Print borrowing details
        else: # if book is not available
            print("Sorry, this book is not available. You can reserve it.")

    def return_book(self, patron, book): # method for returning book to library
        for b, due_date in patron.books_borrowed: # iterate through books borrowed by patron
            if b == book: # if book is found
                patron.books_borrowed.remove((b, due_date)) # remove book from books borrowed by patron
                book.available_copies += 1 # increase available copies by 1
                days_overdue = max((datetime.now() - due_date).days, 0) # Calculate days overdue
                overdue_fine = days_overdue * 50  # Fine of Rs.50 per day
                if overdue_fine > 0: # if there is a fine
                    print(f"Overdue fine: ${overdue_fine}") # print fine
                print(f"{patron.name} returned {book.title}.") # print return details
                break # break out of loop
        else: # if book is not found
            print("Sorry, you did not borrow this book.")

    def reserve_book(self, patron, book): # method for reserving book from library
        if book.available_copies == 0: # if book is not available
            if book.reserved_by is None: # if book is not reserved
                book.reserved_by = patron # reserve book for patron
                print(f"{patron.name} reserved {book.title}.")
            elif book.reserved_by == patron: # if book is already reserved by patron
                print(f"{patron.name} already has a reservation for {book.title}.")
            else: # if book is already reserved by another patron
                print(f"{book.title} is already reserved by {book.reserved_by.name}.")
        else: # if book is available
            print(f"{book.title} is available for borrowing, no need to reserve.")

    def __str__(self): # string method for Library class to display library details
        return f"Books: {self.books}\nPatrons: {self.patrons}"


class Administrator(Patron): # Administrator class
    def __init__(self, name, admin_id): # constructor for Administrator class
        super().__init__(name, admin_id) # call constructor of Patron class
        self.admin_privileges = True # set admin privileges to True

    def add_book(self, library, book): # method for adding book to library
        library.add_book(book) # call add_book method of Library class to add book to library
    def remove_book(self, library, book_title): # method for removing book from library
        book_to_remove = None # initialize book_to_remove to None
        for book in library.books: # iterate through books in library
            if book.title == book_title: # if book is found
                book_to_remove = book # set book_to_remove to book
                break # break out of loop
        if book_to_remove: # if book is found
            library.books.remove(book_to_remove) # remove book from library
            print("Book removed.")
        else: # if book is not found
            print("Book not found.")

    def manage_patron(self, library, patron): # method for managing patron in library
        library.add_patron(patron) # call add_patron method of Library class to add patron to library

class Catalog: # Catalog class
    def __init__(self, library): # constructor for Catalog class
        self.library = library

    def display_books(self): # method for displaying books in library
        for book in self.library.books: # iterate through books in library
            print(book) # display books

    def display_patrons(self): # method for displaying patrons in library
        for patron in self.library.patrons: # iterate through patrons in library
            print(patron) # display patrons


print("Welcome to the Library Management System!") # Welcome message
print() # Blank line

library = Library() # Creating a library object
catalog = Catalog(library) # Creating a catalog object
admin = Administrator("Admin", "admin123")  # Creating an admin object

while True: # Infinite loop
    # Display menu
    print("1. Add Book")
    print("2. Add Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Add Book (Admin)")
    print("8. Remove Book (Admin)")
    print("9. Add Patron (Admin)")
    print("10. Reserve Book (Admin)")
    print("0. Exit")

    print() # Blank line

    choice = input("Enter your choice: ") # Get user choice from menu

    if choice == "1": # Add book
        print() # Blank line
        title = input("Enter book title: ") # Get book title from user
        author = input("Enter author name: ") # Get author name from user
        isbn = input("Enter ISBN: ") # Get ISBN from user
        total_copies = int(input("Enter total copies: ")) # Get total copies from user and convert to integer
        available_copies = int(input("Enter available copies: ")) # Get available copies from user and convert to integer
        while available_copies < 0: # Check if available copies is negative
            print("Available copies cannot be negative")
            available_copies = int(input("Enter available copies: ")) # Get available copies from user and convert to integer
        new_book = Book(title, author, isbn, total_copies, available_copies) # Create a new book object
        library.add_book(new_book) # Add book to library
        print() # Blank line

    elif choice == "2": # Add patron
        print() # Blank line
        name = input("Enter patron name: ") # Get patron name from user
        patron_id = input("Enter patron ID: ") # Get patron ID from user
        new_patron = Patron(name, patron_id) # Create a new patron object
        library.add_patron(new_patron) # Add patron to library
        print() # Blank line

    elif choice == "3": # Borrow book
        print() # Blank line
        patron_id = input("Enter patron ID: ") # Get patron ID from user
        book_title = input("Enter book title: ") # Get book title from user
        patron = None # Initialize patron to None
        book = None # Initialize book to None

        for p in library.patrons: # Iterate through patrons in library
            if p.patron_id == patron_id: # If patron is found in library
                patron = p # Set patron to p
                break # Break out of loop

        for b in library.books: # Iterate through books in library
            if b.title == book_title: # If book is found in library
                book = b # Set book to b
                break # Break out of loop

        if patron is None or book is None: # If patron or book is not found in library
            print("Invalid patron or book.")
        else: # If patron and book are found in library
            x = library.borrow_book(patron, book) # Borrow book from library

        print() # Blank line

    elif choice == "4": # Return book
        print() # Blank line
        patron_id = input("Enter patron ID: ") # Get patron ID from user
        book_title = input("Enter book title: ") # Get book title from user
        patron = None # Initialize patron to None
        book = None # Initialize book to None

        for p in library.patrons: # Iterate through patrons in library
            if p.patron_id == patron_id: # If patron is found in library
                patron = p # Set patron to p
                break # Break out of loop

        for b in library.books: # Iterate through books in library
            if b.title == book_title: # If book is found in library
                book = b # Set book to b
                break # Break out of loop

        if patron is None or book is None: # If patron or book is not found in library
            print("Invalid patron or book.")
        else: # If patron and book are found in library
            x = library.return_book(patron, book) # Return book to library

        print() # Blank line

    elif choice == "5": # Display books
        print() # Blank line
        print("Books in the library:")
        catalog.display_books() # Display books in library
        print() # Blank line

    elif choice == "6": # Display patrons
        print() # Blank line
        print("Patrons in the library:")
        catalog.display_patrons() # Display patrons in library
        print() # Blank line

    elif choice == "7": # Add book (Admin)
        print() # Blank line
        if admin.admin_privileges: # Check if admin privileges is True
            title = input("Enter book title: ") # Get book title from admin
            author = input("Enter author name: ") # Get author name from admin
            isbn = input("Enter ISBN: ") # Get ISBN from admin
            total_copies = int(input("Enter total copies: ")) # Get total copies from admin and convert to integer
            available_copies = int(input("Enter available copies: ")) # Get available copies from admin and convert to integer
            while available_copies < 0: # Check if available copies is negative
                print("Available copies cannot be negative")
                available_copies = int(input("Enter available copies: ")) # Get available copies from admin and convert to integer
            new_book = Book(title, author, isbn, total_copies, available_copies) # Create a new book object
            admin.add_book(library, new_book) # Add book to library
        else: # If admin privileges is False
            print("You do not have admin privileges.")
        print() # Blank line

    elif choice == "8": # Remove book (Admin)
        print() # Blank line
        if admin.admin_privileges: # Check if admin privileges is True
            book_title = input("Enter book title to remove: ") # Get book title from admin
            admin.remove_book(library, book_title) # Remove book from library
        else: # If admin privileges is False
            print("You do not have admin privileges.")
        print() # Blank line

    elif choice == "9": # Add patron (Admin)
        print() # Blank line
        if admin.admin_privileges: # Check if admin privileges is True
            name = input("Enter patron name: ") # Get patron name from admin
            patron_id = input("Enter patron ID: ") # Get patron ID from admin
            new_patron = Patron(name, patron_id) # Create a new patron object
            admin.manage_patron(library, new_patron) # Add patron to library
        else: # If admin privileges is False
            print("You do not have admin privileges.")
        print() # Blank line

    elif choice == "10": # Reserve book (Admin)
        print() # Blank line
        if admin.admin_privileges: # Check if admin privileges is True
            patron_id = input("Enter patron ID: ") # Get patron ID from admin
            book_title = input("Enter book title to reserve: ") # Get book title from admin
            patron = None # Initialize patron to None
            book = None # Initialize book to None

            for p in library.patrons: # Iterate through patrons in library
                if p.patron_id == patron_id: # If patron is found in library
                    patron = p # Set patron to p
                    break # Break out of loop

            for b in library.books: # Iterate through books in library
                if b.title == book_title: # If book is found in library
                    book = b # Set book to b
                    break # Break out of loop

            if patron is None or book is None: # If patron or book is not found in library
                print("Invalid patron or book.")
            else: # If patron and book are found in library
                library.reserve_book(patron, book) # Reserve book from library
        else: # If admin privileges is False
            print("You do not have admin privileges.")
        print() # Blank line

    elif choice == "0": # Exit
        print() # Blank line
        print("Thank you for using the Library Management System!")
        print("Exiting...")
        print() # Blank line
        break # Break out of infinite loop

    else: # Invalid choice from menu
        print() # Blank line
        print("Invalid choice. Please choose a valid option.")
        print() # Blank line
