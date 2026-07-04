# Conditional Statements (if, elif, else)
x = 15
if x < 10:
    print("x is less than 10")
elif x < 20:
    print("x is less than 20")
else:
    print("x is greater than 20")

# Loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating with range():
print("range")
for i in range(5):
    print(i)

# while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

#break → exit the loop early
print("break")
for i in range(10):
    if i == 5:
        break
    print(i)

#continue → skip the current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

#pass → placeholder, does nothing
for i in range(3):
    pass  # TODO: implement later
print("Loop finished")
