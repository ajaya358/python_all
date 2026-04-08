file = open("example.txt", "r")

# Read entire content
content = file.read()
print(content)

file.close()

#---------read 2nd method
file = open("example.txt", "r")

print(file.readline())  # Reads one line
print(file.readlines()) # Reads all lines as list

file.close()
