#1.Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.

file = open("student.txt", "w")

file.write("Name: Vaishnavi\n")
file.write("Roll Number: 101\n")
file.write("Branch: Computer Engineering\n")
file.write("Semester: 5\n")
file.close()
print("Student details written successfully.")

#2.Write a program to open a text file and display its complete contents.

file = open("student.txt", "r")
content = file.read()
print("Contents of student.txt:")
print(content)
file.close()

#3.Write a program to append additional student information to an existing file without deleting its previous contents.
file = open("student.txt", "a")
file.write("College: ABC College\n")
file.write("City: Pune\n")

file.close()

print("Additional student information added successfully.")
#4.Write a program to read a text file line by line and display each line separately.

file = open("student.txt", "r")
for line in file:
    print(line.strip())
file.close()

#5.Write a program to count and display the total number of lines present in a text file.
file = open("student.txt", "r")
lines = file.readlines()
count = len(lines)
file.close()
print("Total number of lines:", count)
#6.Write a program to count the total number of words present in a text file.
file = open("student.txt", "r")
content = file.read()
words = content.split()
count = len(words)
file.close()
print("Total number of words:", count)
#7.Write a program to count the total number of characters in a text file, including spaces.
file = open("student.txt", "r")
content = file.read()
count = len(content)
file.close()
print("Total number of characters:", count)
#8.Write a program to read a text file and display its lines in reverse order.
file = open("student.txt", "r")
lines = file.readlines()
file.close()
print("Lines in reverse order:")
for line in reversed(lines):
    print(line.strip())
#9.Read a text file and count the number of vowels and consonants present in the file.
file = open("student.txt", "r")
content = file.read()
file.close()
vowels = 0
consonants = 0
for ch in content.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
print("Total vowels:", vowels)
print("Total consonants:", consonants)
#10.Read a text file and calculate the number of alphabets, digits, spaces, and special characters.
file = open("student.txt", "r")
content = file.read()
file.close()
alphabets = 0
digits = 0
spaces = 0
special = 0
for ch in content:
    if ch.isalpha():
        alphabets = alphabets + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1
print("Total alphabets:", alphabets)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total special characters:", special)
#11.Read a text file and find the longest word present in the file.
file = open("student.txt", "r")
content = file.read()
file.close()
words = content.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)
print("Length of longest word:", len(longest_word))
#12.Read a text file and count how many times each word occurs. Display the result using a dictionary.
file = open("student.txt", "r")
content = file.read().lower()
file.close()
words = content.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
print("Word occurrences:")
for word, count in word_count.items():
    print(word, ":", count)
#13.Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.
word = input("Enter word to search: ").lower()
file = open("student.txt", "r")
count = 0
line_numbers = []
for line_number, line in enumerate(file, start=1):
    words = line.lower().split()

    if word in words:
        count = count + words.count(word)
        line_numbers.append(line_number)
file.close()
print("Number of occurrences:", count)
print("Line numbers:", line_numbers)
#14.Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
file = open("student.txt", "r")
content = file.read()
file.close()
modified_content = content.replace(old_word, new_word)
file = open("student_new.txt", "w")
file.write(modified_content)
file.close()
print("Word replaced successfully.")
print("Modified file saved as student_new.txt")

# 15. Read a Python source file and create another file after removing single-line comments.
file = open("source.py", "r")
lines = file.readlines()
file.close()
new_file = open("without_comments.py", "w")
for line in lines:
    if not line.strip().startswith("#"):
        new_file.write(line)
new_file.close()
print("Single-line comments removed successfully.")

# 16. Read a text file and create another file containing the same text in uppercase.
file = open("student.txt", "r")
content = file.read()
file.close()
new_file = open("uppercase.txt", "w")
new_file.write(content.upper())
new_file.close()
print("Uppercase file created successfully.")

# 17. Create a file containing student records in the format:
# RollNo,Name,Marks
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78
# Write a program to:
# Display all records.
# Find the student with the highest marks.
# Calculate average marks.
# Display students who scored more than 80.
file = open("students.txt", "w")
file.write("RollNo,Name,Marks\n")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")
file.close()
file = open("students.txt", "r")
lines = file.readlines()
file.close()
students = []
for line in lines[1:]:
    roll, name, marks = line.strip().split(",")

    students.append([int(roll), name, int(marks)])
print("\nAll Student Records:")
for student in students:
    print(student[0], student[1], student[2])

highest = max(students, key=lambda x: x[2])
print("\nStudent with Highest Marks:")
print(highest[1], "-", highest[2])
average = sum(student[2] for student in students) / len(students)
print("\nAverage Marks:", average)
print("\nStudents who scored more than 80:")
for student in students:
    if student[2] > 80:
        print(student[1], "-", student[2])
# 18. Store employee ID, name, department, and salary in a file.
# Write functions to:
# Display all employees.
# Find the highest-paid employee.
# Calculate average salary.
# Display employees earning above a given salary.
def read_employees():

    file = open("employees.txt", "w")
    file.write("ID,Name,Department,Salary\n")
    file.write("1,Amit,IT,50000\n")
    file.write("2,Priya,HR,45000\n")
    file.write("3,Rahul,IT,65000\n")
    file.write("4,Neha,Sales,55000\n")

    file.close()

    file = open("employees.txt", "r")

    lines = file.readlines()

    file.close()

    employees = []

    for line in lines[1:]:
        emp_id, name, department, salary = line.strip().split(",")

        employees.append(
            [int(emp_id), name, department, float(salary)]
        )

    return employees

def display_employees(employees):

    print("\nAll Employees:")

    for employee in employees:
        print(employee)

def highest_paid_employee(employees):

    highest = max(employees, key=lambda x: x[3])

    print("\nHighest-Paid Employee:")
    print(highest)

def average_salary(employees):

    total = sum(employee[3] for employee in employees)

    average = total / len(employees)

    print("\nAverage Salary:", average)


def employees_above_salary(employees, salary):

    print("\nEmployees earning above", salary, ":")

    for employee in employees:

        if employee[3] > salary:
            print(employee)

employees = read_employees()

display_employees(employees)

highest_paid_employee(employees)

average_salary(employees)

salary = float(input("\nEnter salary: "))

employees_above_salary(employees, salary)

# 19. Store student attendance records in a file.
# Calculate the attendance percentage and display students
# having attendance below 75%.
file = open("attendance.txt", "w")
file.write("RollNo,Name,Present,Total\n")
file.write("101,Amit,70,90\n")
file.write("102,Priya,80,90\n")
file.write("103,Rahul,60,90\n")
file.write("104,Neha,85,90\n")
file.close()
file = open("attendance.txt", "r")
lines = file.readlines()
file.close()
print("\nStudent Attendance:")
for line in lines[1:]:

    roll, name, present, total = line.strip().split(",")

    present = int(present)
    total = int(total)

    percentage = (present / total) * 100

    print(name, "-", round(percentage, 2), "%")

    if percentage < 75:
        print("Below 75%:", name)

# 20. Store deposits and withdrawals in a file.
# Read the file and calculate:
# Total deposits
# Total withdrawals
# Final balance
# Largest transaction
file = open("transactions.txt", "w")
file.write("Deposit,10000\n")
file.write("Withdrawal,2000\n")
file.write("Deposit,5000\n")
file.write("Withdrawal,1500\n")
file.write("Deposit,3000\n")
file.close()
file = open("transactions.txt", "r")
total_deposits = 0
total_withdrawals = 0
transactions = []
for line in file:

    transaction, amount = line.strip().split(",")

    amount = float(amount)

    transactions.append(amount)

    if transaction.lower() == "deposit":
        total_deposits = total_deposits + amount

    elif transaction.lower() == "withdrawal":
        total_withdrawals = total_withdrawals + amount

file.close()
final_balance = total_deposits - total_withdrawals
largest_transaction = max(transactions)
print("\nTotal Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)

# 21. Maintain book records containing book ID, title, author, and availability status.
# Implement operations to:
# Add a book.
# Search for a book.
# Issue a book.
# Return a book.
# Display available books.
def load_books():

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()
    books = []
    for line in lines[1:]:
        book_id, title, author, status = line.strip().split(",")

        books.append([book_id, title, author, status])

    return books

def save_books(books):

    file = open("books.txt", "w")
    file.write("BookID,Title,Author,Status\n")
    for book in books:
        file.write(
            book[0] + "," +
            book[1] + "," +
            book[2] + "," +
            book[3] + "\n"
        )

    file.close()


def add_book(books):

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")

    books.append([book_id, title, author, "Available"])

    save_books(books)

    print("Book added successfully.")


def search_book(books):

    book_id = input("Enter Book ID to search: ")

    for book in books:

        if book[0] == book_id:
            print("Book ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Status:", book[3])
            return

    print("Book not found.")


def issue_book(books):

    book_id = input("Enter Book ID to issue: ")

    for book in books:

        if book[0] == book_id:

            if book[3] == "Available":
                book[3] = "Issued"
                save_books(books)
                print("Book issued successfully.")
            else:
                print("Book is already issued.")

            return

    print("Book not found.")


def return_book(books):

    book_id = input("Enter Book ID to return: ")

    for book in books:

        if book[0] == book_id:

            if book[3] == "Issued":
                book[3] = "Available"
                save_books(books)
                print("Book returned successfully.")
            else:
                print("Book is already available.")

            return

    print("Book not found.")


def display_available_books(books):

    print("\nAvailable Books:")

    for book in books:

        if book[3] == "Available":
            print(book[0], book[1], book[2])


# Create books file if it does not exist
file = open("books.txt", "w")
file.write("BookID,Title,Author,Status\n")
file.write("101,Python Basics,John,Available\n")
file.write("102,Java Programming,James,Available\n")
file.write("103,Data Science,David,Issued\n")
file.close()
books = load_books()
while True:

    print("\n--- BOOK MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book(books)

    elif choice == "2":
        search_book(books)

    elif choice == "3":
        issue_book(books)

    elif choice == "4":
        return_book(books)

    elif choice == "5":
        display_available_books(books)

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

# 22. Read the contents of two text files and create a third file
# containing the contents of both files.

file1 = open("file1.txt", "w")
file1.write("This is the content of first file.\n")
file1.write("Welcome to Python File Handling.\n")
file1.close()
file2 = open("file2.txt", "w")
file2.write("This is the content of second file.\n")
file2.write("Python makes file handling easy.\n")
file2.close()
file1 = open("file1.txt", "r")
content1 = file1.read()
file1.close()
file2 = open("file2.txt", "r")
content2 = file2.read()
file2.close()
file3 = open("file3.txt", "w")
file3.write(content1)
file3.write(content2)
file3.close()
print("\nContents of both files combined successfully.")
print("New file created: file3.txt")

# 23. Write a program to compare two text files and display whether
# their contents are identical. If different, identify the first line
# where they differ.
file1 = open("compare1.txt", "w")
file1.write("Hello Python\n")
file1.write("File Handling\n")
file1.close()
file2 = open("compare2.txt", "w")
file2.write("Hello Python\n")
file2.write("File Handling\n")
file2.close()

file1 = open("compare1.txt", "r")
lines1 = file1.readlines()
file1.close()
file2 = open("compare2.txt", "r")
lines2 = file2.readlines()
file2.close()
if lines1 == lines2:
    print("\nBoth files are identical.")

else:
    print("\nFiles are different.")

    min_lines = min(len(lines1), len(lines2))

    for i in range(min_lines):

        if lines1[i] != lines2[i]:
            print("First difference found at line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            break

    else:
        if len(lines1) != len(lines2):
            print("Files have different number of lines.")
            print("First difference at line:", min_lines + 1)
