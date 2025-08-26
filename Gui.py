# from tkinter import*
# root=Tk()
# root.title("Welcome to python lobby ")
# root.geometry('300x500')
# root.mainloop()


# from tkinter import*
# root=Tk()
# root.title("Welcome to python lobby")
# lbl=Label(root,text="Hello")
# lbl.pack()
# root.mainloop()


# from tkinter import*
# root=Tk()
# root.title("Welcome to python lobby")
# lbl=Label(root,text="Hello")
# lbl.place(x=100,y=300)

# entry=Entry(root,width=20)
# entry.pack()
# root.mainloop()


# from tkinter import*
# root=Tk()
# root.title("Welcome to python lobby")
# root.config(bg="lightblue")
# def clicked():
#     print("I am clicked")
# btn=Button(root,text="Click me",command=clicked) 
# btn.pack() 
# root.geometry('300x500')
# root.mainloop() 



######## PHOTOIMAGE ##########

# from tkinter import*
# root=Tk()
# label=Label(root,text='This is image').pack(side=TOP,pady=10)
# path=PhotoImage(file=r"C:\Users\ss\Downloads\notes-1136234_1280.png")
# label_image=Label(root,image=path,width=400,height=800)
# label_image.pack()
# root.geometry("900x400")
# root.title("Pythonlobby.com")
# root.mainloop()


########### GRID #############

# from tkinter import*
# root=Tk()
# root.title("pythonlobby")
# w=Label(root,text='Redzone',bg="red",fg="white")
# w.grid(row=0,column=0)
# w=Label(root,text='Green Glossy',bg="light green",fg="white")
# w.grid(row=0,column=0)
# w=Label(root,text='light yellow',bg="blue",fg="white")
# w.grid(row=0,column=0)
# root.geometry("250x150")
# root.mainloop()



######## CHECK BOXES ###########

# from tkinter import*
# root=Tk()
# root.title("pythonlobby")
# w=Label(root,text="pythonlobby.com",font="60")
# w.pack()
# checkbox1=IntVar()
# checkbox2=IntVar()
# Button0=Checkbutton(root,text="learning",variable=checkbox1,onvalue=1,offvalue=0,height=3,width=12)
# Button1=Checkbutton(root,text="learning",variable=checkbox1,onvalue=1,offvalue=0,height=3,width=12)
# Button0.pack()
# Button1.pack()
# root.geometry("320x200")
# root.mainloop()


######### RADIO BUTTON ##########

from tkinter import*
root=Tk()
root.title("pythonlobby")
value1=StringVar(root,"2")
rbtn1=Radiobutton(root,text="RadioButton 1",variable=value1,value="1")
rbtn1.pack()
rbtn2=Radiobutton(root,text="RadioButton 2",variable=value1,value="2")
rbtn2.pack()
rbtn3=Radiobutton(root,text="RadioButton 3",variable=value1,value="3")
rbtn3.pack()
root.geometry("320x200")
root.mainloop()


########## FRAMES ###########

from tkinter import*
root=Tk()
label=Label(root,text="pythonlobby",font="60")
label.pack()
bottom_frame=Frame(root,bg="green",width=120,height=100)
bottom_frame.pack(side=LEFT,padx=20)
top_frame=Frame(root,bg="red",width=120,height=100)
top_frame.pack(side=LEFT,padx=20)
root.geometry("320x200")
root.mainloop()


######## MENU BAR ######### 

# from tkinter import*
# root=Tk()
# root.title("Menubutton Example")
# menubtn=Menubutton(root,text="options",relief="raised",direction="below")
# menubtn.grid(padx=20,pady=20)
# menu=Menu(menubtn,tearoff=0)
# menubtn.config(menu=menu)
# menu.add_command(label="option1",command=lambda:print("option1 selected"))
# menu.add_command(label="option2",command=lambda:print("option2 selected"))
# menu.add_separator()
# menu.add_command(label="Exit",command=root.quit)
# root.mainloop()



######## LIST BOX ##########


# from tkinter import*
# root=Tk()
# listbox=Listbox(root,width=45,height=15,selectmode=MULTIPLE)
# listbox.pack(pady=20)
# listbox.insert(0,"c")
# listbox.insert(1,"c++")
# listbox.insert(2,"java")
# listbox.insert(3,"python")
# root.title("Python;obby.com")
# root.mainloop()



######## Message box ###########

# from tkinter import*
# from tkinter import messagebox
# root=Tk()
# def callback():
#     messagebox.showinfo("well done great !")
#     print("You clicked Delete")
# button1=Button(root,text="Delete",command=callback)
# button1.grid(row=0,column=0,padx=90,pady=50)
# root.geometry("350x250")
# root.title("pythonLobby")
# root.mainloop()      




# from tkinter import*
# from tkinter import messagebox
# root=Tk()
# def callback():
#     m_box=messagebox.askquestion("Info","Are you sure!",icon="warning")
#     if (m_box=="yes"):
#         print("yes")
#     else:
#         print("no")
# button1=Button(root,text="Delete",command=callback)
# button1.grid(row=0,column=0,padx=90,pady=50)
# root.geometry("350x250")
# root.title("pythonLobby")
# root.mainloop()



####### Message Box #########


from tkinter import*
root=Tk()
def callback():
    # text=textEditor.get("0.1",END)
    print('text')
textEditor=Text(root,width=43,height=10)
textEditor.pack()
button1=Button(root,text="Display Text",command=callback)
button1.pack(pady=12)
root.geometry("350x250")
root.title("pythonLobby")
root.mainloop()   