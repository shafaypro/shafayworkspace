from Tkinter import *
root = Tk() # This creates a Tkinter Frame of Root Lines
root.title("@_ButtonLayout")
root.geometry("200x200")
frontFrame = Frame(root)
frontFrame.pack()
BottomFrame = Frame (root)
BottomFrame.pack(side=BOTTOM) # this packs the Bottom Frame layout with the Bottom Section
Button1 = Button(frontFrame, text="Button1", fg = "red")
Button2 = Button(frontFrame, text="Button2", fg = "Blue")
Button3 = Button(frontFrame, text="Button3", fg = "Grey")
Button4 = Button(BottomFrame, text="Button4", fg = "Yellow")
Button1.pack(side=LEFT)
Button2.pack(side=LEFT)    # All the layout side is done at the packing section in such a way that the packing is possible easily
Button3.pack(side=LEFT)
Button4.pack(side=BOTTOM)
root.mainloop()  # This runs the gui program in the loop unless the exit button is clicked to generate an event