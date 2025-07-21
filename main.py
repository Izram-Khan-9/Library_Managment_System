user_name = input('Enter your name: ')
hello_message = f'Hello {user_name}😊'
print('\n_-_-_-_-_-_-_-_-📖Izram\'s Library📖_-_-_-_-_-_-_-_-\n')
welcome_message = f'You are welcome to Izram\'s Library {user_name}❤️😎'
thank_you_message = f'Thank you for using Izram\'s Library {user_name}🤝\n'
features = 'You can perform the following operations in this Library:\n\n1. Add as many books as you want\n2. Remove as many books as you want\n3. View the total number of books in your library'

print(hello_message)
print(welcome_message)
print(thank_you_message)
print(features)
print('\n--------------------------------------------------------------\n')


class Library:
  def __init__(self, no_of_books, books):
    self.no_of_books = no_of_books
    self.books = books

  def display_books(self):
    if len(self.books) > 0:
      print('You have the following books in your library:')
      for index, book in enumerate(self.books, start=1):
        print(index, book)
    else:
      print('You currently have no books in your library\n')

  def add_book(self):
    while True:
      new_book = input('Enter the name of the book you want to add (0 to stop): ')
      if new_book in self.books:
        print('Oops! Book already exists ❌')
      elif new_book == '0':
        print('\nYou stopped adding books\n')
        break
      else:
        self.books.append(new_book)
        self.no_of_books += 1
        print(f'{new_book} is added successfully to your library ➕\n')

  def remove_book(self):
    print('It\'s time to remove some extra stuff from your library')
    while True:
      book_to_remove = input('Enter the name of the book you want to remove (0 to stop): ')
      if book_to_remove in self.books:
        self.books.remove(book_to_remove)
        self.no_of_books -= 1
        print(f'{book_to_remove} is removed successfully from your library ➖')
      elif book_to_remove == '0':
        print('\nYou stopped removing books\n')
        break
      else:
        print('Oops! Book does not exist ❌')

  def total_number_of_books(self):
    print(f'You have a total of {self.no_of_books} books in your library')
    print('The books are:')
    for index, book in enumerate(self.books, start=1):
      print(f'{index}: {book}')


a = Library(0, [])
a.display_books()
a.add_book()
a.remove_book()
a.total_number_of_books()
print(f'Nice collection of books, {user_name} 📕')
print('\n---------------⛔THE END⛔---------------\n')
