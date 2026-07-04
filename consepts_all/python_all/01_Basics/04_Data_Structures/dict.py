# Creating a dictionary
student = {
    "name": "Ravi",
    "age": 22,
    "course": "Python"
}

# Access value
print(student["name"])  # Ravi

# get() → safe access
print(student.get("age"))  # 22

# update() → modify or add
student.update({"age": 23, "city": "Hyderabad"})
print(student)
# {'name': 'Ravi', 'age': 23, 'course': 'Python', 'city': 'Hyderabad'}

# keys() and values()
print(student.keys())    # dict_keys(['name', 'age', 'course', 'city'])
print(student.values())  # dict_values(['Ravi', 23, 'Python', 'Hyderabad'])
