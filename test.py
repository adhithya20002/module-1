from tkinter import *
root = Tk()
root.title("Login Page")
root.config(bg="blue")
root.geometry("500x600")
def login():
    if user.get() == "adhithya123" and password.get() == "16123":
        print("Login Successful")
    else:
        print("Login Failed")
lbl1=Label(root, text="Username")
lbl1.pack()
user=Entry(root)
user.pack()
lbl2=Label(root, text="Password")
lbl2.pack()
password = Entry(root)
password.pack()
btn = Button(root, text="Login", command=login)
btn.pack()
root.mainloop()


##base class vehicle using inheritence car bike truck and display details

class Vehicle:
    def __init__(self, car, bike, truck):
        self.car=car
        self.bike=bike
        self.truck=truck        
    def display_vehicle(self):
        print("Car name is:",self.car)
        print("Bike name is:",self.bike)
        print("Truck name is:",self.truck)
veh = Vehicle("Swift","Abc","Xyz")
veh.display_vehicle()


##program to find the sum of multiple numbers

# num=int("Enter the number")
# total=sum(num)
# print("sum of numbers is ",num)