class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author} ({self.quantity} available)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, quantity):
        self.books.append(Book(title, author, quantity))

    def display_books(self):
        if not self.books:
            print("No books available in the library.\n")
            return
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book}")
        print()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.quantity > 0:
                    book.quantity -= 1
                    return book
                else:
                    raise ValueError("This book is currently unavailable.")
        raise ValueError("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.quantity += 1
                return book
        raise ValueError("Invalid book title. This book doesn't belong to this library.")

class User:
    def __init__(self, name, roll, class_name, section):
        self.name = name
        self.roll = roll
        self.class_name = class_name
        self.section = section
        self.borrowed_books = []

    def __repr__(self):
        return f"{self.name} (Roll: {self.roll}, Class: {self.class_name}, Section: {self.section})"

class StudentManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, roll, class_name, section):
        new_user = User(name, roll, class_name, section)
        self.users.append(new_user)
        print(f"User {name} added successfully.\n")

    def display_users(self):
        if not self.users:
            print("No users registered.\n")
            return
        for idx, user in enumerate(self.users, start=1):
            print(f"{idx}. {user}")
        print()

    def find_user(self, roll):
        for user in self.users:
            if user.roll == roll:
                return user
        return None

    def display_borrowed_books(self, roll):
        user = self.find_user(roll)
        if user:
            if user.borrowed_books:
                print(f"{user.name} has borrowed:")
                for book in user.borrowed_books:
                    print(f"- {book.title}")
            else:
                print(f"{user.name} has not borrowed any books.")
        else:
            print("User not found.")

def main():
    library = Library()
    student_manager = StudentManager()
    while True:
        add = input("Add a student? (y/n): ").strip().lower()
        if add == "y":
            name = input("Name: ")
            roll = input("Roll no: ")
            class_name = input("Class: ")
            section = input("Section: ")
            student_manager.add_user(name, roll, class_name, section)
        else:
            break

    while True:
        print("1. Add Book\n2. View Books\n3. Borrow Book\n4. Return Book\n5. View Students\n6. View Borrowed Books by Student\n7. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                while True:
                    try:
                        quantity = int(input("Enter quantity: "))
                        if quantity < 1:
                            print("Quantity must be at least 1.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid integer for quantity.")
                library.add_book(title, author, quantity)
            elif choice == "2":
                library.display_books()
            elif choice == "3":
                roll = input("Enter your roll number: ")
                user = student_manager.find_user(roll)
                if not user:
                    print("User not found. Please register first.")
                    continue
                title = input("Enter the title of the book you want to borrow: ")
                book = library.borrow_book(title)
                user.borrowed_books.append(book)
                print(f"{user.name} borrowed: {book.title}\n")
            elif choice == "4":
                roll = input("Enter your roll number: ")
                user = student_manager.find_user(roll)
                if not user:
                    print("User not found.")
                    continue
                title = input("Enter the title of the book you want to return: ")
                for b in user.borrowed_books:
                    if b.title.lower() == title.lower():
                        library.return_book(title)
                        user.borrowed_books.remove(b)
                        print(f"{user.name} returned: {title}\n")
                        break
                else:
                    print("You did not borrow this book.")
            elif choice == "5":
                student_manager.display_users()
            elif choice == "6":
                roll = input("Enter the roll number of the student: ")
                student_manager.display_borrowed_books(roll)
            elif choice == "7":
                print("Thanks for using the Library System!")
                break
            else:
                print("Invalid choice. Try again.\n")
        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
