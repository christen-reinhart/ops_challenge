# Assign a list of ten string elements to a variable
my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Print the fourth element of the list
print("Fourth element:", my_list[3])

# Print the sixth through tenth element of the list
print("Sixth through tenth elements:", my_list[5:10])

# Change the value of the seventh element to “onion”
my_list[6] = "onion"

# Print the updated list
print("Updated list:", my_list)

# Stretch Goals (Optional Objectives)
# Use Python methods to manipulate the list

# append()
my_list.append("mango")

# clear()
# Commenting this out to preserve the list for other operations
# my_list.clear()

# copy()
copied_list = my_list.copy()

# count()
count_of_onion = my_list.count("onion")
print("Count of 'onion':", count_of_onion)

# extend()
extension_list = ["papaya", "quince"]
my_list.extend(extension_list)

# index()
index_of_lemon = my_list.index("lemon")
print("Index of 'lemon':", index_of_lemon)

# insert()
my_list.insert(2, "blueberry")

# pop()
popped_element = my_list.pop(4)

# remove()
my_list.remove("date")

# reverse()
my_list.reverse()

# sort()
my_list.sort()

# Print the final list after all operations
print("Final list:", my_list)

# Create one tuple
my_tuple = ("apple", "banana", "cherry")

# Create one set
my_set = {"apple", "banana", "cherry"}

# Create one dictionary
my_dict = {"fruit1": "apple", "fruit2": "banana", "fruit3": "cherry"}

# Print the tuple, set, and dictionary
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)