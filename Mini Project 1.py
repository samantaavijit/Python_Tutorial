"""
create a library class
display book
lend book - (who owns the book if not present)
add book
return book
constructor 'Library(listofbooks, libraryname)'
create a main function and run an infinite while loop asking users
for their input
"""


class Library:
    def __init__(self, ls, name):
        self.bookList = ls
        self.name = name
        self.lenDict = {}

    def displayBooks(self):
        print(f"We have following books in our library : {self.name}")
        for book in self.bookList:
            print(book)
        print()

    def lendBooks(self, user, book):
        if book not in self.bookList:
            print(f"{book} not present in our library")
            self.displayBooks()
            return
        if book not in self.lenDict.keys():
            self.lenDict.update({book: user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lenDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book added successfully")

    def returnBook(self, book):
        del self.lenDict[book]


if __name__ == '__main__':
    avijit = Library(["JAVA", "HTML", "C++", "C", "Python", "Android", "CSS", "JS", "PHP"], "SamantaAvijit")
    while True:
        print(f"Welcome to the {avijit.name} library. Enter your choice to continue")
        print("1. For Display Book\n2. For Lend a Book\n3. For Add a Book\n4. For Return a Book\n")
        user_choice = int(input())
        if user_choice == 1:
            avijit.displayBooks()
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend : ")
            user = input("Enter your name ")
            avijit.lendBooks(user, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add : ")
            avijit.addBook(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return : ")
            avijit.returnBook(book)
        else:
            print("Not a  valid option")

        a = input("Press q to quit and c to continue ").lower()
        while a != "q" and a != "c":
            a = input("Press q to quit and c to continue ").lower()

        if a == "q":
            exit()
        if a == "c":
            continue
