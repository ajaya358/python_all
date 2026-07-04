class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Eligible to vote!")

try:
    check_age(16)
except InvalidAgeError as e:
    print("Custom Error:", e)
