'''
| Operator | Meaning                   | Example              |
| -------- | ------------------------- | -------------------- |
| `=`      | Assign                    | `x = 5`              |
| `+=`     | Add and assign            | `x += 3 → x = x + 3` |
| `-=`     | Subtract and assign       | `x -= 3`             |
| `*=`     | Multiply and assign       | `x *= 3`             |
| `/=`     | Divide and assign         | `x /= 3`             |
| `%=`     | Modulus and assign        | `x %= 3`             |
| `//=`    | Floor division and assign | `x //= 3`            |
| `**=`    | Exponent and assign       | `x **= 3`            |

'''
# Basic assignment
x = 5  # x becomes 5
print("x =", x)

# Add and assign
x += 2  # x = x + 2 -> 7
print("x += 2 ->", x)

# Subtract and assign
x -= 3  # x = x - 3 -> 4
print("x -= 3 ->", x)

# Multiply and assign
x *= 4  # x = x * 4 -> 16
print("x *= 4 ->", x)

# Divide and assign
x /= 2  # x = x / 2 -> 8.0
print("x /= 2 ->", x)

# Modulus and assign
x %= 3  # x = x % 3 -> 2.0
print("x %= 3 ->", x)

x = 10 
print("Reset x to", x)

# Floor division and assign
x //= 2  # x = x // 2 -> 1.0
print("x //= 2 ->", x)

# Exponent and assign
x **= 3  # x = x ** 3 -> 1.0
print("x **= 3 ->", x)

# Another simple example with a name
name = "Jay"  # name is Jay
name += "aram"  # name becomes Jayaram
print("name ->", name)

