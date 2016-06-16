from tkinter import *  # imports the tkinter header file


class Window(Frame):  # Starts a windows instance
	def __init__(self, master=None):  # the constructor of the Windows Class
		Frame.__init__(self, master)  # a self frame is created using this
		self.master = master  # intialize the master with the current frame master (variable)



root = Tk() # creates an object of the tkinter class
app = Window(root)  # to pass the root of tkinter to the class created
root.mainloop()  # to display the tkinter result