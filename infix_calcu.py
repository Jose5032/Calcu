from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA INFIJA")
#ventana.configure(background="gray12")
ventana.geometry("360x490")

Entry(ventana,font=('Arial',20,"bold"),width=23,bd=2,bg="PaleGreen3",justify="right").place(x=4,y=30)

Button(ventana,text="7",width=7,height=2).place(x=4,y=150)
Button(ventana,text="8",width=7,height=2).place(x=80,y=150)
Button(ventana,text="9",width=7,height=2).place(x=152,y=150)
Button(ventana,text="CE",width=7,height=2).place(x=224,y=150)
Button(ventana,text="C",width=7,height=2).place(x=296,y=150)
Button(ventana,text="4",width=7,height=2).place(x=4,y=208)
Button(ventana,text="5",width=7,height=2).place(x=80,y=208)
Button(ventana,text="6",width=7,height=2).place(x=152,y=208)
Button(ventana,text="X",width=7,height=2).place(x=224,y=208)
Button(ventana,text="%",width=7,height=2).place(x=296,y=208)
Button(ventana,text="1",width=7,height=2).place(x=4,y=266)
Button(ventana,text="2",width=7,height=2).place(x=80,y=266)
Button(ventana,text="3",width=7,height=2).place(x=152,y=266)
Button(ventana,text="+",width=7,height=2).place(x=224,y=266)
Button(ventana,text="-",width=7,height=2).place(x=296,y=266)
Button(ventana,text="0",width=7,height=2).place(x=4,y=324)
Button(ventana,text="+/-",width=7,height=2).place(x=80,y=324)
Button(ventana,text=".",width=7,height=2).place(x=152,y=324)
Button(ventana,text="EXP",width=7,height=2).place(x=224,y=324)
Button(ventana,text="=",width=7,height=2).place(x=296,y=324)
ventana.mainloop()

