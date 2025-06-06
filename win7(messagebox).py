import tkinter
from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("300x200")

w=Label(root, text='ITDLH Polonnaruwa',font="50")
w.pack()

messagebox.showinfo("show information","Type Your Message Here")
messagebox.showwarning("show warning","Warning Message")
messagebox.showerror("show error","Error")
messagebox.askquestion("Ask Question","Are You Sure?")
messagebox.askokcancel("Ask ok Cancel","Want To Continue")
messagebox.askyesno("Ask Yes No Question","Find The Value")
messagebox.askretrycancel("ask retry cancel","Try Again")
root,mainloop()
