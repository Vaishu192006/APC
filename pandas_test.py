# ============================================================
# Q1. Create a dictionary containing information for 5 students:
# Student ID, Student Name, Python Marks, DBMS Marks,
# Mathematics Marks.
#
# Convert the dictionary into a Pandas DataFrame and:
# 1. Display the DataFrame.
# 2. Calculate total marks for each student.
# 3. Calculate average marks.
# 4. Display students who scored more than 75% average.
# ============================================================

import pandas as pd
student = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Student_Name': ['Vaishnavi', 'Priya', 'Sneha', 'Riya', 'Pooja'],
    'Python': [98, 75, 85, 65, 90],
    'DBMS': [80, 70, 88, 60, 92],
    'Mathematics': [95, 78, 82, 70, 89]
}
df = pd.DataFrame(student)
print("Student Data:")
print(df)
df['Total'] = df['Python'] + df['DBMS'] + df['Mathematics']
df['Average'] = df['Total'] / 3
print("\nStudent Data with Total and Average:")
print(df)
print("\nStudents who scored more than 75% average:")
print(df[df['Average'] > 75])

# ============================================================
# Q2. Create a dictionary containing:
# Employee ID, Employee Name, Department, Salary, Experience.
#
# Convert it into a Pandas DataFrame and:
# 1. Display employees with salary greater than Rs. 50,000.
# 2. Find the average salary.
# 3. Find the highest salary.
# 4. Find the employee with the highest experience.
# ============================================================

import pandas as pd
employee = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Employee_Name': ['Amit', 'Rahul', 'Sneha', 'Priya', 'Neha'],
    'Department': ['CSE', 'IT', 'HR', 'CSE', 'IT'],
    'Salary': [60000, 45000, 55000, 75000, 50000],
    'Experience': [5, 3, 7, 8, 4]
}
df = pd.DataFrame(employee)
print("Employee Data:")
print(df)
print("\nEmployees with salary greater than Rs. 50,000:")
print(df[df['Salary'] > 50000])
print("\nAverage Salary:")
print(df['Salary'].mean())
print("\nHighest Salary:")
print(df['Salary'].max())
print("\nEmployee with highest experience:")
print(df.loc[df['Experience'].idxmax()])

# ============================================================
# Q3. Create a dictionary containing:
# Product ID, Product Name, Category, Price, Quantity.
#
# Convert it into a DataFrame.
# Calculate:
# Total Amount = Price × Quantity
#
# Then find the product having the highest total sales.
# ============================================================

import pandas as pd
product = {
    'Product_ID': [101, 102, 103, 104, 105],
    'Product_Name': ['Laptop', 'Mobile', 'Keyboard', 'Monitor', 'Mouse'],
    'Category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories'],
    'Price': [50000, 25000, 1500, 12000, 800],
    'Quantity': [2, 4, 10, 5, 20]
}
df = pd.DataFrame(product)
print("Product Data:")
print(df)
df['Total_Amount'] = df['Price'] * df['Quantity']
print("\nProduct Data with Total Amount:")
print(df)
print("\nProduct having highest total sales:")
print(df.loc[df['Total_Amount'].idxmax()])

# ============================================================
# Q4. Create a dictionary containing:
# Patient ID, Patient Name, Age, Disease, Medical Charges.
#
# Convert the dictionary into a Pandas DataFrame and:
# 1. Display patients above 60 years.
# 2. Find the average medical charge.
# 3. Find the maximum medical charge.
# 4. Display patients whose medical charges are greater
#    than Rs. 50,000.
# ============================================================

import pandas as pd
patient = {
    'Patient_ID': [101, 102, 103, 104, 105],
    'Patient_Name': ['Amit', 'Sunita', 'Raj', 'Pooja', 'Ramesh'],
    'Age': [65, 45, 72, 35, 68],
    'Disease': ['Diabetes', 'Fever', 'Heart Disease', 'Cold', 'Cancer'],
    'Medical_Charges': [60000, 25000, 85000, 15000, 70000]
}
df = pd.DataFrame(patient)
print("Patient Data:")
print(df)
print("\nPatients above 60 years:")
print(df[df['Age'] > 60])
print("\nAverage Medical Charge:")
print(df['Medical_Charges'].mean())
print("\nMaximum Medical Charge:")
print(df['Medical_Charges'].max())
print("\nPatients with medical charges greater than Rs. 50,000:")
print(df[df['Medical_Charges'] > 50000])

# ============================================================
# Q5. Create a dictionary containing:
# Order_ID, Customer, Product, Quantity, Price, Discount.
#
# Create a DataFrame and calculate:
# Final Amount = Quantity × Price − Discount
#
# Then display:
# 1. All orders
# 2. Orders above Rs. 5,000
# 3. Highest-value order
# 4. Average order value
# ============================================================

import pandas as pd
order = {
    'Order_ID': [101, 102, 103, 104, 105],
    'Customer': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Neha'],
    'Product': ['Laptop', 'Mobile', 'Monitor', 'Tablet', 'Printer'],
    'Quantity': [1, 2, 3, 2, 1],
    'Price': [55000, 25000, 12000, 18000, 15000],
    'Discount': [2000, 1000, 500, 1000, 500]
}
df = pd.DataFrame(order)
df['Final_Amount'] = (df['Quantity'] * df['Price']) - df['Discount']
print("All Orders:")
print(df)
print("\nOrders above Rs. 5,000:")
print(df[df['Final_Amount'] > 5000])
print("\nHighest-value order:")
print(df.loc[df['Final_Amount'].idxmax()])
print("\nAverage Order Value:")
print(df['Final_Amount'].mean())

# ============================================================
# Q6. Create a dictionary containing:
# Student_ID, Name, Department, Total_Classes, Classes_Attended.
#
# Create a DataFrame and calculate:
# Attendance Percentage =
# (Classes_Attended / Total_Classes) × 100
#
# Display students whose attendance is below 75%.
# ============================================================

import pandas as pd
student = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Vaishnavi', 'Priya', 'Sneha', 'Riya', 'Pooja'],
    'Department': ['CSE', 'CSE', 'IT', 'CSE', 'IT'],
    'Total_Classes': [100, 100, 100, 100, 100],
    'Classes_Attended': [90, 70, 85, 60, 75]
}
df = pd.DataFrame(student)
df['Attendance_Percentage'] = (
    df['Classes_Attended'] / df['Total_Classes']
) * 100
print("Student Attendance Data:")
print(df)
print("\nStudents whose attendance is below 75%:")
print(df[df['Attendance_Percentage'] < 75])

# ============================================================
# Q7A. A retail shop maintains sales information in a Python
# dictionary containing:
# Product_ID, Product_Name, Category, Price, Quantity.
#
# Write a Python program to:
# 1. Convert the dictionary into a Pandas DataFrame.
# 2. Add a new column Total_Sales.
# 3. Calculate total sales using Price × Quantity.
# 4. Display products with sales greater than Rs. 10,000.
# 5. Find the product with maximum sales.
# 6. Calculate the average sales.
# ============================================================

import pandas as pd
product = {
    'Product_ID': [101, 102, 103, 104, 105],
    'Product_Name': ['Laptop', 'Mobile', 'TV', 'Printer', 'Keyboard'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Office', 'Accessories'],
    'Price': [50000, 25000, 40000, 12000, 1500],
    'Quantity': [2, 3, 1, 2, 10]
}
df = pd.DataFrame(product)
df['Total_Sales'] = df['Price'] * df['Quantity']
print("Product Data:")
print(df)
print("\nProducts with sales greater than Rs. 10,000:")
print(df[df['Total_Sales'] > 10000])
print("\nProduct with maximum sales:")
print(df.loc[df['Total_Sales'].idxmax()])
print("\nAverage Sales:")
print(df['Total_Sales'].mean())

# ============================================================
# Q7B. Create a Pandas Series using a dictionary where
# student names are keys and their marks are values.
#
# Perform:
# 1. Display the Series.
# 2. Display marks of a particular student.
# 3. Find maximum and minimum marks.
# 4. Calculate the average marks.
# 5. Display students who scored more than 75.
# ============================================================

import pandas as pd
marks = {
    'Vaishnavi': 98,
    'Priya': 72,
    'Sneha': 85,
    'Riya': 68,
    'Pooja': 91
}
series = pd.Series(marks)
print("Student Marks Series:")
print(series)
print("\nVaishnavi's marks:")
print(series['Vaishnavi'])
print("\nMaximum Marks:")
print(series.max())
print("\nMinimum Marks:")
print(series.min())
print("\nAverage Marks:")
print(series.mean())
print("\nStudents scoring more than 75:")
print(series[series > 75])

# ============================================================
# Q8. Create a Pandas Series using a dictionary containing
# employee names and their salaries.
#
# Perform:
# 1. Display the Series.
# 2. Find the highest salary.
# 3. Find the lowest salary.
# 4. Calculate average salary.
# 5. Display employees earning more than Rs. 50,000.
# ============================================================

import pandas as pd

salary = {
    'Amit': 60000,
    'Rahul': 45000,
    'Sneha': 75000,
    'Priya': 50000,
    'Neha': 85000
}
series = pd.Series(salary)
print("Employee Salary Series:")
print(series)
print("\nHighest Salary:")
print(series.max())
print("\nLowest Salary:")
print(series.min())
print("\nAverage Salary:")
print(series.mean())
print("\nEmployees earning more than Rs. 50,000:")
print(series[series > 50000])

# ============================================================
# Q9. Create a Pandas Series using a dictionary containing
# product names and prices.
#
# Perform:
# 1. Display all products and prices.
# 2. Increase every price by 10%.
# 3. Find the most expensive product.
# 4. Find products costing more than Rs. 1,000.
# ============================================================

import pandas as pd
price = {
    'Laptop': 50000,
    'Mobile': 25000,
    'Keyboard': 1500,
    'Mouse': 800,
    'Monitor': 12000
}
series = pd.Series(price)
print("Product Prices:")
print(series)
new_price = series * 1.10
print("\nPrices after 10% increase:")
print(new_price)
print("\nMost expensive product:")
print(series.idxmax(), "=", series.max())
print("\nProducts costing more than Rs. 1,000:")
print(series[series > 1000])

# ============================================================
# Q10. Create a Pandas Series using a dictionary where
# patient IDs are the index and patient ages are the values.
#
# Perform:
# 1. Find the average age.
# 2. Find the oldest patient.
# 3. Find the youngest patient.
# 4. Display patients above 60 years.
# ============================================================

import pandas as pd

age = {
    101: 65,
    102: 45,
    103: 72,
    104: 35,
    105: 68
}

series = pd.Series(age)

print("Patient Age Series:")
print(series)

print("\nAverage Age:")
print(series.mean())

print("\nOldest Patient:")
print("Patient ID:", series.idxmax())
print("Age:", series.max())

print("\nYoungest Patient:")
print("Patient ID:", series.idxmin())
print("Age:", series.min())

print("\nPatients above 60 years:")
print(series[series > 60])

# ============================================================
# Q11. Create a Pandas Series using a dictionary containing
# student names and attendance percentages.
#
# Perform:
# 1. Find the average attendance.
# 2. Display students with attendance below 75%.
# 3. Display students with attendance above 90%.
# 4. Find the highest attendance.
# ============================================================

import pandas as pd

attendance = {
    'Vaishnavi': 95,
    'Priya': 72,
    'Sneha': 88,
    'Riya': 65,
    'Pooja': 92
}

series = pd.Series(attendance)

print("Student Attendance Series:")
print(series)

print("\nAverage Attendance:")
print(series.mean())

print("\nStudents with attendance below 75%:")
print(series[series < 75])

print("\nStudents with attendance above 90%:")
print(series[series > 90])

print("\nHighest Attendance:")
print(series.max())

# ============================================================
# Q12. Dataset: students.csv
#
# Columns:
# Student_ID, Name, Department, Python, DBMS, Maths
#
# Read students.csv using Pandas and perform:
# 1. Display the first 5 records.
# 2. Display the last 5 records.
# 3. Find the total and average marks of each student.
# 4. Display students whose average marks are greater than 75.
# 5. Find the student with the highest average.
# 6. Find the average marks for each subject.
# ============================================================

import pandas as pd


df = pd.read_csv("student.csv")
print("First 5 Records:")
print(df.head())
print("\nLast 5 Records:")
print(df.tail())
df['Total'] = df['Python'] + df['DBMS'] + df['Maths']
df['Average'] = df['Total'] / 3
print("\nTotal and Average Marks:")
print(df)
print("\nStudents with average marks greater than 75:")
print(df[df['Average'] > 75])
print("\nStudent with highest average:")
print(df.loc[df['Average'].idxmax()])
print("\nAverage Python Marks:", df['Python'].mean())
print("Average DBMS Marks:", df['DBMS'].mean())
print("Average Maths Marks:", df['Maths'].mean())

# ============================================================
# Q13. Dataset: employees.csv
#
# Columns:
# Employee_ID, Name, Department, Experience, Salary
#
# Read the CSV file and:
# 1. Display employees from the CSE department.
# 2. Find the average salary.
# 3. Find the highest and lowest salary.
# 4. Display employees having salary greater than Rs. 50,000.
# 5. Calculate department-wise average salary.
# ============================================================

import pandas as pd
df = pd.read_csv("employee.csv")
print("Employee Data:")
print(df)
print("\nEmployees from CSE Department:")
print(df[df['Department'] == 'CSE'])
print("\nAverage Salary:")
print(df['Salary'].mean())
print("\nHighest Salary:")
print(df['Salary'].max())
print("\nLowest Salary:")
print(df['Salary'].min())
print("\nEmployees having salary greater than Rs. 50,000:")
print(df[df['Salary'] > 50000])
print("\nDepartment-wise Average Salary:")
print(df.groupby('Department')['Salary'].mean())

# ============================================================
# Q14. Dataset: patients.csv
#
# Columns:
# Patient_ID, Name, Age, Gender, Disease, Medical_Expense
#
# Read the CSV file and:
# 1. Display patients above 60 years.
# 2. Calculate average medical expense.
# 3. Find the patient with the highest medical expense.
# 4. Count patients for each disease.
# 5. Display patients whose medical expense exceeds Rs. 50,000.
# ============================================================

import pandas as pd
df = pd.read_csv("patients.csv")
print("Patient Data:")
print(df)
print("\nPatients above 60 years:")
print(df[df['Age'] > 60])
print("\nAverage Medical Expense:")
print(df['Medical_Expense'].mean())
print("\nPatient with highest medical expense:")
print(df.loc[df['Medical_Expense'].idxmax()])
print("\nNumber of Patients for Each Disease:")
print(df['Disease'].value_counts())
print("\nPatients with medical expense greater than Rs. 50,000:")
print(df[df['Medical_Expense'] > 50000])



# ============================================================
# Q15. Dataset: weather.csv
#
# Columns:
# Date, City, Temperature, Humidity, Rainfall
#
# Read the CSV file and:
# 1. Find the maximum temperature.
# 2. Find the minimum temperature.
# 3. Calculate the average temperature.
# 4. Display records where temperature is above 35°C.
# 5. Calculate city-wise average temperature.
# ============================================================

import pandas as pd
df = pd.read_csv("weather.csv")
print("Weather Data:")
print(df)
print("\nMaximum Temperature:")
print(df['Temperature'].max())
print("\nMinimum Temperature:")
print(df['Temperature'].min())
print("\nAverage Temperature:")
print(df['Temperature'].mean())
print("\nRecords where temperature is above 35°C:")
print(df[df['Temperature'] > 35])
print("\nCity-wise Average Temperature:")
print(df.groupby('City')['Temperature'].mean())


