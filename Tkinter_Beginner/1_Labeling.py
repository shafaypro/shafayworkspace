from Tkinter import *

root =Tk()
label1 = Label(root, text='Welcome to the First Application of Tkinter')
Button1 = Button(root,text="Clickme")
Button2 = Button(root,text="Another Clicker")
label1.pack()
Button1.pack()
Button2.pack()
root.mainloop()