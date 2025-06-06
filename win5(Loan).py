import tkinter
from tkinter import*

root=Tk()
root.geometry("440x400")
root.title('Loan')
root.configure(bg="pink")
root.resizable(False,False)

interst=""
total=""

def cal():
    global interst
    global total
    interst=""
    total=""
    amount=float(entry1.get())
    rate=float(entry1.get())
    time=int(entry1.get())
    interest=amount*rate*time/100
    total=amount+interest
    round(interest,2)
    round(total,2)
    entry4.insert(END,interest)
    entry5.insert(END,total)

def clear():
    
    entry4.delete(0.0,END) #Textbox
    entry1.delete(0,END)   #Entry
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry5.delete(0.0,END)
    
    
    
    
    
    

    

#Label

labelm=Label(root,text="Loan Calculator",bg="pink",fg="#000",font=("arial",18))
labelm.place(x=142,y=3)
label1=Label(root,text="Basic Amount",bg="pink",fg="#000",font=("arial",12))
label1.place(x=10,y=52)
label2=Label(root,text="Interest Rate",bg="pink",fg="#000",font=("arial",12))
label2.place(x=10,y=92)
label3=Label(root,text="Time(Dates)",bg="pink",fg="#000",font=("arial",12))
label3.place(x=10,y=132)
label4=Label(root,text="Interest",bg="pink",fg="#000",font=("arial",12))
label4.place(x=10,y=172)
label5=Label(root,text="Total",bg="pink",fg="#000",font=("arial",12))
label5.place(x=10,y=212)



#Entry
entry1=Entry(root,width=30,bg="#fff",fg="#000",font=("arial",12))
entry1.place(x=150,y=52)
entry2=Entry(root,width=30,bg="#fff",fg="#000",font=("arial",12))
entry2.place(x=150,y=92)
entry3=Entry(root,width=30,bg="#fff",fg="#000",font=("arial",12))
entry3.place(x=150,y=132)


#text

entry4=Text(root,width=30,height=1,bg="#fff",fg="#000",font=("arial",12))
entry4.place(x=150,y=172)
entry5=Text(root,width=30,height=1,wrap=WORD,bg="#fff",fg="#000",font=("arial",12))
entry5.place(x=150,y=212)

#button
button1=Button(text="Calculate",width=15,height=2,bg="#fff",fg="#000",font=("arial",12),command=lambda:cal())
button1.place(x=10,y=300)
button2=Button(text="Clear",width=15,height=2,bg="#fff",fg="#000",font=("arial",12),command=lambda:clear())
button2.place(x=278,y=300)



root.mainloop()

