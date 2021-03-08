# Lets do some basic class definitions

# TODO: create a basic class

class Book:
    #pass     # pass means the function is doing nothing
    def __init__(self, title):
        self.title = title

# TODO: create instances of the class

b1 = Book("Wear Masks")
b2 = Book("Stay at home AND learn")


# TODO: print the class and property
print(b1)
print(b1.title)
