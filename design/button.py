from tkinter import *
class Demo(Frame):
	def __init__(self,m): #radot button self ,text, string, value
		super().__init__(m)
		self.val=StringVar(value=False)
		self.r1=Radiobutton(self, text="Python",variable=self.val,value="Python",command=self.show)
		self.r2=Radiobutton(self, text="Java",variable=self.val,value="java",command=self.show)
		self.r3=Radiobutton(self, text=".Net",variable=self.val,value=".net",command=self.show)
		self.l1=Label(self)
		self.r1.grid(row=1,column=1)
		self.r2.grid(row=2,column=1)
		self.r3.grid(row=3,column=1)
		self.l1.grid(row=4,column=1)
		self.pack()
	def show(self):
		msg='Selection: '+self.val.get()
		self.l1.config(text=msg) #blamk label p value add k lye
root=Tk()
ob=Demo(root)
root.title("Radio button example")
root.geometry('350x300')
root.mainloop()
