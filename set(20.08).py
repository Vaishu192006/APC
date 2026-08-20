 #1.Write a Python program to create a set containing five integers and display all its elements.
numbers = {10, 20, 30, 40, 50}
print("Set elements:", numbers)

#2.Create a list containing duplicate values. Convert the list into a set and display the resulting set.
numbers = [10, 20, 10, 30, 20, 40]
result = set(numbers)
print("Set:", result)

#3.Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
fruits.add("Papaya")
fruits.add("Guava")
print("Updated set:", fruits)

#4.Create a set of numbers and remove a specified number from the set.
numbers = {10, 20, 30, 40, 50}
numbers.remove(30)
print("Set after removing 30:", numbers)

#5.Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
students = {"Rahul", "Priya", "Amit", "Sneha", "Neha"}
name = input("Enter student name: ")
if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist in the set.")

#6.Create a set of cities and determine the total number of cities using an appropriate function.
city={"Kolhapur","Kagal","Karad","Pune","Mumbai"}
print("Total number of cities:",len(city))

#7.Create a set of programming languages and display each language using a for loop.
languages = {"Python", "Java", "C", "C++", "JavaScript"}
for language in languages:
    print(language)

#8.Create a list containing duplicate numbers, use a set to remove the duplicates.

numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique_numbers = set(numbers)
print("Numbers without duplicates:", unique_numbers)

#9.Create two sets of integers and find their union.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
print("Union:", union_set)

#10.Create two sets and find the elements common to both sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common = set1.intersection(set2)
print("Common elements:", common)


# 11.Create two sets and find:
#•Elements present in the first set but not the second 
#•Elements present in the second set but not the first

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("1. First set but not second:", set1 - set2)
print("   Second set but not first:", set2 - set1)


#12.Create two sets and find:
#•Elements present in the first set but not the second 
#•Elements present in the second set but not the first

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("\n2. Elements in either set but not both:", set1 ^ set2)


#13.Create two sets and determine whether the first set is a subset of the second set.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print("\n3. First set is subset:", set1.issubset(set2))


#14.Create two sets and determine whether the first set is a superset of the second set.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print("\n4. First set is superset:", set1.issuperset(set2))


#15.Write a program to determine whether two sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("\n5. Sets have no common elements:", set1.isdisjoint(set2))


#16.Create two sets and check whether they are equal.
set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}

print("\n6. Both sets are equal:", set1 == set2)


#17.Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
student1 = {"Maths", "Python", "Java", "DBMS"}
student2 = {"Python", "DBMS", "C++", "Networking"}
print("\n7. Subjects studied by both:", student1 & student2)


#18.Accept a sentence from the user and use a set to display all unique words.
sentence = input("\n8. Enter a sentence: ")
words = set(sentence.split())
print("Unique words:", words)

#19.Create two sets:1.Students present in the morning session 2.Students present in the afternoon session 
#Find:1.Students present in both sessions,2.Students present only in the morning,3.Students present only in the afternoon,4.Students present in at least one session

morning = {"Amit", "Rahul", "Priya", "Sneha"}
afternoon = {"Priya", "Sneha", "Neha", "Rohan"}
print("student present in both session:",morning&afternoon)
print("student present in only morning session:",morning-afternoon)
print("student present in both session:",afternoon-morning)
print("Students in at least one session:",morning|afternoon)

#20.Create sets representing students enrolled in:,Python ,Java
python_students = {"Amit", "Rahul", "Priya", "Sneha", "Neha"}
java_students = {"Priya", "Sneha", "Rohan", "Kiran"}

print(" Python Students:", python_students)
print("   Java Students:", java_students)

#21.Find students enrolled in both courses and students enrolled in only one course.
python_students = {"Amit", "Rahul", "Priya", "Sneha", "Neha"}
java_students = {"Priya", "Sneha", "Rohan", "Kiran"}
print("students enrolled in both courses:",python_students&java_students)
print("students enrolled in only one course:",python_students^java_students)

#22.Create two sets representing technical skills of two employees.
employee1 = {"Python", "Java", "SQL", "HTML"}
employee2 = {"Python", "C++", "SQL", "CSS"}
print("Common skills:", employee1 & employee2)
print("Unique to Employee 1:", employee1 - employee2)
print("Unique to Employee 2:", employee2 - employee1)
print("All available skills:", employee1 | employee2)


#23.Create a set containing available books and another set containing requested books. Determine which requested books are available.
available_books = {"Python", "Java", "C++", "DBMS"}
requested_books = {"Python", "DBMS", "HTML"}

print("Available requested books:", available_books & requested_books)


#24.Visitor IDs
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)
category1 = {"Laptop", "Mobile", "Tablet", "Camera"}
category2 = {"Mobile", "Tablet", "Smartwatch", "Camera"}
print("Products in both categories:", category1 & category2)


#25.Friends of two users
user1 = {"Amit", "Rahul", "Sneha", "Priya"}
user2 = {"Sneha", "Priya", "Neha", "Kiran"}
print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", user1 | user2)

