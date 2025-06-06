import tkinter
from tkinter import*

root=Tk()
root.geometry("495x548+100+200")
root.title("Calculator")
root.configure(bg="#000")
root.resizable(False,False)

num=""
n1=""
n2=""
f=""
equation=""


def click(value):
    global num
    global equation
    equation+=value
    num+=value
    result.config(text=num)
    result1.config(text=equation)

def fun(sym):
    global num
    global equation
    equation+=sym
    n1=num
    f=sym
    num+=sym
    result.config(text=num)
    result1.config(text=equation)
    num=""

def eq(equal):
    global num
    global equation
    ans=""
    n2=num
    result1.config(text=equation)
    ans=eval(equation)
    result.config(text=ans)
    
    result1.config(text=equation+"=")
    num=""
            
    
              
def clear():
    global num
    global equation
    num=""
    equation=""
    result.config(text=num)
    result1.config(text=equation)

#hover

#on
    
def on7(e):
    b7["bg"]="#8accff"
    b7["fg"]="white"
def on8(e):
    b8["bg"]="#8accff"
    b8["fg"]="white"
def on9(e):
    b9["bg"]="#8accff"
    b9["fg"]="white"
def on4(e):
    b4["bg"]="#8accff"
    b4["fg"]="white"
def on5(e):
    b5["bg"]="#8accff"
    b5["fg"]="white"
def on6(e):
    b6["bg"]="#8accff"
    b6["fg"]="white"
def on1(e):
    b1["bg"]="#8accff"
    b1["fg"]="white"
def on2(e):
    b2["bg"]="#8accff"
    b2["fg"]="white"
def on3(e):
    b3["bg"]="#8accff"
    b3["fg"]="white"
def on0(e):
    b0["bg"]="#8accff"
    b0["fg"]="white"
def onp(e):
    bp["bg"]="#8accff"
    bp["fg"]="white"
def one(e):
    be["bg"]="#e6f600"
    be["fg"]="black"
def onc(e):
    bc["bg"]="#bfdafa"
    bc["fg"]="#0000ff"
def ond(e):
    bd["bg"]="orange"
    bd["fg"]="#000"
def onmulti(e):
    multi["bg"]="#e633f0"
    multi["fg"]="#000"
def ondivide(e):
    divide["bg"]="#e633f0"
    divide["fg"]="#000"
def onminus(e):
    minus["bg"]="#e633f0"
    minus["fg"]="#000"
def onadd(e):
    add["bg"]="#e633f0"
    add["fg"]="#000"

#off
    
def off7(e):
    b7["bg"]="#fff"
    b7["fg"]="#000"
def off8(e):
    b8["bg"]="#fff"
    b8["fg"]="#000"
def off9(e):
    b9["bg"]="#fff"
    b9["fg"]="#000"
def off4(e):
    b4["bg"]="#fff"
    b4["fg"]="#000"
def off5(e):
    b5["bg"]="#fff"
    b5["fg"]="#000"
def off6(e):
    b6["bg"]="#fff"
    b6["fg"]="#000"
def off1(e):
    b1["bg"]="#fff"
    b1["fg"]="#000"
def off2(e):
    b2["bg"]="#fff"
    b2["fg"]="#000"
def off3(e):
    b3["bg"]="#fff"
    b3["fg"]="#000"
def off0(e):
    b0["bg"]="#fff"
    b0["fg"]="#000"
def offp(e):
    bp["bg"]="#fff"
    bp["fg"]="#000"
def offe(e):
    be["bg"]="#f45f00"
    be["fg"]="#fff"
def offc(e):
    bc["bg"]="#0000ff"
    bc["fg"]="#fff"
def offd(e):
    bd["bg"]="#c61600"
    bd["fg"]="#fff"
def offmulti(e):
    multi["bg"]="violet"
    multi["fg"]="#fff"
def offdivide(e):
    divide["bg"]="violet"
    divide["fg"]="#fff"
def offminus(e):
    minus["bg"]="violet"
    minus["fg"]="#fff"
def offadd(e):
    add["bg"]="violet"
    add["fg"]="#fff"






#margin
result1=Label(root,text="",width=41,height=1,font=("arial",10),bg="black",fg="white")
result1.pack()

#answere
result=Label(root,text="",width=25,height=2,font=("arial",24))
result.pack()

#functions

multi=Button(root,text="x",width=7,height=2,font=("arial",18,"bold"),bg="violet",fg="#fff",bd=2,command=lambda:fun("*"))
multi.place(x=10,y=108)
divide=Button(root,text="/",width=7,height=2,font=("arial",18,"bold"),bg="violet",fg="#fff",bd=2,command=lambda:fun("/"))
divide.place(x=131,y=108)
minus=Button(root,text="-",width=7,height=5,font=("arial",18,"bold"),fg="#fff",bg="violet",bd=2,command=lambda:fun("-"))
minus.place(x=10,y=196)
add=Button(root,text="+",width=7,height=5,font=("arial",18,"bold"),fg="#fff",bg="violet",bd=2,command=lambda:fun("+"))
add.place(x=10,y=372)

#Delete

bd=Button(root,text="Del",width=7,height=2,font=("arial",18,"bold"),bg="#c61600",fg="#fff",bd=2)
bd.place(x=252,y=108)

#clear

bc=Button(root,text="C",width=7,height=2,font=("arial",18,"bold"),bg="#0000ff",fg="#fff",bd=2,command=lambda:clear())
bc.place(x=373,y=108)

#Numbers

b7=Button(root,text="7",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("7"))
b7.place(x=131,y=196)
b8=Button(root,text="8",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("8"))
b8.place(x=252,y=196)
b9=Button(root,text="9",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("9"))
b9.place(x=373,y=196)

b4=Button(root,text="4",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("4"))
b4.place(x=131,y=284)
b5=Button(root,text="5",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("5"))
b5.place(x=252,y=284)
b6=Button(root,text="6",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("6"))
b6.place(x=373,y=284)

b1=Button(root,text="1",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("1"))
b1.place(x=131,y=372)
b2=Button(root,text="2",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("2"))
b2.place(x=252,y=372)
b3=Button(root,text="3",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("3"))
b3.place(x=373,y=372)

bp=Button(root,text=".",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("."))
bp.place(x=131,y=460)
b0=Button(root,text="0",width=7,height=2,font=("arial",18,"bold"),fg="#000",bg="#fff",bd=2,command=lambda:click("0"))
b0.place(x=252,y=460)

#Equal

be=Button(root,text="=",width=7,height=2,font=("arial",18,"bold"),fg="#fff",bg="#f45f00",bd=2,command=lambda:eq("="))
be.place(x=373,y=460)

#bind
b7.bind("<Enter>",on7)
b7.bind("<Leave>",off7)
b8.bind("<Enter>",on8)
b8.bind("<Leave>",off8)
b9.bind("<Enter>",on9)
b9.bind("<Leave>",off9)
b4.bind("<Enter>",on4)
b4.bind("<Leave>",off4)
b5.bind("<Enter>",on5)
b5.bind("<Leave>",off5)
b6.bind("<Enter>",on6)
b6.bind("<Leave>",off6)
b1.bind("<Enter>",on1)
b1.bind("<Leave>",off1)
b2.bind("<Enter>",on2)
b2.bind("<Leave>",off2)
b3.bind("<Enter>",on3)
b3.bind("<Leave>",off3)
b0.bind("<Enter>",on0)
b0.bind("<Leave>",off0)
bp.bind("<Enter>",onp)
bp.bind("<Leave>",offp)
be.bind("<Enter>",one)
be.bind("<Leave>",offe)
bc.bind("<Enter>",onc)
bc.bind("<Leave>",offc)
bd.bind("<Enter>",ond)
bd.bind("<Leave>",offd)
multi.bind("<Enter>",onmulti)
multi.bind("<Leave>",offmulti)
divide.bind("<Enter>",ondivide)
divide.bind("<Leave>",offdivide)
minus.bind("<Enter>",onminus)
minus.bind("<Leave>",offminus)
add.bind("<Enter>",onadd)
add.bind("<Leave>",offadd)




root.mainloop()
