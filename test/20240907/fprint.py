name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

a = 10
b = 20

print(f"The sum of {a} and {b} is {a + b}.")

def greet(name):
    return f"Hello, {name}!"

name = "Bob"
print(f"{greet(name)} How are you today?")

price = 19.98765
print(f"The price of the item is ${price: .2f}.")

for i in range(1, 6):
    print(f"Number: {i:<2} | Square: {i**2:<3} | Cube: {i**3:<4}")

"""
Explanation:

<2 aligns the number to the left within 2 spaces.
<3 and <4 do similar left-aligning for squares and cubes,
 with enough spaces reserved for each value.
"""

student = {'name': 'Charlie', 'age': 22, 'grade': 'A'}
print(f"{student['name']} is {student['age']} years old and got a grade of {student['grade']}.")

name = "Dave"
age = 30
bio = f"""
Name: {name}
Age: {age}
Occupation: Engineer
"""

print(bio)


from datetime import datetime
now = datetime.now()
print(f"The current date and time is {now:%Y-%m-%d %H:%M:%S}.")


temperature = 25
print(f"The weather is {'hot' if temperature > 30 else 'pleasent'}.")


value = 10
print(f"The result is {{value}}.")

"""
Summary of Key Features:
Variable substitution: You can embed variables directly in f-strings.
Expressions: Perform operations inside the f-string.
Formatting: You can control number formatting, like floating-point precision.
Alignment: Left, right, and center alignment are possible with padding.
Conditional logic: Include conditions and simple logic directly in the f-string.

"""

