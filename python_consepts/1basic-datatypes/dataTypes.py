
'''int(), float(), str(), list(), tuple(), set()'''
# int
x = 10
y = -5
print(type(x))
print(x)

# float
a = 3.14
b = -2.5
print(type(a))
print(a)

# complex — Complex numbers
z = 2 + 3j
print(type(z))
print(z.imag)
print(z.real)

# string
name = "Jayaram"
greeting = 'Hello'

print(name)
print(type(name))
print(name[0])
print(name[0:4])

print(name + " Reddy")  # Concatenation
print(name * 2)  # Repetition
print(len(name))  # Length

# boolean
is_active = True
is_logged_in = False

print(type(is_active))  # <class 'bool'>
print(is_active and is_logged_in)  # False

#Tuples
colors = ("red", "green", "blue")
print(colors[0])  # red

#set
numbers = {1, 2, 3, 2}
print(numbers)  # {1, 2, 3} — duplicate removed
numbers.add(4)
print(numbers)

# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # banana
fruits.append("orange")  # Add element
print(fruits)
fruits[0] = "mango"  # Modify element
print(fruits)

#dict (Dictionaries)
person ={"name":"jai","age":25,"city":"Kuppam"}
print(person["name"]) #jai
print(person.get("email", "Not found"))  # Not found
person.update({"age": 26, "city": "Paris"})
print(person)  # {'name': 'jai', 'age': 26, 'city': 'Paris'}

# Data Types Example
name = "Jayaram"  # string
age = 28          # int
height = 5.9      # float
is_student = True # boolean
fruits = ["apple", "banana", "cherry"]  # list

print(f"My name is {name}, I am {age} years old, my height is {height}")
print(f"Am I a student? {is_student}")
print(f"My favorite fruit is {fruits[0]}")

