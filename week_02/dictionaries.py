# LESSON 6 - DICTIONARIES

myself = {
    "name": "Dan",
    "age": 19,
    "course": "Computer Science",
    "hobby": "guitar",
    "school": "your school here"
}

for key, value in myself.items():
    print(f"{key}: {value}")


grades = {
    "Math": 85,
    "English": 90,
    "Science": 78,
    "Filipino": 88,
    "PE": 95
}
print("\nSubjects above 85:")
for k, v in grades.items():
    if v > 85:
        print(f"outstanding! {k} with a grade of {v}")


# CONTACT BOOK WITH SEARCH

contacts = {
    "jayden": 324567,
    "mark": 886431,
    "jason": 929929
}

search = input("\nEnter contact name: ")

if search in contacts:
    print(f"The contact number is {contacts[search]}")
else:
    print("Nothing found!")
