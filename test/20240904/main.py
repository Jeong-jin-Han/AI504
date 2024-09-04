fruits = ['apple', 'banana', 'cherry', 'mango']
print(fruits)

fruits.append('orange') # append for list
print(fruits)

fruits.pop(1) # remove banana, pop for list
print(fruits)

fruits.sort() # sort for list
print(fruits)

book = {
    'title' : '1984',
    'auther' : 'Gerge Orwell',
    'year' : 1949
}

print(book)

book['genre'] = 'Dystopian' # just adding w.r.t dictionary
print(book)

book['year'] = 1950 # chaing the elt w.r.t dictionary
print(book)

book.pop('genre') # remove the elt w.r.t dictionary
print(book)

colors = {'red', 'blue', 'green'}
print(colors)

colors.add('yellow') # add the elt w.r.t set
print(colors)

colors.remove('blue') # remove the elt w.r.t set
print(colors)

print('red' in colors)
print('purple' in colors)

students = ['Alice', 'Bob', 'Charlie']
grades = {'Alice': 90, 'Bob': 85, 'Charlie' : 92}
subjects = {'Math', 'Science', 'History'}

print(students)
print(grades)
print(subjects)