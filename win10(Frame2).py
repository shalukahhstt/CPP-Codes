import tkinter
from tkinter import*

root=Tk()
root.title('Using Frames')
root.geometry('800x600')



topf=LabelFrame(root,text='Top Frame')
topf.pack(side=TOP,expand='yes',fill='both')

bottomf=LabelFrame(root,text='Top Frame')
bottomf.pack(side=BOTTOM,expand='yes',fill='both')

bottomleftf=LabelFrame(bottomf,text='Bottom Left Frame')
bottomleftf.pack(side=LEFT,expand='yes',fill='both')

bottomrightf=LabelFrame(bottomf,text='Bottom Rifht Frame')
bottomrightf.pack(side=RIGHT,expand='yes',fill='both')


l1=Label(topf,text='Enter Your Name ',font=14)
l1.place(x=10,y=10)
e1=Entry(topf)
e1.place(x=250,y=10)

l2=Label(bottomleftf,text='Enter Your Email ',font=14)
l2.place(x=10,y=10)
e2=Entry(bottomleftf)
e2.place(x=250,y=10)

root.mainloop()


