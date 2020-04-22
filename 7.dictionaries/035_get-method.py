# printing values using get method

books = {'author' : 'Khaled Hosseini', 'name' : 'Kite runner'}

print(books.get('author'))
print(books.get('name'))
print(books.get('publisher', 'Not found.'))
