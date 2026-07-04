def total_sum(*args):
    print(args)           # (10, 20, 30)
    return sum(args)

print(total_sum(10, 20, 30))  # 60

#_____________________________________________________________________________________
def display_details(**kwargs):
    print(kwargs)  # {'name': 'Ravi', 'age': 25, 'city': 'Hyderabad'}
    for key, value in kwargs.items():
        print(f"{key} = {value}")

display_details(name="Ravi", age=25, city="Hyderabad")
