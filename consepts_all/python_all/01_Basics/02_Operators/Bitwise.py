'''
| Operator | Meaning     | Example       |    |        |
| -------- | ----------- | ------------- | -- | ------ |
| `&`      | AND         | `5 & 3 = 1`   |    |        |
| `        | `           | OR            | `5 | 3 = 7` |
| `^`      | XOR         | `5 ^ 3 = 6`   |    |        |
| `~`      | NOT         | `~5 = -6`     |    |        |
| `<<`     | Left shift  | `5 << 1 = 10` |    |        |
| `>>`     | Right shift | `5 >> 1 = 2`  |    |        |

'''

x = 5  # 0b0101
y = 3  # 0b0011

print(x & y)  # 1
print(x | y)  # 7
print(x ^ y)  # 6
print(~x)     # -6
print(x << 1) # 10
print(x >> 1) # 2
