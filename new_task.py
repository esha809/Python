class Bookcollection:
    def __init__(self):
        self.book = {}

    def add_book(self, title, quantity):
        if title in self.book:
            self.book[title] += quantity
        else:
            self.book[title] = quantity

    def remove_book(self, title, quantity):
        if title in self.book:
            if self.book[title] >= quantity:
                self.book[title] -= quantity
                if self.book[title] == 0:
                    del self.book[title]
            else:
                print("Not enough books to remove")
        else:
            print("Book not found")

    def view_book(self):
        for title, quantity in self.book.items():
            print(f"{title} : {quantity}")

    def total_book(self):
        return sum(self.book.values())

def main():
    collection = Bookcollection()
    while True:
        choice = input("\n1. Add 2. Remove 3. View 4. Total 5. Exit: ")
        if choice == '1':
            collection.add_book(input("Title: "), int(input("Quantity: ")))
        elif choice == '2':
            collection.remove_book(input("Title: "), int(input("Quantity: ")))
        elif choice == '3':
            collection.view_book()
        elif choice == '4':
            print(f"Total books: {collection.total_book()}")
        else:
            break

main()
