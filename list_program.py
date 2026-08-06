#1.Write a Python program to create a list of five fruits and display the list.
lst=["Apple","banana","Mango","Cherry","Puppya"]
print("List element:",lst)

#2.Create a list of five integers. Display:
#•First element 
#•Last element 
#•Third element
lst=["Apple","banana","Mango","Cherry","Puppya"]
print("First Element:",lst[0])
print("First Element:",lst[4])
print("First Element:",lst[3])

#3.Create a list of colors. Replace the third color with another color and display the updated list.
lst1=["Red","Black","Orange","White","Pink","Blue"]
print("List element:",lst1)
lst1[3]="Brown"
print("updated list:",lst1)

'''4.Create a list of numbers. Add:
•One element at the end 
•One element at the beginning 
•One element at a specified position 
Display the updated list.'''
lst1=[10,20,30,40,50,60]
lst1.append(70)
print("Element at the end:",lst1)
lst1[0]=66
print("Elment at the beginning:",lst1)
lst1.insert(3,44)
print("Element at the specific position:",lst1)

'''5.	student names. Remove:
•	First student 
•	Last student 
•	A specific student by name'''
lst=["Vaishnavi","Madhura","Shravni","Piyusha","Priyanka","Shreya"]
lst.pop(0)
print("After removing first element:",lst)
lst.pop()
print("After removing last element:",lst)
lst.remove("Priyanka")
print("After removing specefic name:",lst)

#6.Write a program to find the largest and smallest number in a list without using max() or min().
num1= [25, 10, 45, 5, 30]
largest = num1[0]
smallest = num1[0]
for num in num1:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num
print("Largest number:", largest)
print("Smallest number:", smallest)

'''.Accept 10 numbers from the user and store them in a list. Calculate:
•Sum 
•Average'''
numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
total = sum(numbers)
average = total / 10
print("Sum:", total)
print("Average:", average)

'''8.	Store 15 integers in a list. Count how many numbers are:
•	Even 
•	Odd'''
numbers = []
even = 0
odd = 0

for i in range(15):
    num = int(input("Enter number: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
#9.Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
cities = ["Pune", "Mumbai", "Karad", "Kolhapur", "Satara"]

city = input("Enter city name: ")

if city in cities:
    print("City exists in the list")
else:
    print("City does not exist in the list")
#10.Write a program to reverse a list without using the reverse() method.
numbers = [10, 20, 30, 40, 50]

reversed_list = numbers[::-1]

print("Original List:", numbers)
print("Reversed List:", reversed_list)

'''11.	Create a list of 10 numbers and display:
•	First 5 elements 
•	Last 5 elements 
•	Middle 4 elements 
•	Alternate elements 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]'''

print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[-5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])

#12.Display all elements present at even index positions.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Elements at even index positions:")

for i in range(0, len(numbers), 2):
    print(numbers[i])
#13.	Accept 10 numbers and sort them in:
#•	Ascending order 
#•	Descending order
numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)
#14.Create a list containing duplicate values and display only unique elements.
numbers = [10, 20, 30, 20, 40, 10, 50, 30]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original List:", numbers)
print("Unique Elements:", unique)

#15.Find the second largest element in a list.
numbers = [10, 50, 20, 40, 30]
numbers.sort()
print("Second largest element:", numbers[-2])

'''16.Create a nested list storing:
•Student Name 
•Roll Number 
•Marks 
Display all student details.'''
students = [
    ["Amit", 101, 85],
    ["Rahul", 102, 78],
    ["Sneha", 103, 92]
]
for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()
#17.Create two 3 × 3 matrices using nested lists and perform matrix addition.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(3):
    for j in range(3):
        result[i][j] = A[i][j] + B[i][j]

print("Matrix Addition:")
for row in result:
    print(row)

'''18.Create a shopping cart using a list.
Perform:
•	Add item 
•	Remove item 
•	Search item 
•	Display cart 
•	Count total items'''

cart = ["Milk", "Bread", "Rice"]

# Add item
cart.append("Sugar")
print("After adding:", cart)
# Remove item
cart.remove("Bread")
print("After removing:", cart)
# Search item
item = input("Enter item to search: ")

if item in cart:
    print("Item found")
else:
    print("Item not found")
# Display cart
print("Shopping Cart:", cart)
# Count total items
print("Total items:", len(cart))

'''19.Store names of students present in class.
Display:
•	Total students 
•	Search a student's attendance 
•	Add a new student 
•	Remove an absent student'''

students = ["Amit", "Rahul", "Sneha", "Pooja"]
# Total students
print("Total students:", len(students))
# Search student attendance
name = input("Enter student name to search: ")

if name in students:
    print(name, "is present")
else:
    print(name, "is absent")
# Add new student
new_student = input("Enter new student name: ")
students.append(new_student)
print("After adding:", students)
# Remove absent student
remove_student = input("Enter student name to remove: ")

if remove_student in students:
    students.remove(remove_student)
    print("Student removed")
else:
    print("Student not found")

print("Final Student List:", students)

'''20.Create a list of books.
Implement:
•	Add a new book 
•	Search a book 
•	Remove a book 
•	Display all books 
•	Count total books'''

books = ["Python", "Java", "C++"]

# Add new book
new_book = input("Enter book to add: ")
books.append(new_book)
# Search book
search_book = input("Enter book to search: ")

if search_book in books:
    print("Book found")
else:
    print("Book not found")
# Remove book
remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)
    print("Book removed")
else:
    print("Book not found")
# Display all books
print("Books:", books)
# Count total books
print("Total books:", len(books))

#21.Accept two lists and merge them into a single list.
list1 = [10, 20, 30]
list2 = [40, 50, 60]
merged_list = list1 + list2
print("Merged List:", merged_list)

#22.Find common elements between two lists.
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common = []
for i in list1:
    if i in list2:
        common.append(i)

print("Common Elements:", common)

#23.Count the frequency of each element in a list.
numbers = [10, 20, 10, 30, 20, 10]
checked = []
for i in numbers:
    if i not in checked:
        print(i, "occurs", numbers.count(i), "times")
        checked.append(i)

'''24.	Rotate a list:
•	Left by one position 
•	Right by one position'''

numbers = [10, 20, 30, 40, 50]
left = numbers[1:] + numbers[:1]
print("Left Rotation:", left)
right = numbers[-1:] + numbers[:-1]
print("Right Rotation:", right)

#25.Remove all duplicate elements while preserving the original order.
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)

print("Original List:", numbers)
print("After Removing Duplicates:", unique)

















