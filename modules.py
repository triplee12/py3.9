# Navigating folder
# import a module
import glob
import json
import random
import os
import operator
import sys


directory = os.getcwd()
print(f"Current directory: {directory}")

# Change folders
os.chdir(directory)

# ListDir
for f in os.listdir():
    print(f)
    print(f"Path: {os.path.abspath(f)}")
    if os.path.isdir(f):
        print(f"directory: {f}")
    elif os.path.isfile(f):
        print(f"file: {f}")
    elif os.path.islink(f):
        print(f"link: {f}")


# ScanDir
for s in os.scandir():
    print(s)
    print(f"Name {s.name}")
    print(f"Path {s.path}")
    if s.is_dir:
        print(f"Dir: {f}")
    elif s.is_file:
        print(f"File: {f}")
    elif s.is_link:
        print(f"Link: {f}")


# Glob - multiple ways
# Recursive scan

os.chdir('..')
dir = os.getcwd()

for filename in glob.glob(pathname= dir + '**/**', recursive=True):
    print(f"glob: {filename}")

for currentpath, folders, files in os.walk('.'):
    for file in files:
        print(f"Walk: {os.path.join(currentpath, file)}")


# Reading a text file
# Get a filename

print(f"File: {__file__}")
print(f"Args: {sys.argv}")
sfile = os.path.abspath(sys.argv[0])
print(f"Reading: {sfile}")

# Existing
if not os.path.exists(sfile):
    print("Oops, file does not exist")
    exit(1)

# Open file
f = open(sfile, 'r')
# Read a line
line = f.readline()
print("Reading: {line}")
# Read number of letters
chars = f.read(10)
print(f"Chars: *{chars}*")

# Position
print(f"Position: {f.tell()} of {os.stat(sfile).st_size} bytes")

# Seek - move to a position within a file
# Zero based position
f.seek(0, os.SEEK_SET)
# Read all lines
print('----------------------------------------')
for l in f.readline():
    print(l.strip())

# Close file
# Allows other applications to work with it
f.close()


# Write a text file
# Simplify mode usage
def toFile(filename, mode, data):
    f = open(filename, mode)
    for i in range(5):
        f.write(str(i) + ':' + data + '\r\n')
    # f.flush() # Automatically called when file is closed
    f.close()


# Write will overwrite the entire file
def writeFile(filename):
    toFile(filename, 'w', "Python is cool.") 

# Append will add to the end of the file
def appendFile(filename):
    toFile(filename, 'a', "Python is cool and funky.") 


# Read file
def readFile(filename):
    if not os.path.exists(filename):
        print("File does not exist")
        return
    f = open(filename, 'r')
    for line in f.readline():
        print("Reading line")
        print("================================")
        print(line.strip())
    f.close()

quotes = "Keep it simple and not complex"
writeFile(quotes)
appendFile(quotes)
readFile(quotes)

# Reading binary files
def randomBytes(size):
    bytes = []
    for i in range(size):
        bytes.append(random.randrange(0,225))
    return bytes

def displayBytes(bytes):
    print("*"*50)
    for index, item in enumerate(bytes):
        print(f"{index} = {item} ({hex(item)})")
    print("-"*50)

b = randomBytes(20)
displayBytes(b)

# Write bytes
def writeBytes(filename, bytes):
    with open(filename, 'wb') as f:
        for b in bytes:
            f.write(b.to_bytes(1, byteorder="big") + "$0")

# Read bytes
def readBytes(filename):
    bytes = []
    with open(filename, 'rb') as f:
        while True:
            b = f.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder="big"))
    return bytes

# Create a random bytes
outbytes = randomBytes(20)
displayBytes(outbytes)

# write bytes
filename = 'text.txt'
writeBytes(filename, outbytes)

# Read bytes
inbytes = readBytes(filename)
displayBytes(inbytes)
print(f"Match: {operator.eq(outbytes, inbytes)}")


# Working with json files
jsonfiles = 'json.txt'

# To string
outData = dict(name="Ebuka", age=28, pet="dog")
s = json.dumps(outData) #This dump in string format.
print(s)

# To file
with open(jsonfiles, 'w') as f:
    json.dump(outData, f) #This dump in file.

# From string
inData = json.loads(s) # This load the dictionary from string.
print(f"Dictionary = {inData}")

# Load from file
with open(jsonfiles, 'r') as f:
    fD = json.load(f)
print(f"Type: {type(fD)} = {fD}")














