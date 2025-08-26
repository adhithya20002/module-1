from tkinter import*
def login():
    email = email_entry.get()
    password = password_entry.get()
    print("Email:", email)
    print("Password:", password)
root =Tk()
root.title("Facebook Login")
root.geometry("300x300")
root.configure(bg="White")
Label(root, text="facebook", fg= "Dodger Blue", bg="White",font=("Facebook Sans", 28, "bold")).pack(pady=10)
email_entry = Entry(root, width=30)
email_entry.insert(0, "Email or Phone")
email_entry.pack(pady=5)
password_entry =Entry(root, width=30)
password_entry.insert(0, "Password")
password_entry.pack(pady=10)
Button(root, text="Log In", bg= "Dodger Blue",fg="white", width=30).pack(pady=10)
Label(root, text="Forgotten account?", fg= "Dodger Blue", bg="White").pack()
Label(root, text="Sign up for Facebook", fg="Dodger Blue", bg="White").pack()
root.mainloop()





