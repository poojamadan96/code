from tkinter import *
class CheckDemo(Frame):
	def __init__(self,m):
		super().__init__(m)
		self.val1=IntVar()
		self.val2=IntVar()
		self.male=Checkbutton(self,text='Male',variable=self.val1)
		self.female=Checkbutton(self,text='Female',variable=self.val2)
		self.male.grid(row=1,column=1)
		self.female.grid(row=2,column=1)
		self.pack()
	def show(self):
		print("Hello")
root=Tk()
ob=CheckDemo(root)
root.title("Check box demo")
root.geometry('350x300')
root.mainloop()
