# Prompt the user to enter 5 names
names = []

for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

# Print each name in uppercase using a for loop and f-strings
for name in names:
    print(f"{name.upper()}")