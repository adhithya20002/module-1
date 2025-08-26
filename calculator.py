# def add(a,b):
#     return a+b


# def subtract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     if b==0:
#         return "Error : division by zero"

#     return a/b






from tkinter import *

def calculate(exp):
    try:
        result.set(eval(exp))
    except:
        result.set("Error")

root = Tk()
root.title("Calculator")

result = StringVar()

Entry(root, textvar=result, font=("Arial", 18), justify="right").grid(row=0, column=0, columnspan=4)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0","C","=","+"
]

row, col = 1, 0
for b in buttons:
    def cmd(x=b):
        if x == "=":
            calculate(result.get())
        elif x == "C":
            result.set("")
        else:
            result.set(result.get()+x)
    Button(root, text=b, width=5, height=2, command=cmd).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
