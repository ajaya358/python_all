file = open("example.txt", "a")
file.write("This line was added later.\n")
file.close()

#/read
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
