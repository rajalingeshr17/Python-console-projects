import datetime

class Library:
    def __init__(self, books):
        self.books = books
        self.lent_books = {}

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book not in self.lent_books:
                print(f" - {book}")
        print()

    def lend_book(self, book_name, user):
        if book_name not in self.books:
            print("This book is not in the library.")
        elif book_name in self.lent_books:
            print(f"This book is already lent to {self.lent_books[book_name]}.")
        else:
            self.lent_books[book_name] = user
            print(f"{book_name} has been lent to {user} on {datetime.date.today()}.")

    def add_book(self, book_name):
        if book_name in self.books:
            print("This book already exists in the library.")
        else:
            self.books.append(book_name)
            print(f"{book_name} has been added to the library.")

    def return_book(self, book_name, user):
        if self.lent_books.get(book_name) == user:
            del self.lent_books[book_name]
            print(f"{book_name} has been returned by {user}.")
        else:
            print("Either the book was not lent or you are not the borrower.")

def main():
    library = Library([
        "Python Programming",
        "Data Science Essentials",
        "Machine Learning Basics",
        "Artificial Intelligence Guide"
    ])

    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Display Available Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            library.lend_book(book, user)
        elif choice == '3':
            book = input("Enter the name of the book you want to add: ")
            library.add_book(book)
        elif choice == '4':
            book = input("Enter the name of the book you want to return: ")
            user = input("Enter your name: ")
            library.return_book(book, user)
        elif choice == '5':
            print("Thank you for using the Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
