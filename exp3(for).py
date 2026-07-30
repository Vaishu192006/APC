#Write a PYTHON program to print the natural numbers up to n
n=int(input("enter size of natural number:"))
for i in range(1,n+1):
    print(i)
print("=====================")

#Write a PYTHON program to print even numbers up to n
n=int(input("enter size of natural number:"))
for i in range(2,n+1,2):
    print("even no:",i)
print("=====================")

#Write a PYTHON program to print odd numbers up to n
n=int(input("enter size of natural number:"))
for i in range(1,n+1,2):
    print("odd no:",i)
print("=====================")

#Write a PYTHON program that prints  1 2 4 8 16 32 … n2
n=int(input("enter size of natural number:"))
value=1
for i in range(n):
    print(value)
    value=value*2
#Write a PYTHON program to sum the given sequence
     # 1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!
# Program to find the sum of the series:
# 1 + 1/1! + 1/2! + ... + 1/n!

n = int(input("Enter the value of n: "))
sum_series = 1.0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    sum_series += 1 / factorial

print("Sum of the series =", sum_series)

# Program to compute cos(x) using series

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))
sum = 1
fact = 1
sign = -1

for i in range(2, 2 * n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum += sign * (x ** i) / fact
    sign *= -1

print("Cos(", x, ") =", sum)
print("=====================")

# Program to check whether the square root of a number is prime or not

import math
n = int(input("Enter a number: "))
root = int(math.sqrt(n))

if root * root != n:
    print("Square root is not a whole number.")
else:
    prime = True
    if root < 2:
        prime = False
    else:
        for i in range(2, int(math.sqrt(root)) + 1):
            if root % i == 0:
                prime = False
                break
    if prime:
        print("Square root =", root)
        print("Square root is Prime.")
    else:
        print("Square root =", root)
        print("Square root is Not Prime.")
print("=====================")

#Write a PYTHON program to produce following design
#			A B C 
#			A B C 
#			A B C


for i in range(3):
    for ch in ['A','B','C']:
        print(ch, end=" ")
    print()
print("=====================")



# 9.Program to print the pattern

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
print("=====================")


#10. Write a PYTHON program to produce following design
n = int(input("Enter the value of n: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
print("=====================")


# Program to print the pattern

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("=====================")


# Program to print the pattern

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
print("=====================")













