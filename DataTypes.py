# Collection Data Types
"""
List in Python

List[:] - Prints everything
List[0:] - prints from 0
List[0:4] - prints from 0 to 3, but 4 is not included

Methods: len ()
         extend ()
         insert ()
         remove ()
         pop ()

students = ["John", "Jane", "James"]
print(students)

# The list() constructor
students = list((["John", "Jane", "James"]))

print(students)


"""

items = ["Wabz", 34, True, 3.142, 67, "Caleb"]
items[5] = "Brenda" # Replaces the specified value

items.insert (6, False) # insert() method inserts an item at the specified index

items.append("Wizar") # append() method adds an item to the end of the list

# items.insert (8, 89)
items.pop (0)
items.remove (True)

print (items)

"""
print (items[0])
print (items[3])
# print (items[-1])
print (items[0:])
print (items[0:4])

"""