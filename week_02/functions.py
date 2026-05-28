# LESSON 4 - FUNCTIONS

def greet(name):
    """Takes a name and prints a welcome message."""
    print(f"Hello {name}, welcome to Python!")

greet("Dan")

# FUNCTION WITH RETURN
def square(num):
    """Takes a number and returns it multiplied by itself."""
    return num * num

result = square(4)
print(f"Square of 4 is: {result}")

# FUNCTION WITH CONDITION TYPES
def is_even(number):
    """Takes a number and returns True if even, False if odd."""
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False


# FUNCTION IF I ADD A LOOP
def countdown(start):
    """Counts down from start to 1 then prints Blast off."""
    for i in range(start, 0, -1):
        print(i)
    print("Blast off!")

countdown(10)
