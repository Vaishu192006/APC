import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to Tkinter",
                 font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me",
                   command=lambda: label.config(text="Hello!"))
button.pack()

root.mainloop()
import tkinter as tk

def add():
    a = int(e1.get())
    b = int(e2.get())
    result.config(text="Sum = " + str(a + b))

root = tk.Tk()
root.title("Addition")
root.geometry("300x250")

tk.Label(root, text="Enter First Number").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Enter Second Number").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Button(root, text="Add", command=add).pack(pady=10)

result = tk.Label(root, text="Result")
result.pack()

root.mainloop()


import tkinter as tk
from tkinter import messagebox

def submit():
    name = e1.get()
    roll = e2.get()
    gender = gender_var.get()
    course = course_var.get()

    messagebox.showinfo(
        "Student Details",
        f"Name: {name}\nRoll No: {roll}\n"
        f"Gender: {gender}\nCourse: {course}"
    )

root = tk.Tk()
root.title("Student Registration")
root.geometry("350x400")

tk.Label(root, text="Student Registration",
         font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Student Name").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Roll Number").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Gender").pack()

gender_var = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male",
               variable=gender_var, value="Male").pack()

tk.Radiobutton(root, text="Female",
               variable=gender_var, value="Female").pack()

tk.Label(root, text="Select Course").pack()

course_var = tk.StringVar(value="BTech")

tk.OptionMenu(root, course_var,
              "BTech", "BCA", "MCA", "MBA").pack()

tk.Button(root, text="Submit",
          command=submit).pack(pady=20)

root.mainloop()


import tkinter as tk
from tkinter import messagebox

def login():
    username = e1.get()
    password = e2.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Login")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")

tk.Label(root, text="Username").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Password").pack()
e2 = tk.Entry(root, show="*")
e2.pack()

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()
