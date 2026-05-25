# LESSON 3 - LOOPS
name = "Dan"

# For loop
for i in range(5):
    print("Hello", name, "number", i)

# While loop
count = 1
while count <= 5:
    print("Round", count)
    count = count + 1

# Countdown challenge
for i in range(10, 0, -1):
    print(i)
print("Blast off!")

# Even numbers
for i in range(0, 11):
    if i % 2 == 0:
        print(i)
