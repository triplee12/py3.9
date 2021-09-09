# What is variable?
# Variable is a container that holds values: like 'x' is a variable that contains '5 * 5'.
x = 5 * 5
print(x)

# Data types are:
# 1. float
# 2. string
# 3. boolean
# 4. integer
# 5. complex: list, array, set, tuple, or dictionary


# boolean are of two types: True and False.
y = True
z = False
print(f'y = {y}')
print(f'z = {z}')
print(f'Equal: {y == z}')
print(f'Not Equal: {y != z}')

# integer Type is numerical like '1, 2, 30, 004, 235
my_integer = 123
print(f'my_integer = {my_integer}')

comNumbers = complex(10,  5)
print(f'comNumbers for real = {comNumbers.real}, comNumbers for imag = {comNumbers.imag}')

a = 5
b = a + 10
print(f'Addition = {b}')
c = b - 2
print(f'Subtraction = {c}')
d = c * 5
print(f'Multiplication = {d}')
e = d / 2
print(f'Division = {e}')
f = e % d
print(f'Modulus = {f}')
g = f ** c
print(f'Expontential = {g}')
h = g // f
print(f'Floor Division = {h}')

#  String: string is any character weather aphabet or number enclose in quote. like examples below
my_string = 'a b c def'
print(f'my_string = {my_string}')

my_num_string = '012345' # '012345' is a string not integer

for i in 'hello': 
    print(f'{i} = {ord(i)}') # 'hello' in for loop is a string


# Working with escaped characters - starts with slash \
# \r: carriage return: returns next character to a new line
carriage = 'Hello\rWorld'
print(f'carriage = {carriage}')

# \t: Tab gives 4 spaces before 
tab = 'Hello\tWorld'
print(f'tab = {tab}')

# There are so many escape characters which we will not discuss here.
# But we will use some in the future; just know that any character follows slash (\) is an escape character.

# Working with formatting
name = "Immanuel"
age = 28
# print(name + ' ' + age) # This will throw an error because python is loosely typed.
# And python will always try to add "name" to "age" as integer. 

"""Using format 'f{}' to format a string and integer at same time to produce expected result. """
print(f'name = {name} and age = {age}') 
print("My name is %s, I am %s years old" %(name, age)) 


# Basic String operations
desc = "My name is Emmanuel, I am 28 years old."
print(f"length of desc '{desc}': is ", len(desc)) # len keyword is used to get the length.
print("Replace: ", desc.replace("Emmanuel", 'Immanuel')) # replace keyword is used to replace word(s) in string.
print("Split: ", desc.split()) # split keyword is used to split word(s) in string into segments or words and returns news array.
print("Sartswith: ", desc.startswith('My')) # startswith returns True if the string starts with 'My' and return False otherwise.
print("Endswith: ", desc.endswith('old.')) # endswith returns True if the string ends with 'old' and return False otherwise.
print("Uppercase: ", desc.upper()) # upper returns all letters to uppercase.
print("Lowercase: ", desc.lower()) # lower returns all letters to lowercase.
print("Capitalize: ", desc.capitalize()) # capitalize returns first letter to uppercase.

# Let's talk about slicing in python
print("Slicing: ", desc[0:8]) # This returns new string starting from index[0] to index[9] 
print("Slicing: ", desc[2:]) # This returns new string starting from index[3] to the end. 
print("Slicing: ", desc[-8]) # This returns the last words at index[-8]

# Let's talk  about the index position
# How can you find index of words without actually knowing the index position.
toFindIndex = desc.find("My name is Emmanuel") # find is used to get the index position and returns -1 if not found.
print("Find: 'My name is Emmanuel' is at index", toFindIndex)
toFindIndex = desc.find("name is Emmanuel") # find is used to get the index position and returns -1 if not found.
print("Find: 'name is Emmanuel'", toFindIndex)
toFindIndex = desc.find("is Emmanuel") # find is used to get the index position and returns -1 if not found.
print("Find: 'is Emmanuel' is at index", toFindIndex)
toFindIndex = desc.find("Emmanuel") # find is used to get the index position and returns -1 if not found.
print("Find: 'Emmanuel' is at index ", toFindIndex)
getIndex = desc.index('o') # It will return error if index is not found.
print("Index: of o = ", getIndex)


# List [] is a complex data type. It's a collection of data types.
# Example [1, 0, 10, 'apple', 'orange']. List can contain any thing.
names = ['apple', 'orange']
print('List of name ', names)
mixList = ['Ebuka', 3, 'orange', 10, 7, 'apple', 'orange']
print('List of mix list ', mixList)

# Index and positioning - zero based
print(f'Zero: {mixList[0]}') # print the first item which is at index 0 of mixlist.
print(f'Third: {mixList[3]}')

# Adding item - append, insert
mixList.append('Burgar') # append adds item to the end(last) of the list.
mixList.append('Pizza')
print(mixList)
mixList.insert(4, 'Cat') # insert adds item to the specific index
print(mixList)

# Removing items from list - remove, pop, delete
mixList.remove(10) # remove removes item from a specific position
print(mixList)
l = mixList.index('orange') # This will throw an error if not found the item
print(f"Item: {mixList.pop(l)}") # This will removes item 'orange' from the lists and returns the item
print(f"Lists: {mixList}") # Note: In the lists the first orange found at the index of 2 was removed.

n = mixList.index("apple") # Getting index of apple, this will throw an error if not found
del mixList[n] # This will delete the item without returning it
print(mixList)

# Extending a list - Adds elements from another list
programming_lang = ['python', 'java', "c++", "js", "R"]
print(f"Programming languages: {programming_lang}")
"""Let's extend the mixList with the programming_lang list"""
mixList.extend(programming_lang) # This adds "programming_lang" list to "mixList" list
print(f"New list of mixList: {mixList}") # Here is our new list after adding "programming_lang".

# Sorting - sort, reverse
# mixList.sort() # This will sort element alphabetically and throw an error if tried to sort integer and string together
# print(f"Sorted mixList: {mixList}")
programming_lang.sort() # Sort accending order
print(f"Sorted programming_lang: {programming_lang}")

programming_lang.reverse() # Sort decending order
print(f"Reverse programming_lang: {programming_lang}")

# Making copy of a list
languages = programming_lang.copy() # Copies the elements into a new list
print(f"Languages: {languages}")
# You can now modify the new list 
languages.append("Qbasic") # Here we modified the elements in the languages list which didn't affect the main list.
print(f"Languages: {languages}")
print(f"Programming_lang: {programming_lang}") # Note the main list here was not modified.

# Deleting the whole list
# del languages
print(languages) # This will throw an error; saying languages is not defined

# Clearing elements of a list
languages.clear() # This will clear the whole elements and returns an empty list
print(languages)

# Creating lists in lists; like [[], [], []] list can contains other lists
course = ["s"]
numbers = [1, 2, 3, 4]
programming_lang = ['python', 'java', "c++", "js", "R"]
course.append(numbers) # This will create new lists inside course list
print(f"Lists in lists: {course}")
course.append(programming_lang)
print(f"New lists: {course}")

# To read lists of lists
print(course[0][0]) # This will return first element of first(index 0) list of lists
print(course[1][3]) # this will return fourth element of second list of lists
print(course[2][1]) # this will return second element of third list of lists


# Changing item - positional(index)
course[0] = "Python 101" # This will change element at index 0 of the list.
print(course)


# Sets {}
# Set contains unordered, unique, immutable data ttpes in a hash table
sets = {} # Empty set

s = {1,2,3,4,5,6,7,7,7,7,8,9,10} # Remember: set is unique meaning we can not have two the same elements in a set.
print(s) # this will return new set

# Converting list into set
my_name__age = ["Ebuka", "Ejie", 28]
na = set(my_name__age) # This will convert "my_name__age" into set
print(na)

# Adding items in a set
na.add("Python is fun") # This will add "Python is fun" in the "na" set
na.update(["a", "b", "c"]) # likewise update
print(na)

# Removing items from a set
na.discard("a") # This will remove "a" from the set and returns a new set
print(na)
na.remove("b") # This will remove "b" and returns a new set; and throws an error if not found
print(na)
na.pop() # This will remove an item and returns it back
print(na)


# Tuple: is a fast list that can not be modified
# Create a tuple
t = () # Empty tuple
print(t)
t = (1,2,3,4,5)
print(t)

# Access elements in a tuple
print(f"Index: {t[1]}")
print(f"Slice: {t[2:]}")
print(f"Boolean: {3 in t}")

# Assignment
(x, y, z) = (1, 2, 3) # Here x is assigned to 1, likewise other veriables assigned to 2, 3 respectively
print(x)
print(y)
print(z)


(x, y, z) = range(3) # But down to this, python treats x, y, and z as tuple, which will throw an error if tried to print values more than 3 ranges because veriable are only three.
print(range(3)) # Here this will print range(0, 3) meaning that python sees it as loop
print((x, y, z))
print(x)
print(y)
print(z)

# Dictionary - index by keys {k:v, k:v} where k = key and v = value
# Create a dictionary
my_pet = {'pet':'cat', 'age': 10, "name":"spew"}
print(my_pet)
my_pet1 = dict(pet="dog", age=13, name="Jasper")
print(my_pet1)
# Get keys and values
print(f"Items: {my_pet.items()}") # This will return list keys and their values.
print(f"keys: {my_pet.keys()}") # This will return keys of my_pet
print(f"values: {my_pet.values()}") # This will return values of my_pet
# Getting values from keys
print(my_pet["pet"]) # This will return the pet and will throw an error if the key is not found
# Add an item
my_pet1["Eyes"] = "blue"
print(my_pet1)
# Removing item
del my_pet1["Eyes"]
print(my_pet1)

if "name" in my_pet1:
    print(my_pet["name"])
    for key in my_pet1.keys():
        print(f"Keys in my_pet1: {key}")
    for value in my_pet1.values():
        print(f"values in my_pet1: {value}")

for key in my_pet.keys():
    print(f"{key} = {my_pet[key]}") # If you want to print keys with their values in a for loop

# Flow control using if else elif statement
#  if condition
me = False
if me:
    print("Go on and code.") # This will print only me is true otherwise it moves to else condition
else:
    print("Please, you're not suppose to be here.")
    
# Condition evaluation {True - run} {False - not run}
num1 = 200
num2 = 100
if num1 == num2: print("Equal To") # Here our code will not run because we cound not met the condition
if num1 != num2: print("Not Equal To") # Here our code will run perfectly
if num1 < num2: print("Less than") # Here our code will not run
if num1 > num2: print("Greater than") # Here our code will run
if num1 >= num2: print("Greater than or equal to") # Here our code will run
if num1 <= num2: print("Less than or equal to") # Here our code will not run

# elif condition
num3 = 5
if num3 == 15:
    print("num3 is 15")
elif num3 == 20:
    print("num3 is 21")
elif num3 == 25:
    print("num3 is 25")
else:
    print(f"Oops num3 is: {num3}")

# Nested statement
num = 90
if num > 50:
    print("num is greater than 50")
    if num > 60:
        print("num is greater than 60")
        if num > 70:
            print("num is greater than 70")
            if num > 80:
                print("num is greater than 80")
else:
    print("num is less than 50")
    
# while loop - running code until conditions are not met 
num = 0
while num < 100:
    num += 1
    print(f"num = {num}")
print("Complete!")
# pass
while num < 10:
    pass # This tells python to leave a program and continue with its normal work
print("We used pass")
# continue and break
num = 1 
while True: # This code will run forever
    num += 1
    if num < 5:
        print(f"num < 5: {num}")
        continue # this tell python to continue with the program
    print(f"Oops")
    break # this tells python to leave the while loop block 
print("Complete!")

# for loop
# for loop on lists, tuples, sets
x = [1,2,3,4,5,6,7,8,9] # list
y = (1,2,3,4,5,6,7,8,9) # tuple
z = {1,2,3,4,5,6,7,8,9} # set
for i in x: # for loop has beginning and end
    print(f"list: i is {i}")

for i in y: # for loop has beginning and end
    print(f"Tuple: i is {i}")

for i in z: # for loop has beginning and end
    print(f"Set: i is {i}")

# for loopon dictionary
m = dict(ebuka=28, emmanuel=30, john=40, daniel=50)
print(m)
for k in m.keys():
    print(f"{k} is {m[k]} years old.")
    
for k,v in m.items():
    print(f"{k} is {v} years old.")


# Range
p = range(9)
print(p)
for i in p:
    print(i)

# Range start, stop and step
p = range(1,10,2)
for i in p:
    print(i)














































































































