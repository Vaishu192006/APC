#numpy version
import numpy as np
print(np.__version__)
print("-----------------------------------")
#basic operation
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))

#Arithmetic operation
import numpy as np

a=np.array([10,20,3,5,60])
b=np.array([5,6,7,13,8])
print("Array 1:",a)
print("Array 2:",b)
print("Addition:",a+b)
print("substraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("exponantiation:",a**2)
print("floor division:",a//b)
print("Modules:",a%b)
#matrix operation
import numpy as np
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Matrix:")
print(matrix)
print("Number of rows and columns:", matrix.shape)
print("Sum:", np.sum(matrix))
print("Maximum:", np.max(matrix))
print("Minimum:", np.min(matrix))

#Shape and Dimension of Array
import numpy as np
a = np.array([10, 20, 30, 40, 50])
print("Array:", a)
print("Shape:", a.shape)
print("Dimension:", a.ndim)
b = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
print("3D Array:")
print(b)
print("Shape:", b.shape)
print("Dimension:", b.ndim)

#Reshape
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
print(a)
b = a.reshape(2, 3)
print("Reshaped Array:")
print(b)

#Flatten                                                                                                                                                                                                                                                                                                                                                                                        
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Original Array:")
print(a)
b = a.flatten()
print("Flattened Array:")
print(b)

#indexing
import numpy as np
a = np.array([10, 20, 30, 40, 50])
print("Array:", a)
print("First element:", a[0])
print("Third element:", a[2])
print("Last element:", a[-1])

#slicing
import numpy as np
a = np.array([10, 20, 30, 40, 50])
print("Array:", a)
print("First three elements:", a[0:3])
print("Elements from index 2:", a[2:])
print("First four elements:", a[:4])

#Array Data Type
import numpy as np
a = np.array([10, 20, 30, 40])
print("Array:", a)
print("Data type:", a.dtype)
print("Array size:",a.size)


#Concatenation
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print("Array 1:", a)
print("Array 2:", b)
print("Concatenated Array:", c)

#Transpose
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Matrix:")
print(a)
print("Transpose:")
print(a.T)


print("#######################################")
#1.Write a Python program using NumPy to create a one-dimensional array containing 10 integers
#and display the array, its size, data type, and number of dimensions.
import numpy as np
arr=np.array([10,20,30,40,50,60,70,80,90,100])
print("Array:",arr)
print("Size of array:",arr.size)
print("Data type:",arr.dtype)
print("Number of dimension:",arr.ndim)

#2. Create two NumPy arrays of 5 integers each. Perform and display:
#•Addition, Subtraction ,Multiplication ,Division ,Modulus
import numpy as np
a=np.array([10,20,3,5,60])
b=np.array([5,6,7,13,8])
print("Array 1:",a)
print("Array 2:",b)
print("Addition:",a+b)
print("substraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("exponantiation:",a**2)
print("floor division:",a//b)
print("Modules:",a%b)
#3.Create a NumPy array containing 10 numbers. Find and display
#the maximum, minimum, sum, and average of the elements.
import numpy as np
arr = np.array([10, 20, 30, 40, 50,60,70,80,90,100])
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
#4.Create a NumPy array of integers from 1 to 20. Use Boolean
#indexing to separate and display the even and odd numbers.
import numpy as np
a = np.arange(1, 21)
even = a[a % 2 == 0]
odd = a[a % 2 != 0]
print("Original Array:", a)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
#5.Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:2 × 6 matrix ,3 × 4 matrix 4 × 3 matrix
import numpy as np
a = np.arange(1,13)
print("Original Array:")
print(a)
b = a.reshape(2,6)
print("Reshaped Array2*6:")
print(b)
c=a.reshape(3,4)
print("Reshaped array 3*4:")
print(c)
d=a.reshape(4,3)
print("Reshaped array 4*3:")
print(d)
#6:Create two 3 × 3 NumPy matrices and perform matrix addition.
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
B = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])
C = A + B
print("First Matrix:")
print(A)
print("Second Matrix:")
print(B)
print("Matrix Addition:")
print(C)
#7.Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.

import numpy as np
A = np.array([[1, 2, 3],  [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])
C = np.dot(A, B)
print("First Matrix:")
print(A)
print("Second Matrix:")
print(B)
print("Matrix Multiplication:")
print(C)
#8.Create a 3 × 4 matrix and display its transpose.
import numpy as np
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12]])
T = A.T
print("Original Matrix:")
print(A)
print("Transpose of Matrix:")
print(T)

#9.Create a 4 × 4 NumPy array and write a program to:
# Display the first row
# Display the last column
# Display the diagonal elements
# Display the elements from the second and third rows

import numpy as np
a = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]])

print("First Row:", a[0, :])
print("Last Column:", a[:, -1])
print("Diagonal Elements:", np.diag(a))
print("Second and Third Rows:")
print(a[1:3, :])

# 10.Create a 4 × 4 matrix and calculate the sum of each row
# and each column separately.
# Create a 4 × 4 matrix
import numpy as np
a = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]])
row_sum = np.sum(a, axis=1)
column_sum = np.sum(a, axis=0)
print("Matrix:")
print(a)
print("Sum of Each Row:", row_sum)
print("Sum of Each Column:", column_sum)

#11.Create a NumPy array containing numbers from 1 to 20.
# Using slicing, display:
# First 5 elements
# Last 5 elements
# Alternate elements
# Elements in reverse order
# Create array from 1 to 20
import numpy as np
a = np.arange(1, 21)
print("First 5 Elements:", a[:5])
print("Last 5 Elements:", a[-5:])
print("Alternate Elements:", a[::2])
print("Reverse Order:", a[::-1])
#12.Create an array of 10 integers. Replace all elements
# greater than 50 with 0 using NumPy Boolean indexing.
import numpy as np
a = np.array([25, 60, 45, 75, 30, 90, 55, 40, 80, 20])
a[a > 50] = 0
print("Array after replacing values greater than 50:")
print(a)
#13.Create an unsorted NumPy array and display it in:
# Ascending order
# Descending order
import numpy as np
a = np.array([50, 10, 80, 30, 90, 20, 60, 40])
ascending = np.sort(a)
descending = np.sort(a)[::-1]
print("Original Array:", a)
print("Ascending Order:", ascending)
print("Descending Order:", descending)
# 14.Create an array containing duplicate values.
# Find and display only the unique elements.
import numpy as np
a = np.array([10, 20, 10, 30, 20, 40, 30, 50, 40, 50])
unique = np.unique(a)
print("Original Array:", a)
print("Unique Elements:", unique)

#15.Create two NumPy arrays and concatenate them
# horizontally and vertically.

import numpy as np
a = np.array([[1, 2],[3, 4]])
b = np.array([[5, 6],[7, 8]])
horizontal = np.hstack((a, b))
vertical = np.vstack((a, b))
print("First Array:")
print(a)
print("Second Array:")
print(b)
print("Horizontal Concatenation:")
print(horizontal)
print("Vertical Concatenation:")
print(vertical)
# 16.Store marks of 10 students in a NumPy array.
# Calculate:
# Highest marks
# Lowest marks
# Average marks
# Median
# Standard deviation
import numpy as np
marks = np.array([75, 82, 68, 90, 55, 78, 88, 65, 72, 95])
highest = np.max(marks)
lowest = np.min(marks)
average = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)
print("Marks:", marks)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Median:", median)
print("Standard Deviation:", std_dev)
#17.Take marks of 20 students, calculate the class average
# and display the marks of students who scored above the average.
import numpy as np
marks = np.array([65, 72, 45, 80, 55, 90, 68, 75, 82, 60,48, 95, 70, 85, 58, 77, 88, 52, 69, 92])
average = np.mean(marks)
print("Class Average:", average)
above_average = marks[marks > average]
print("Marks Above Average:", above_average)
#18.Write a Python program using NumPy to create a 3D array
# of shape (2, 3, 4) containing numbers from 1 to 24.
# Display the array and its:
# Number of dimensions
# Shape
# Size
import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:")
print(a)
print("Number of Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)
# 19.Create a 3D array of shape (2, 3, 4) and write a program
# to access:
# First element
# Last element
# Element at index [0,1,2]
# Element at index [1,2,3]
import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:")
print(a)
print("First Element:", a[0, 0, 0])
print("Last Element:", a[-1, -1, -1])
print("Element at [0,1,2]:", a[0, 1, 2])
print("Element at [1,2,3]:", a[1, 2, 3])
#20.Create a (2, 3, 4) array and calculate:
# Sum of all elements
# Sum of each layer
# Sum along rows
# Sum along columns
import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:")
print(a)
print("Sum of All Elements:", np.sum(a))
print("Sum of Each Layer:", np.sum(a, axis=(1, 2)))
print("Sum Along Rows:")
print(np.sum(a, axis=2))
print("Sum Along Columns:")
print(np.sum(a, axis=1))
#21.Create a 3D array of random integers between 1 and 100.
# Replace all values greater than 50 with 0.
import numpy as np
a = np.random.randint(1, 101, size=(2, 3, 4))
print("Original 3D Array:")
print(a)
a[a > 50] = 0
print("Array After Replacing Values Greater Than 50:")
print(a)

# 22.Generate a random 3D array of shape (3, 4, 5)
# and calculate its mean, median, standard deviation,
# variance, minimum, and maximum.

import numpy as np
a = np.random.randint(1, 101, size=(3, 4, 5))
print("Random 3D Array:")
print(a)
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))

# 23.Create a 3D NumPy array of shape (2, 3, 4)
# containing numbers from 1 to 24. Flatten the array into
# a one-dimensional array and display both the original
# and flattened arrays.

import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
flat_array = a.flatten()
print("Original 3D Array:")
print(a)
print("Flattened 1D Array:")
print(flat_array)

# 24.Create a 3D array containing integers from 1 to 27.
# Flatten the array and calculate:
# Sum
# Average
# Maximum
# Minimum
import numpy as np
a = np.arange(1, 28).reshape(3, 3, 3)
flat_array = a.flatten()
print("Flattened Array:")
print(flat_array)
print("Sum:", np.sum(flat_array))
print("Average:", np.mean(flat_array))
print("Maximum:", np.max(flat_array))
print("Minimum:", np.min(flat_array))

# 25.Create a random 3D NumPy array of shape (3, 4, 5).
# Flatten it and display only the elements that are:
# Greater than 50
# Even numbers
# Less than the average value

import numpy as np
a = np.random.randint(1, 101, size=(3, 4, 5))
flat_array = a.flatten()
average = np.mean(flat_array)
print("Original 3D Array:")
print(a)
print("Flattened Array:")
print(flat_array)
print("Elements Greater Than 50:")
print(flat_array[flat_array > 50])
print("Even Numbers:")
print(flat_array[flat_array % 2 == 0])
print("Average:", average)
print("Elements Less Than Average:")
print(flat_array[flat_array < average])
