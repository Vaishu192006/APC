#Write a PYTHON program to print the natural numbers up to n
n=int(input("enter the size of natural number:"))
i=1
while i<=n:
    print(i)
    i+=1

#Write a PYTHON program to print even numbers up to n
n=int(input("enter the size of natural number:"))
i=0
while i<=n:
    i=i+2
    print(i)

#Write a PYTHON program to print odd numbers up to n
n=int(input("enter the size of natural number:"))
i=1
while i<=n:
    print(i)
    i=i+2

#Write a PYTHON program to print sum of natural numbers up to n
n=int(input("enter the size of natural number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print(sum)


#Write a PYTHON program to print sum of odd numbers up to n
n=int(input("enter the size of natural number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+2
print(sum)

#Write a PYTHON program to print sum of even numbers up to n
n=int(input("enter the size of natural number:"))
sum=0
i=2
while i<=n:
    sum=sum+i
    i=i+2
print(sum)

#Write a PYTHON program to print natural numbers up to n in reverse order.
n=int(input("enter the size of natural number:"))

while n>=1:
    print(n)
    n=n-1

#Write a PYTHON program to print Fibonacci series up to n

n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 1
while count <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1

#Write a PYTHON program  find a factorial of given number

n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1

print("Factorial =", fact)

#Write a PYTHON program to check the entered number is prime or not

n = int(input("Enter a number: "))
i = 2
flag = 0

while i < n:
    if n % i == 0:
        flag = 1
        break
    i += 1

if n <= 1:
    print("Not Prime")
elif flag == 0:
    print("Prime Number")
else:
    print("Not Prime")


#Write a PYTHON program to find the sum of digits of given number

n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)

#Write a PYTHON program to check the entered  number is palindrome or not

n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

#Write a PYTHON program to reverse the given number.
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed Number =", rev)

#Write a PYTHON program to print the multiplication table
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

#Write a PYTHON program to print the largest of n numbers
n = int(input("Enter how many numbers: "))
i = 1
largest = None

while i <= n:
    num = int(input("Enter number: "))
    if largest is None or num > largest:
        largest = num
    i += 1

print("Largest number =", largest)

#Write a PYTHON program to print smallest of n numbers

n = int(input("Enter how many numbers: "))

i = 1
smallest = None

while i <= n:
    num = int(input("Enter number: "))
    if smallest is None or num < smallest:
        smallest = num
    i += 1

print("Smallest number =", smallest)





    

