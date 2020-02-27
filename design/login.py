#login.py
from tkinter import *
class Demo(Frame):
	def __init__(self,arg):
		super().__init__(arg)
		self.b1=Button(self,text='login')
		self.b1.grid(row=1,column=1)
		self.pack()

root=Tk()
ob=Demo(root)
root.title('Pathal')
root.geometry('500x350')
root.mainloop()

