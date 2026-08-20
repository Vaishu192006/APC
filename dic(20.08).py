#1.Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
d1={"roll no":101,"name":"Vaishnavi","department":"CSE","marks":95}
print("dictionanry:",d1)
#2.Create a dictionary containing employee information and display the value associated with a specified key.
employee = {
    "id": 1001,
    "name": "Rahul",
    "department": "IT",
    "salary": 60000
}
key = "name"
print(employee[key])

# 3. Create dictionary of five products and prices, then add a new product
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Bottle": 200,
    "Pencil": 5
}
products["Notebook"] = 80
print(products)

# 4. Create student marks dictionary and update specified student's marks
marks = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 90
}
marks["Rahul"] = 88
print(marks)

# 5. Create cities and populations, then remove a specified city
cities = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Delhi": 30000000,
    "Kolhapur": 500000
}
del cities["Pune"]
print(cities)

# 6. Create employee IDs and names, then check whether an ID exists
employees = {
    101: "Atharv",
    102: "Rahul",
    103: "Amit"
}
emp_id = int(input("Enter employee ID: "))
if emp_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")

#7.Create a dictionary containing student records and find the total number of key-value pairs.
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 90,
    "Rohit": 75
}
print("Total pairs:", len(students))

# 8. Display all keys, values and key-value pairs
data = {
    "name": "Atharv",
    "age": 20,
    "department": "CSE"
}
print("Keys:", data.keys())
print("Values:", data.values())
print("Key-Value pairs:", data.items())


# 9. Programming languages and their creators
languages = {
    "Python": "Guido van Rossum",
    "C": "Dennis Ritchie",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup"
}
for key, value in languages.items():
    print(key, ":", value)


# 10. Accept five student names and marks from user
students = {}
for i in range(5):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))
    students[name] = mark
print(students)


# 11. Find student with highest marks
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 95,
    "Rohit": 88
}
highest = max(students, key=students.get)
print("Highest:", highest, students[highest])




# 12. Find student with lowest marks
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 95,
    "Rohit": 65
}
lowest = min(students, key=students.get)
print("Lowest:", lowest, students[lowest])


# 13. Calculate average marks
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 95,
    "Rohit": 65
}
average = sum(students.values()) / len(students)
print("Average:", average)


# 14. Character frequency in a string
text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)


# 15. Word frequency in a sentence
sentence = input("Enter a sentence: ")
frequency = {}
for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)

#16.Create two dictionaries and merge them into a single dictionary.
cities = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Delhi": 30000000,
    "Kolhapur": 500000
}
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 95,
    "Rohit": 65
}
merged = {**cities, **students}
print(merged)

# 17. Find common keys in two dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 5, "c": 6, "d": 7}
common_keys = dict1.keys() & dict2.keys()
print("Common keys:", common_keys)


# 18. Find common values in two dictionaries
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 40, "z": 30}
common_values = set(dict1.values()) & set(dict2.values())
print("Common values:", common_values)


# 19. Remove duplicate values while retaining corresponding keys
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
result = {}
for key, value in data.items():
    if value not in result.values():
        result[key] = value
print(result)


# 20. Display dictionary elements in ascending order of keys
data = {
    4: "D",
    1: "A",
    3: "C",
    2: "B"
}
for key in sorted(data):
    print(key, ":", data[key])


# 21. Numbers 1 to 10 and their squares
squares = {}
for i in range(1, 11):
    squares[i] = i ** 2
print(squares)


# 22. Numbers 1 to 20 and squares of even numbers only
squares = {}
for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2
print(squares)


# 23. Frequency of each unique number in a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)


# 24. Integers 1 to 10 and their cubes
cubes = {}
for i in range(1, 11):
    cubes[i] = i ** 3
print(cubes)

# 25. Student management system
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 92
}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All")
    print("6. Highest Marks")
    print("7. Average")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = float(input("Enter new marks: "))
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Student not found")

    elif choice == 5:
        print(students)

    elif choice == 6:
        name = max(students, key=students.get)
        print("Highest:", name, students[name])

    elif choice == 7:
        print("Average:", sum(students.values()) / len(students))

    elif choice == 8:
        break

    else:
        print("Invalid choice")


# 26. Employee salary analysis
employees = {
    "Atharv": 60000,
    "Rahul": 45000,
    "Amit": 75000,
    "Rohit": 52000
}

print("Highest salary:", max(employees.values()))
print("Lowest salary:", min(employees.values()))
print("Average salary:", sum(employees.values()) / len(employees))

print("Employees earning more than 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)


# 27. Product quantity management
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15
}

while True:
    print("\n1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Products Below 10")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product: ")
        quantity = int(input("Enter quantity: "))
        products[name] = quantity

    elif choice == 2:
        name = input("Enter product: ")
        if name in products:
            products[name] = int(input("Enter new quantity: "))
        else:
            print("Product not found")

    elif choice == 3:
        name = input("Enter product: ")
        if name in products:
            del products[name]
        else:
            print("Product not found")

    elif choice == 4:
        name = input("Enter product: ")
        if name in products:
            print(name, ":", products[name])
        else:
            print("Product not found")

    elif choice == 5:
        for name, quantity in products.items():
            if quantity < 10:
                print(name, quantity)

    elif choice == 6:
        break

    else:
        print("Invalid choice")


# 28. Contact management system
contacts = {
    "Atharv": "9876543210",
    "Rahul": "9876501234"
}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == 2:
        name = input("Enter name: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in contacts:
            contacts[name] = input("Enter new phone: ")
        else:
            print("Contact not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
        else:
            print("Contact not found")

    elif choice == 5:
        print(contacts)

    elif choice == 6:
        break

    else:
        print("Invalid choice")


# 29. Book management system
books = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Computer Networks"
}

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display All Books")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        books[book_id] = name

    elif choice == 2:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            print(books[book_id])
        else:
            print("Book not found")

    elif choice == 3:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            del books[book_id]
        else:
            print("Book not found")

    elif choice == 4:
        print(books)

    elif choice == 5:
        print("Total books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid choice")


# 30. Group students according to department
students = {
    "Atharv": "CSE",
    "Rahul": "ECE",
    "Amit": "CSE",
    "Rohit": "IT",
    "Sneha": "ECE"
}

groups = {}

for name, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(name)

print(groups)


# 31. Group words according to their length
words = ["cat", "dog", "apple", "book", "banana", "sun"]
groups = {}

for word in words:
    length = len(word)
    if length not in groups:
        groups[length] = []
    groups[length].append(word)

print(groups)


# 32. Find two numbers whose sum equals target using a dictionary
numbers = [2, 7, 11, 15]
target = 9
seen = {}

for num in numbers:
    complement = target - num
    if complement in seen:
        print("Numbers:", complement, num)
        break
    seen[num] = True


# 33. Find first character that occurs only once
text = input("Enter a string: ")
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break


# 34. Find first character that occurs more than once
text = input("Enter a string: ")
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break


# 35. Word length and number of words having that length
paragraph = input("Enter a paragraph: ")
result = {}

for word in paragraph.split():
    length = len(word)
    result[length] = result.get(length, 0) + 1

print(result)




