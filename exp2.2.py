#create program to calculate area of trianagle , vol of sphere, total surface area of cylinder,area of square
base=int(input("Enter base:"))
height=int(input("Enter height:"))
at=0.5*base*height
print("Area of triangle:",at)
print("---------")
r=float(input("enter radius:"))
v_s=4/3*3.14*r**3
print("volume of sphere:",v_s)
print("---------")
h=int(input("Enter height:"))
r1=float(input("enter radius:"))
total=2*3.14*r1*(r1+h)
print("total surface area of cylinder:",total)
print("---------")
s=int(input("enter the side:"))
a_s=s*s
print("Area of square:",a_s)
print("------------------------------------------------------------------------------")



#wap to convert pounds into kg,km into miles
pounds=int(input("enter pounds value:"))
kg=pounds*0.453592
print("Pounds to Kg:",kg)
km=int(input("enter kilo miter value:"))
kilo=km*0.621371
print("km to miles:",kilo)


#wap to calculate factorial of number
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
print("------------------------------------------------------------------------------")


#wap to check number is prime or not
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
print("------------------------------------------------------------------------------")



#wap to check the number is palindrome or not
n=int(input("enter a number:"))
rev=0
num=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
    
if num==rev:
    print("palindrome")
else:
    print("not palindrome")
print("------------------------------------------------------------------------------")


    
#wap to convert decimal to binary, decimal to hexadecimal,decimal to octal
num = int(input("Enter a decimal number: "))
print("Binary =", bin(num))
num = int(input("Enter a decimal number: "))
print("hexadecimal =", hex(num))
num = int(input("Enter a decimal number: "))
print("octal =", oct(num))
print("------------------------------------------------------------------------------")



#wap to factors of a number
n=int(input("enter a number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
print("------------------------------------------------------------------------------")


        
#wap to find ascii value of character
ch = input("Enter a character: ")
print("ASCII value of", ch, "is", ord(ch))
print("------------------------------------------------------------------------------")


