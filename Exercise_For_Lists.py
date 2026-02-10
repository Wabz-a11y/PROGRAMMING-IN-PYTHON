# Exercise for Lists

"""
Create a Python program that prompts the user to enter a list of names.
After receiving the input, the program should sort the names in alphabetical orde, remove any duplicates,
and then display the final sorted list.
Additionally, count and print the total number of names entered by the user.
"""
"""
names = []


name1 = (input("Enter the list of names: "))
name2 = (input("Enter the list of names: "))


names.append (name1)
names.append (name2)

for name in names: {
    name>=3

}

print (names)
"""

names = []

total = int(input("How many names do you want to enter? "))

for i in range(total):
    name = input("Enter name: ")
    names.append(name)

# Remove duplicates
names = list(set(names))

# Sort alphabetically
names.sort()

print("\nFinal sorted list (no duplicates):")
print(names)

print("Total unique names:", len(names))


