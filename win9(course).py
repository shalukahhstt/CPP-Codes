import tkinter
from tkinter import*
from tkinter import ttk
import os
import openpyxl

win=Tk()
win.geometry('240x270')

def add_data():
    title=title_combobox.get()
    name=name_entry.get()
    age=int(age_spinbox.get())
    course=course_combobox.get()

#create Excel sheet
    filepath=r"D:\Shaluka\Python\win9(course)registration.xlsx"
    if not os.path.exists(filepath):
        workbook=openpyxl.Workbook()
        sheet=workbook.active
        heading=["Title","Name","Age","Course Name"]
        workbook.save(filepath)

#insert data to excel sheet
    workbook=openpyxl.load_workbook(filepath)
    sheet=workbook.active
    sheet.append([title,name,age,course])
    workbook.save(filepath)



title_label=Label(win,text='Title',font='none 12').place(x=5,y=25)
title_combobox=ttk.Combobox(win,width='15',values=['Mr','Mrs','Miss'])
title_combobox.place(x=120,y=25)

name_label=Label(win,text='Name',font='none 12').place(x=5,y=65)
name_entry=Entry(win,width='12',font='none 12')
name_entry.place(x=120,y=65)

age_label=Label(win,text='Age',font='none 12').place(x=5,y=105)
age_spinbox=Spinbox(win,font='none 12',width=11,from_=1,to=150)
age_spinbox.place(x=120,y=105)

Label(win,text='Course Name',font='none 12').place(x=5,y=145)
course_combobox=ttk.Combobox(win,width='15',values=['MS Office','Web Development','Programming'])
course_combobox.place(x=120,y=145)

add_button=Button(text='Add Data',font='none 12',width=10,activebackground="pink",command=add_data)
add_button.place(x=133,y=225)

win.mainloop()
                        
