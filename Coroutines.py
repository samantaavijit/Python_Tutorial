import time


def searcher():
    # Some 4 seconds time consuming task
    book = "This is a book on Avijit"
    time.sleep(4)
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")


if __name__ == '__main__':
    search = searcher()
    print("Search Started")
    next(search)
    search.send("Avijit")
    input("Press any key ")
    search.send("book")
    search.send(input("Press any value "))
    search.close()
