#1. Create and display an integer array
import array as arr
a = arr.array('i', [1, 2, 3])
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

#2. Create and display a double array
a = arr.array('d', [2.5, 3.2, 3.3])
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")


#3.Insert an element into an array
a = arr.array('i', [1, 2, 3])
a.insert(1, 4)
print("Array after insertion : ", end=" ")
for i in a:
    print(i, end=" ")


#4.Append an element to an array
a = arr.array('i', [1, 2, 3])
a.append(4)
print("Array after append : ", end=" ")
for i in a:
    print(i, end=" ")


#5. Remove an element from an array
a = arr.array('i', [1, 2, 3, 4])
a.remove(3)
print("Array after removing 3 : ", end=" ")
for i in a:
    print(i, end=" ")


#6. Pop an element from an array
a = arr.array('i', [1, 2, 3, 4])
a.pop()
print("Array after pop : ", end=" ")
for i in a:
    print(i, end=" ")


#7. Slicing an array
a = arr.array('i', [1, 2, 3, 4, 5])
b = a[1:4]
print("Sliced array : ", end=" ")
for i in b:
    print(i, end=" ")

#8. Search an element in an array
a = arr.array('i', [10, 20, 30, 40, 50])
num = int(input("Enter element to search: "))
if num in a:
    print("Element found")
else:
    print("Element not found")


#9. Find the index of an element
a = arr.array('i', [10, 20, 30, 40, 50])
num = int(input("Enter element: "))
if num in a:
    print("Index of element:", a.index(num))
else:
    print("Element not found")

#10. Count an element in an array
a = arr.array('i', [1, 2, 2, 3, 2, 4])
num = int(input("Enter element: "))
print("Count:", a.count(num))

#11.Reverse an array
a = arr.array('i', [1, 2, 3, 4, 5])
a.reverse()
print("Reversed array : ", end=" ")
for i in a:
    print(i, end=" ")


#12. Update an element in an array
a = arr.array('i', [10, 20, 30, 40])
a[2] = 35
print("Updated array : ", end=" ")
for i in a:
    print(i, end=" ")


#13. Find length of an array
a = arr.array('i', [10, 20, 30, 40, 50])
print("Length of array:", len(a))


#14. Extend an array
a = arr.array('i', [1, 2, 3])
b = arr.array('i', [4, 5, 6])
a.extend(b)
print("Array after extending : ", end=" ")
for i in a:
    print(i, end=" ")


#15. Convert array into a list
a = arr.array('i', [1, 2, 3, 4, 5])
b = a.tolist()
print("List:", b)


#16. Convert list into an array
numbers = [10, 20, 30, 40]
a = arr.array('i', numbers)
print("Array : ", end=" ")
for i in a:
    print(i, end=" ")


#17. Find sum of array elements
a = arr.array('i', [10, 20, 30, 40, 50])
total = sum(a)
print("Sum of elements:", total)


#18. Find largest and smallest element
a = arr.array('i', [10, 50, 20, 5, 30])
print("Largest element:", max(a))
print("Smallest element:", min(a))


#19. Display alternate elements
a = arr.array('i', [1, 2, 3, 4, 5, 6])
b = a[::2]
print("Alternate elements : ", end=" ")
for i in b:
    print(i, end=" ")


#20. Delete an array
a = arr.array('i', [1, 2, 3, 4, 5])
print("Array:", a)
del a
print("Array deleted successfully")
