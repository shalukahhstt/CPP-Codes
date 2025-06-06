from tkinter import*
import tkinter
import tkinter as tk
from tkinter import ttk
import openpyxl
import os

def add():
    #read data
    title=titlec.get()
    name=namee.get()
    age=int(agespin.get())
    course=coursec.get()
    olict='Done' if ict.get() else 'not'

    #add data
    path=r'D:\Shaluka\Python\registration.xlsx'
    workbook=openpyxl.load_workbook(path)
    sheet=workbook.active
    row_values=[title,name.age,course,olict]
    sheet.append(row_values)
    workbook.save(path)
    
    #insert row view
    treeview.insert('',tk.END,values=row_values)

def style():
    if mode_switch.instate(['selected']):
        style.theme_use('forest-light')
    else:
        style.theme_use('forest-dark') 

def load():
    path=r'D:\Shaluka\Python\registration.xlsx'
    workbook=openpyxl.load_workbook(path)
    sheet=workbook.active
    listValues=list(sheet.values)
    for col_name in listValues[0]:
        treeview.heading(col_name, text=col_name)
    for value_tuple in listValues[1:]:
        treeview.insert('',tk.END,values=value_tuple)

    

root=tk.Tk()
root.title('Registration')
root.resizable(FALSE,FALSE)

clist=['MS Office','Web Development','Software Development','Graphic Designing']

#Create Frame

frame=ttk.Frame(root)
frame.pack()
inputf=ttk.LabelFrame(frame,text='Data In')
inputf.grid(row=0,column=0,padx=10,pady=20)

#Widgets

#Title
titlel=ttk.Label(inputf,text="Title",font="none 12")
titlel.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
titlec=ttk.Combobox(inputf,width="10",values=['Mr','Mrs','Miss'])
titlec.grid(row=0,column=1,sticky="w",padx=5,pady=10)

#name
namel=ttk.Label(inputf,text="Name",font="none 12")
namel.grid(row=1,column=0,sticky="ew",padx=5,pady=10)
namee=Entry(inputf,font="none 12",width="25")
namee.grid(row=1,column=1,sticky="ew",padx=5,pady=10)

#age
agel=ttk.Label(inputf,text="Age",font="none 12")
agel.grid(row=2,column=0,sticky="ew",padx=5,pady=10)
agespin=ttk.Spinbox(inputf,width=6, from_=16, to=25)
agespin.insert(0,'Age')
agespin.grid(row=2,column=1,sticky="w",padx=5,pady=10)

#course
coursel=ttk.Label(inputf,text="Course Name",font="none 12")
coursel.grid(row=3,column=0,sticky="ew",padx=5,pady=10)
coursec=ttk.Combobox(inputf,width="30",values=clist)
coursec.current(0)
coursec.grid(row=3,column=1,sticky="ew",padx=5,pady=10)

#Button

ict=tk.BooleanVar()
checkb=ttk.Checkbutton(inputf,text="OL ICT",variable=ict)
checkb.grid(row=4,column=1,sticky="w",padx=5,pady=10)

addb=ttk.Button(inputf,text="Add Data",command=add)
addb.grid(row=5,column=1,sticky="ew",padx=5,pady=10)

modes=ttk.Checkbutton(inputf,text="Mode",style='Switch',command=style)
modes.grid(row=6,column=0,sticky="nsew",padx=5,pady=10)

showf=ttk.Frame(frame)
showf.grid(row=0,column=1,paddy=10)
scrlbar=ttk.Scrollbar(showf)
scrlbar.pack(side='right',fill='y')

cols=('Title','Name','Age','Course Name','OL ICT')
treeview=ttk.Treeview(showframe,show='headings',yscrollcommand=scrlbar.set,column=cols,height=14)

treeview.pack()
scrlbar.config(command=treeview.yview)

treeview.column('Title',width=50)
treeview.column('Name',width=50)
treeview.column('Age',width=50)
treeview.column('Course Name',width=150)
treeview.column('OL ICT',width=50)
treeview.pack()

Load()











root.mainloop()
