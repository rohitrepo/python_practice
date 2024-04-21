class Book:
    def __init__ (self, name, author, page):
        self.name = name
        self.author = author
        self.page = page
        print("An instance is created")

firstbook = Book ('Alchemist', 'Paulo Coelho', 200)
print(firstbook.name)
print(firstbook.author)
print(firstbook.page)

secondbook = Book ('Its not about the bike', 'Lance Armstrong', 220)
print(secondbook.name)
print(secondbook.author)
print(secondbook.page)