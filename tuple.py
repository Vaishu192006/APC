#1.Write a Python program to create a tuple of five integers and display it.
t1=(10,20,30,40,50)
print("tuple element:",t1)

#2.Create a tuple containing five city names. Display First city ,Last city ,Third city
t1=("kolhapur","Kagal","pune","mumbai","karad")
print("first city:",t1[0])
print("Last city:",t1[-1])#t1[5])
print("Third city:",t1[3])

#3.Create a tuple of student names and display the total number of students using the len() function.
t1=("Vaishnavi","Madhura","Shreya","Piyusha","Pranali","Shravni","Rohoni")
print("Length of tuple:",len(t1))

#4.Create a tuple of colors. Check whether a given color exists in the tuple
t1=("red","yellow","black","blue","pink","white","brown","orange")
color=input("enter color:")
if color in color:
    print("color is exist")
else:
    print("color is not exist")

#5.Create a tuple of fruits and display each fruit using a loop.
t1=("apple","banana","pineapple","cherry","strawberry")
for i in range(len(t1)):
    print("tuple elements(fruit):",t1[i])

#6.Create a tuple with repeated numbers and count how many times a particular number appears.
no=(10,20,10,20,30,30,40,50)
n=int(input("enter number :"))
print("counts of number:",no.count(n))

#7.Create a tuple of employee IDs and find the index of a given ID.
t1=(101,102,10,3,104,105,106,107,108,109,109)
id=int(input("enter the id:"))
if id in t1:
    print("id exist at index:",t1.index(id))
else:
    print("not exist")

#8.Create two tuples of numbers and concatenate them into a single tuple.
t1=(10,20,30,40,50,400,56,45)
t2=(80,70,90,100,456,123,779,741,852)
t3=t1+t2
print("after concatenation:",t3)

#9.Create a tuple containing three elements and repeat it four times.
t1=(10,20,30)
t2=t1*4
print(t2)

#10.Create a tuple of 10 numbers and display:

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# First five elements
print("First five elements:", numbers[:5])
# Last five elements
print("Last five elements:", numbers[5:])
# Middle four elements
print("Middle four elements:", numbers[3:7])
# Alternate elements
print("Alternate elements:", numbers[::2])
# Reverse tuple
print("Reverse tuple:", numbers[::-1])

#11.Convert a tuple into a list and add a new element.
t = (10, 20, 30, 40)
l = list(t)
l.append(50)
print("Tuple:", t)
print("List after adding element:", l)
#12.Accept five numbers from the user, store them in a list, and convert the list into a tuple.
l = []
for i in range(5):
    n = int(input("Enter number: "))
    l.append(n)
t = tuple(l)
print("List:", l)
print("Tuple:", t)
#13.Modify a tuple by converting it into a list and then back into a tuple.
t = (10, 20, 30, 40)
l = list(t)
l[2] = 100
t = tuple(l)
print("Modified tuple:", t)
#14.Create a tuple and delete it completely.
t = (10, 20, 30, 40)
print("Tuple:", t)
del t
print("Tuple deleted successfully")
#15.Create a nested tuple containing student details and display each record.
students = (
    (1, "Vaishnavi", 85),
    (2, "Priya", 90),
    (3, "Sneha", 88)
)
for student in students:
    print("Roll No:", student[0])
    print("Name:", student[1])
    print("Marks:", student[2])
    print()
#16.Store ten numbers in a tuple and calculate their sum.
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
total = 0
for n in t:
    total = total + n
print("Sum =", total)
#17.ind the largest and smallest number in a tuple without using max() and min().
t = (25, 10, 45, 5, 80, 30)
largest = t[0]
smallest = t[0]
for n in t:
    if n > largest:
        largest = n

    if n < smallest:
        smallest = n
print("Largest number:", largest)
print("Smallest number:", smallest)
#18.Calculate the average of elements stored in a tuple.
t = (10, 20, 30, 40, 50)
total = 0
for n in t:
    total = total + n
average = total / len(t)
print("Average =", average)
#19.Store 15 integers in a tuple and count:Even numbers 	Odd numbers
t1=(10,20,30,12,11,45,56,87,25,13,5,6,89,74,23,15)
even = 0
odd = 0
for n in t1:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even numbers:", even)
print("Odd numbers:", odd)

#20.Accept a number from the user and determine whether it exists in the tuple.
t = (10, 20, 30, 40, 50)
n = int(input("Enter a number: "))
if n in t:
    print("Number exists in the tuple")
else:
    print("Number does not exist in the tuple")

#21. Store student details in a tuple and display all the details
student = (101, "Vaishnavi", "Computer Science", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])

#22.Create tuples containing:
employees = (
    (101, "Rahul", 25000),
    (102, "Priya", 30000),
    (103, "Amit", 28000)
)
for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()

#23. Store item prices and calculate total, average, highest and lowest price
prices = (100, 250, 150, 500, 300)

total = sum(prices)
average = total / len(prices)
highest = max(prices)
lowest = min(prices)
print("Total Bill:", total)
print("Average Price:", average)
print("Highest Price:", highest)
print("Lowest Price:", lowest)

#24. Store temperatures of seven days
temperatures = (30, 32, 29, 35, 31, 33, 28)
total = sum(temperatures)
average = total / len(temperatures)

print("Maximum Temperature:", max(temperatures))
print("Minimum Temperature:", min(temperatures))
print("Average Temperature:", average)

#25. Store runs scored in 10 matches
runs = (45, 67, 89, 34, 56, 78, 90, 23, 55, 72)
total = sum(runs)
average = total / len(runs)
print("Total Runs:", total)
print("Highest Score:", max(runs))
print("Lowest Score:", min(runs))
print("Average Score:", average)

#26.Create two tuples and find common elements

t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 50, 60, 70)
common = tuple(set(t1) & set(t2))
print("Common Elements:", common)
#27. Merge two tuples and remove duplicate elements
t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)
merged = tuple(set(t1 + t2))
print("Merged Tuple:", merged)

#28. Count the frequency of each element in a tuple
t = (10, 20, 10, 30, 20, 10, 40, 30)
for element in set(t):
    print(element, "occurs", t.count(element), "times")


#29. Convert a tuple into sorted tuple in ascending and descending order

t = (50, 20, 80, 10, 40, 30)
ascending = tuple(sorted(t))
descending = tuple(sorted(t, reverse=True))
print("Ascending Order:", ascending)
print("Descending Order:", descending)

#30. Create a tuple containing patient records
patients = (
    (101, "Rakesh", 25, "A+"),
    (102, "Prajkta", 30, "B+"),
    (103, "Abhay", 40, "O+"),
    (104, "Sakshi", 28, "A+")
)
print("All Patient Records:")
for patient in patients:
    print(patient)
pid = int(input("\nEnter Patient ID to search: "))

found = False
for patient in patients:
    if patient[0] == pid:
        print("Patient Found:", patient)
        found = True
        break
if not found:
    print("Patient not found")
print("\nTotal Number of Patients:", len(patients))
blood = input("\nEnter Blood Group: ")
print("Patients with", blood, "blood group:")
for patient in patients:
    if patient[3] == blood:
        print(patient)



    

