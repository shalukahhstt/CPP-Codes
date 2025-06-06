import tkinter
from tkinter import*

root=Tk()
root.geometry('270x150')
root.configure(bg='pink')
root.title('Pass/Fail')
root.resizable(FALSE,FALSE)

def click():
    mark1=t1.get()
    t2.delete(0.0,END)
    try:
        mark=int(mark1)
        if mark>100 :
            result='Invalid Marks'
        elif mark>=45:
            result='You are Pass'
        elif mark>=0 :
            result='You are Fail'
        else:
            result='Invalid Marks'
            
    except:
        result='Invalid Marks'
        
    t2.insert(END,result)

l1=Label(root,text='MY MARKS',font=("arial",16),bg='pink',fg='#000')
l1.place(x=77,y=1)

l2=Label(root,text='Input Marks',font=("arial",12),bg='pink',fg='#000')
l2.place(x=2,y=50)

t1=Entry(root,width=8,font=("arial",12),fg='#000')
t1.place(x=180,y=50)

b1=Button(root,text='Submit',width=10,height=1,font=("arial",9),fg='#000',activebackground='orange',command=lambda:click())
b1.place(x=180,y=80)

t2=Text(root,width=28,height=1,font=("arial",12),fg='#000')
t2.place(x=2,y=118)

root.mainloop()
