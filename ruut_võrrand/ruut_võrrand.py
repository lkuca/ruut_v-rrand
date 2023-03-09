from tkinter import *
matemaatika=Tk()
matemaatika.geometry("1000x1000")
matemaatika.title("ruut võrrand")
lbl=Label(matemaatika,text="ruut võrrandi lahendamine",bg="blue",fg="#b2cf87",font="Arial 20",height=5,width=15)
ent=Entry(matemaatika,fg="blue",bg="Lightblue",width=15, font= "Arial 20",justify=LEFT)
lbl=Label(matemaatika,text="x**2+",bg="white",fg="#b2cf87",font="Arial 20",height=5,width=15)
ent=Entry(matemaatika,fg="blue",bg="Lightblue",width=15, font= "Arial 20",justify=CENTER)
lbl=Label(matemaatika,text="=0",bg="white",fg="#b2cf87",font="Arial 20",height=5,width=15)
ent=Entry(matemaatika,fg="blue",bg="Lightblue",width=15, font= "Arial 20",justify=RIGHT)
btn=Button(matemaatika,text="lahenda",font="Arial 24",relief=GROOVE,fg="green")#SUNKEN, RAISED
