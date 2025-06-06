import tkinter
from tkinter import*
#define function
def click():
    word=entrybox.get()
    word=word.lower()#can enter in uppercase or lowercase
    outbox.delete(0.0,END)
    try:
        defi=mydic[word]
    except:
        defi='Sorry Learn English First'
    outbox.insert(END,defi)

def on1(e):
    b1["bg"]="#8accff"
    b1["fg"]="white"
def off1(e):
    b1["bg"]="#fff"
    b1["fg"]="#000"
    


main=Tk()
main.geometry('710x95+360+0')
main.title('My App')
main.configure(bg='pink')
main.resizable(False,False)

#create a Label
label1=Label(main, text='Enter a Word',bg='Pink',fg='blue',font=("arial" ,12 ,"bold"))
label1.place(x=10,y=3)


#create an entry to input keyword
entrybox=Entry(main,width=20,bg='white',font=10)
entrybox.place(x=200,y=3)


#create a button
b1=Button(main,text='Submit',width='20',activebackground="red",command=click)
b1.place(x=550,y=3)

#create a Label
label2=Label(main, text='Meaning ',bg='Pink',fg='black',font='arial 12 bold')
label2.place(x=10,y=50)


#create Text Box
outbox=Text(main,width=62,height=2,wrap=WORD,bg='white',fg='purple')
outbox.place(x=200,y=50)

#bind
b1.bind("<Enter>",on1)
b1.bind("<Leave>",off1)

#create dictiionary
mydic={'cpu':'Central Processing Unit','alu':'Arithmetic & Logic Unit'}


main.mainloop()

