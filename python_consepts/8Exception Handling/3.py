try:
    num = int(input("Enter number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Invalid input!")
else:
    print("No errors occurred!")
finally:
    print("Program execution completed.")
