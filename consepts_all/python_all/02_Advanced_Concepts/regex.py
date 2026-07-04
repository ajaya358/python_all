import re

text = "My email is ajay@example.com and ravi@example.org"
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)
print(emails)

phone = "Call me at 9876543210"
match = re.search(r"\d{10}", phone)
if match:
    print("Phone number found:", match.group())
