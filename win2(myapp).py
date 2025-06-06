from tkinter import*
#define function
def click():
    word=entrybox.get()
    word=word.lower()
    outbox.delete(0.0,END)
    try:
        defi=mydic[word]
    except:
        defi='Sorry Learn English First'
    outbox.insert(END,defi)

main=Tk()
main.geometry('800x600+360+0')
main.title('My App')
main.configure(bg='pink')

#create a Label
label1=Label(main, text='Enter a Word',bg='Pink',fg='blue',font=("Agency FB" ,18 ,"bold"))
label1.grid(row=1,column=0,sticky=W)

#create an entry to input keyword
entrybox=Entry(main,width=20,bg='white',font=16)
entrybox.grid(row=1,column=2,sticky=W)

#create a button
Button(main,text='Submit',width='20',activebackground="red",command=click).grid(row=1,column=3,sticky=W)

#create a Label
label2=Label(main, text='\n\nMeaning ',bg='Pink',fg='black',font='arial 18 bold')
label2.grid(row=2,column=0,sticky=W)

#create Text Box
outbox=Text(main,width=50,height=10,wrap=WORD,bg='white',fg='purple')
outbox.grid(row=4,column=0,sticky=W)

#create dictiionary
mydic={'cpu':'Central Processing Unit','alu':'Arithmetic & Logic Unit'}


main.mainloop()
