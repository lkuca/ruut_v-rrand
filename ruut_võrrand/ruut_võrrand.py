from cmath import sqrt
from ctypes import c_bool, c_buffer
from gettext import npgettext
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
def lahenda():
    if ent1.get()=="":
        ent1.configure(bg="red")
    else:
        ent1.configure(bg="Lightblue")
    if ent2.get()=="":
        ent2.configure(bg="red")
    else:
        ent2.configure(bg="Lightblue")
    if ent3.get()=="":
        ent3.configure(bg="red")
    else:
        ent3.configure(bg="Lightblue")
    if ent1.get()!="" and ent2.get!="" and ent3.get!="":
        a_=float(ent1.get())
        b_=float(ent2.get())
        c_=float(ent3.get())
        D=b_*b_-4*a_*c_ 
        if D>0:
            x1=round((-1*ent2-sqrt(D))/(2*ent1),2)
            x2=round((-1*ent2+sqrt(D))/(2*ent1),2)
            vas=f"x1={x1} \nx2={x2}"
        elif D==0:
            x1=round((-1*ent2)/(2*ent1),2)
            vas=f"x1={x1}"
        else:
            vas="Lahendust pole"
        vastus.configure(text=vas)
def graafika():
    a_=float(ent1.get())
    b_=float(ent2.get())
    c_=float(ent3.get())
    x0=(-b_)/2*a_ 
    y0=a_*x0*x0+b_*x0+c_ 
    x=np.arange(x0-15, x0+15,1)#min, max,step
    y=a_*x*x+b_*x+c_ 
    fig=plt.figure()
    plt.plot(x,y,'r-d')
    plt.title("ruudvõrrand")
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)
    plt.show()
matemaatika=Tk()
matemaatika.geometry("700x200")
matemaatika.title("ruut võrrand")
lbl1=Label(matemaatika,text="ruut võrrandi lahendamine",bg="blue",fg="#b2cf87",font="Arial 20",height=1)
ent1=Entry(matemaatika,fg="blue",bg="Lightblue",width=5, font= "Arial 20",justify=LEFT)
lbl2=Label(matemaatika,text="x**2+",bg="white",fg="#b2cf87",font="Arial 20",height=1)
lbl4=Label(matemaatika,text="x+",bg="white",fg="#b2cf87",font="Arial 20",height=1)
ent2=Entry(matemaatika,fg="blue",bg="Lightblue",width=5, font= "Arial 20",justify=CENTER)
lbl3=Label(matemaatika,text="=0",bg="white",fg="#b2cf87",font="Arial 20",height=1)
ent3=Entry(matemaatika,fg="blue",bg="Lightblue",width=5, font= "Arial 20",justify=RIGHT)
btn=Button(matemaatika,text="lahenda",font="Arial 24",relief=GROOVE,fg="green",command=lahenda)#SUNKEN, RAISED
vastus=Label(matemaatika,text="LAhendus",bg="yellow",fg="#b2cf87",font="Arial 20",height=1, width=10)
grafik=Button(matemaatika,text="graafik",fg="#b2cf87",font="Arial 20",height=1, command=graafika)
lbl1.pack()
ent1.pack(side=LEFT)
lbl2.pack(side=LEFT)
ent2.pack(side=LEFT)
lbl4.pack(side=LEFT)
lbl3.pack(side=LEFT)
btn.pack(side=RIGHT)
grafik.pack(side=RIGHT)
ent3.pack(side=LEFT)
vastus.pack(side=BOTTOM)

matemaatika.mainloop()
