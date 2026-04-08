'''
| Mode   | Meaning      | Description                                      |
| ------ | ------------ | ------------------------------------------------ |
| `'r'`  | Read         | Opens file for reading (error if not found)      |
| `'w'`  | Write        | Overwrites if file exists, creates new otherwise |
| `'a'`  | Append       | Adds new data at the end of file                 |
| `'x'`  | Create       | Creates new file, error if exists                |
| `'r+'` | Read + Write | Both reading and writing                         | '''

# Write mode ('w') - overwrites file
file = open("example.txt", "w")
file.write("Hello, Jayaram!\n")
file.write("Learning Python file handling.\n")
file.close()
