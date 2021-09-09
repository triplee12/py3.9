# Define a function
def pet(): # Function must start with def keyword and function name must end with bracket.
    print("This is a function")
pet() # Calling a function

# Define a function with parameter and return a value
def sqft(w,h): # w,h is a parameter
    v = w * h
    return v
total = sqft(12,12) # 12,12 is an argument
print(total)

# Function and scope
# Global scope
name = "Ebuka" # Globale variable name
def call_name():
    print(f"My name is {name}")
call_name()

x = 20 # Globale variable name
def addition():
    x = 50 # Local variable name
    print(f"Function scope local variable {x}")
addition()
print(f"global variable {x}")

# Function do not share scope with other
def dog():
    d = 2 # Only exists in this function
    
def cat():
    c = 3 # Only exists in this function

# Function can return values
def num(steps):
    r = range(1, 30,steps)
    for i in r:
        print(i)
    return r

def lottery():
    z = num(7) # call num() function in lottery
    for i in z:
        print(f"Lucky number {i}")

lottery()


# Function in depth
#  Position and keyword arguments
def message(name, msg, age):
    print(f"Hello {name}, {msg}, you're {age} years old.")
message("Ebuka", "Looking good", 28) # Positional
message(msg="You are awesome", name="Ebuka", age=28) # Keyword arguments

# Internal Function
def counter():
    def display(count = 0): # Internal function
        print(f"Internal counter: {count}")
        
    for x in range(5):
        display(x)
counter()

# *args: positional argument
def divide(*args):
    x = 4
    for num in args:
        print(f"Num = {num}")
        x /= num
    print(f"Divide: {x}")
divide(6, 7, 8,9)

# **kwargs: positional argument is used to pass keyword arguments
def profile(**person):
    print(person)
    def display(p):
        if p in person.keys():
            print(person[p])
    display('name')
profile(name="Ebuka", age=28)

# lambda Function - anonymous function
sqftb = lambda width = 10, height = 30: width * height
print(sqftb(40, 20))

# Packing and unpacking data
# Problem with *args and **kwargs is that we can not use lists and dictionaries
# Instead we have to pack and unpack data

# Packing data
def pack(*nums):
    print(f"Packed: {nums}")
    for num in nums:
        print(f"Packed: {num}")
pack(3,4,5,6,7,8,9,10,11,12,13,14,15)

# Unpacking data
def unpack(a,b,c):
    print("Unpacked")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

num = [1, 2, 3]
unpack(*num)

# Dictionary issues
d = dict(name="Ebuka", age=28, pet="dog")
print(f"Packing dictionary")
pack(*d)

print(f"Unpacking dictionary")
unpack(*d)

# Packing Dictionary
def packDict(**nums):
    print(f"Nums = {nums}")
    for k in nums:
        print(f"Packed: {k} = {nums[k]}")

packDict(name="Ebuka", age=28, pet="dog")

def UnpackDict(name, age, pet):
    print("Unpacking dictionary")
    print(f"name = {name}")
    print(f"age = {age}")
    print(f"pet = {pet}")

UnpackDict(**d)

# Function and arguments
# Function in argument
def test(name, age, pet):
    print(f"name = {name}")
    print(f"age = {age}")
    print(f"pet = {pet}")

def getData():
    return dict(name="Ebuka", age=28, pet="dog")

d = getData()
test(d['name'], d['age'], d['pet'])
test(**getData())

# Function as an argument
def cool(data):
    d = data()
    print(d)
    print(f"Name = {d['name']}")
    print(f"Age = {d['age']}")
    print(f"Pet = {d['pet']}")


cool(getData)

# Global
# Global keyword which allows code to modify a variable
# Outside of the scope

x = 12
def test():
    x = 13 # Only exists in this function
    print(x)

test()
print(x)

# Global variable
counter = 0

# Scope issues
def count(max):
    # With "global"
    global counter # This will throw an exception if not declared global
    counter += 1
    if counter >= max:
        return False
    return True
    
count(100)

limit = 10
for x in range(limit):
    b = count(limit)
    print(b)


# Walus operator and global
# Added in Python 3.8 looks like this: :=

# Assign a variable from an expression
# Common issues ()
# y := len("Hello") # Invalid syntax
(y := len("Hello")) # Valid syntax
print(y)

people = ["Ebuka", "Emmanuel", "John"]
if n := len(people) <= 3:
    print(n)

if (n := len(people)) <= 3:
    print(n)


# Simple example
lines = []

def canAdd(max = 5):
    global lines
    if allowed := (count := len(lines)) < max:
        print(f"Yan can enter {max - count} more")
    return allowed

while canAdd():
    lines.append(l := input("Enter a line: "))
print(f"You entered: {lines}")


# Main function
print(f"Name: {__name__}")
print(f"File: {__file__}")

# Create some code
def test1():
    print("This is a test function one")

def main():
    print("This is a main function")
    test1()

# Run automatically
if __name__ == "__main__":
    main()



























