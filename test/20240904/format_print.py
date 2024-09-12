name = "John"
print("Hello, my name is %s." % name)

name = "Alice"
age = 25
print("%s is %d years old." % (name, age))

#'.2' means you want to display only two decimal places.
price = 19.99
print("The price of the item is $%.2f" % price)

name = "Bob"
age = 30
height = 5.8
print("%s is %d years old and his height is %.1f feet." % (name, age, height))



"""
The %r format is useful for debugging because it uses the "representation" of an object 
(the way Python sees the object internally).
"""

name = "Eve"
age = 27
print("Name: %r, Age: %r" %(name, age))


num = 255
print("The number %d in hexadecimal is %x and in octal is %o." % (num, num, num))



"""
Here:

%2d reserves at least 2 spaces for the number i.
%4d reserves at least 4 spaces for the square of i.
"""

for i in range(1, 6):
    print("%2d: %4d" %(i, i ** 2))



"""
Explanation:
%s is for "string" formatting. It displays the object as a user-friendly string.
%r is for "representation" formatting. It displays the internal, or "raw", representation of the object, which is often useful for debugging.


name = "Eve"
print("Using %%s: %s" % name)  # %% is used to escape % in the string.
print("Using %%r: %r" % name)


Using %s: Eve
Using %r: 'Eve'
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return "Person named %s" % self.name
    
    def __repr__(self):
        return "Preson('%s', %d)" % (self.name, self.age)
    
p = Person("Alice", 30)
print("Using %%s: %s" % p)
print("Using %%r: %r" % p)

"""
Using %s: Person named Alice
Using %r: Preson('Alice', 30)
"""

