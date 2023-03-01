books = []

print("Welcome to my digital library! It is a cute projec that Ms. Orret can up with!")

response = input("Do you want to add a book, find a book, or quit? Select A/F/Q")

if response == "A":
    book = input("What book do you want to add")
    books.append(book)

if response == "F":
    toFind = input("What book do you want to find?")
    found = False
    for book in books:
        if book == toFind:
            found = True
            print("Your book was found in your library! You already own this one!")
            break
    if found == False:
        print("Didn't find your book! Sorry! Better buy it!")