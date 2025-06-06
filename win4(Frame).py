import tkinter
from tkinter import*

root=Tk()
root.geometry("140x100")
frame=Frame(root)
frame.pack()

rightframe=Frame(root)
rightframe.pack(side=RIGHT)

leftframe=Frame(root)
leftframe.pack(side=LEFT)

rb=Button(frame,text="red",fg="red",activebackground="red")
rb.pack(side=LEFT)

bb=Button(frame,text="blue",fg="blue",activebackground="red")
bb.pack(side=RIGHT)

gb=Button(rightframe,text="green",fg="green")
gb.pack(side=RIGHT)

yb=Button(leftframe,text="yellow",fg="yellow")
yb.pack(side=LEFT)

root.mainloop()
