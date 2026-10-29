
# 1
import math

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(7), Rectangle(10, 5), Triangle(10, 6)]

for shape in shapes:
    print("Area:", shape.area())


# 2
class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary + self.salary * 0.30


class Developer(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary + self.salary * 0.20


class Tester(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary + self.salary * 0.15


employees = [
    Manager(50000),
    Developer(40000),
    Tester(35000)
]

for employee in employees:
    print("Salary:", employee.calculate_salary())


# 3
class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a key")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()


# 4
class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog says Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says Moo")


class Lion(Animal):
    def sound(self):
        print("Lion says Roar")


animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()


# 5
class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()


# 6
class Student:
    def calculate_grade(self, marks):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        else:
            return "F"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 65:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    print("Grade:", student.calculate_grade(80))


# 7
class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.06


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

for account in accounts:
    print("Interest:", account.calculate_interest(100000))


# 8
class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def generate_report(report):
    report.generate()


generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(HTMLReport())


# 9
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        feet = self.feet + other.feet

        if total_inches >= 12:
            feet += total_inches // 12
            total_inches = total_inches % 12

        return Distance(feet, total_inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(3, 7)

d3 = d1 + d2
d3.display()


# 10
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Rahul", 85)
s2 = Student("Amit", 75)

print("Rahul has greater marks:", s1 > s2)
print("Rahul has lower marks:", s1 < s2)


# 11
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 60000)
p2 = Product("Mobile", 30000)

print("Prices are equal:", p1 == p2)
print("Laptop is more expensive:", p1 > p2)


# 12
class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI Payment of", amount, "completed")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card Payment of", amount, "completed")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet Payment of", amount, "completed")


def process_payment(payment, amount):
    payment.make_payment(amount)


process_payment(UPIPayment(), 1000)
process_payment(CardPayment(), 2000)
process_payment(WalletPayment(), 500)


# 13
class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [
    Student(),
    Faculty(),
    Administrator()
]

for person in people:
    person.display_role()


# 14
class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing Audio")


class Video(Media):
    def play(self):
        print("Playing Video")


class Podcast(Media):
    def play(self):
        print("Playing Podcast")


media_list = [
    Audio(),
    Video(),
    Podcast()
]

for media in media_list:
    media.play()


# 15
class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")


class AC(SmartDevice):
    def turn_on(self):
        print("AC is ON")

    def turn_off(self):
        print("AC is OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")


devices = [
    Light(),
    Fan(),
    AC(),
    TV()
]

for device in devices:
    device.turn_on()
    device.turn_off()
