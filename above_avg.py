print("Write a PYTHON program to check weather number is even or odd.")
n=int(input("enter the number:"))
if n%2==0:
    print(n,"is even number")
else:
    print(n,"is odd number")
print("------------------------------------------------------------------------------")


    
print("Write a PYTHON program to check a year for leap year.")
year=int(input("enter year:"))
if (year%4==0 and year%100!=0)or(year%400==0):
    print(year,"leap year")
else:
    print(year,"not leap year")
print("------------------------------------------------------------------------------")



print("A company insures its drivers in the following cases")
m=input("are you married(yes/no):")
g=input("enter your gender(male/female):")
a=int(input("enter your age:"))
if m=='yes':
    print("comany will give you insures")
elif m=='no' and a>=30 and g=='male':
    print("comany will give you insures")
elif m=='no' and a>=25 and g=='female':
    print("comany will give you insures")
else:
    print("insures are not allowed")
print("------------------------------------------------------------------------------")


    
    
