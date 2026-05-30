
# LESSON 5 - LISTS

fruits = ["pomelo", "watermelon", "lemon", "pear", "banana"]
fruits.sort()
for fruit in fruits:
    print(fruit)


numbers = [5, 3, 8, 1, 9, 2]

print(f"First item: {numbers[0]}")
print(f"Last item: {numbers[-1]}")
print(f"Total items: {len(numbers)}")

# Add item
numbers.append(10)
print(f"After append: {numbers}")

# Remove item
numbers.remove(3)
print(f"After remove: {numbers}")

# Sort list
numbers.sort()
print(f"After sort: {numbers}")
