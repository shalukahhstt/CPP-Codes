import tkinter
from tkinter import*
win=Tk()
win.geometry('380x320')
win.title('My contacts')
win.configure(bg='black')
win.resizable(FALSE,FALSE)


mycontact={'itdlh':'027123312'}

def find():
    name=e_name.get()
    name.lower()
    result=mycontact[name]
    txt_t1.delete(0.0,END)
    txt_t1.insert(END,result)
    print(result)

def add():
    addcontactname=addname.get()
    addcontactname=addcontactname.lower()
    addcontacttel=addtel.get()
    mycontact.update({addcontactname:addcontacttel})
    addname.delete(0,END)
    addtel.delete(0,END)
    print("Contact Added Successful")

def delete():
    e_name.delete(0,END)
    txt_t1.delete(0.0,END)
    

#create find section
Label(win,text='FIND CONTACTS',font='none 14',bg='black',fg='white').place(x=130,y=3)
Label(win,text='Name',font='none 13',bg='black',fg='white').place(x=2,y=43)
Label(win,text='Tel No',font='none 13',bg='black',fg='white').place(x=2,y=83)

e_name=Entry(win,width=45,font=("Agency FB",12))
e_name.place(x=100,y=43)
txt_t1=Text(win,width=45,height=1,font=("Agency FB",12))
txt_t1.place(x=100,y=83)

b1=Button(win,text='Find',width=10,activebackground="pink",command=find)
b1.place(x=295,y=123)

b3=Button(win,text='Delete',width=10,activebackground="pink",command=delete)
b3.place(x=5,y=123)

#create add section
Label(win,text='ADD CONTACTS',font='none 14',bg='black',fg='white').place(x=130,y=163)
Label(win,text='Add Name',font='none 13',bg='black',fg='white').place(x=2,y=203)
Label(win,text='Add Tel No',font='none 13',bg='black',fg='white').place(x=2,y=243)

addname=Entry(win,width=45,font=("Agency FB",12))
addname.place(x=100,y=203)
addtel=Entry(win,width=45,font=("Agency FB",12))
addtel.place(x=100,y=243)

b2=Button(win,text='Add Numbers',width=10,activebackground="pink",command=add)
b2.place(x=295,y=283)

#place controls on the window










