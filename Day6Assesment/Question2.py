import re
password = "Strong@123"
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

text = """hello
WORLD
Python programming"""

pattern_case = r"world"

print("\nWithout IGNORECASE:")
print(re.search(pattern_case, text))

print("\nWith IGNORECASE:")
print(re.search(pattern_case, text, re.IGNORECASE))


pattern_multi = r"^Python"

print("\nWithout MULTILINE:")
print(re.search(pattern_multi, text))

print("\nWith MULTILINE:")
print(re.search(pattern_multi, text, re.MULTILINE))


pattern_dot = r"hello.*Python"

print("\nWithout DOTALL:")
print(re.search(pattern_dot, text))

print("\nWith DOTALL:")
print(re.search(pattern_dot, text, re.DOTALL))
