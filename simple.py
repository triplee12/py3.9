# Simple app - calculator

print("Paint calculator")
print("Enter a wall size as width, height in feet or press enter to stop")
print("example: 12,8")
walls = []
gallons = 1 / 360
total = 0
while True:
    user_input = input("Enter a wall size  ")
    if len(user_input) == 0:
        break
    # Verify input
    sqft = user_input.split(',')
    if len(user_input) < 2:
        print("Invalid format")
        break
    # Convert the string to integer
    width = int(sqft[0])
    height = int(sqft[1])
    item = [width,height]
    walls.append(item)
    print(f"Calculating wall: {item}")

print(f"You entered {walls}")
for m in walls:
    w = m[0]
    h = m[1]
    s = w * h
    v = s * gallons
    total += v
print(f"You need to buy {round(total,2)} gallons of paint")