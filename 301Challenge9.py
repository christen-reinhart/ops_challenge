#!/usr/bin/env python3


# Variables
a = 5
b = 10

# If statement using the equals conditional
if a == b:
    print("a is equal to b")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# If statement with and between conditions
if a > 0 and b > 0:
    print("Both a and b are positive")

# If statement with or between conditions
if a == 5 or b == 5:
    print("Either a or b is equal to 5")

# Nested if statement
if a > 0:
    if b > 0:
        print("Both a and b are positive")
    else:
        print("a is positive, but b is not")

# If statement with pass to avoid errors
if a < 0:
    # Placeholder for future code
    pass
else:
    print("a is not negative")