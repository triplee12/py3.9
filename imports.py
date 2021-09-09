# Imports
# Import makes our code usable to other programs.
# This also allows us to structure our code and simplify things.

# Create a file
# Check animals.py

# import as
import animals as anim
from modu import testy

print(anim.name)
anim.callName()

anim.name = "Jasper"
anim.callName()
anim.toFile("test.txt")

anim.name = "Tiko"
anim.callName()

anim.fromFile("test.txt")
anim.callName()

testy.doTest()

# Call code
def main():
    testy.doTest()

if __name__ == "__main__":
    main()