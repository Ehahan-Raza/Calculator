from tkinter import *
root=Tk()

def click(event):
    global scvalue
    text=event.widget.cget("text")
    
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        
        else:
            value=eval(screen.get())
        
        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root.geometry("400x600")
root.title("Calculator")
# root.config(background="Black")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root, textvariable=scvalue,font="Lucida 40 bold")
screen.pack(fill=X,ipadx=10,padx=12,pady=12)

f1=Frame(root,bg="grey",width=400,height=50)
b1=Button(f1,text="9",font="Lucida 20 bold",padx=10,pady=10,borderwidth=4,relief=RAISED)
b1.pack(side="left",anchor="w")
b1.bind("<Button-1>",click)

b2=Button(f1,text="8",font="Lucida 20 bold",padx=10,pady=10,borderwidth=4,relief=RAISED)
b2.pack(side="left",anchor="w",padx=10)
b2.bind("<Button-1>",click)

b3=Button(f1,text="7",font="Lucida 20 bold",padx=10,pady=10,borderwidth=4,relief=RAISED)
b3.pack(side="left",anchor="w")
b3.bind("<Button-1>",click)
f1.pack()

f2=Frame(root,bg="grey",width=400,height=50)
b4=Button(f2,text="6",font="Lucida 20 bold",padx=10,pady=10,borderwidth=4,relief=RAISED)
b4.pack(side="left",anchor="w")
b4.bind("<Button-1>",click)

b5=Button(f2,text="5",font="Lucida 20 bold",padx=10,pady=10,borderwidth=4,relief=RAISED)
b5.pack(side="left",anchor="w",padx=10)
b5.bind("<Button-1>",click)

b6=Button(f2,text="4",font="Lucida 20 bold",padx=10,pady=10,borderwidth=4,relief=RAISED)
b6.pack(side="left",anchor="w")
b6.bind("<Button-1>",click)
f2.pack()

f3=Frame(root,bg="grey",width=400,height=50)
b7=Button(f3,text="3",font="Lucida 20 bold",padx=10,pady=10,borderwidth=4,relief=RAISED)
b7.pack(side="left",anchor="w")
b7.bind("<Button-1>",click)

b8=Button(f3,text="2",font="Lucida 20 bold",padx=10,pady=10,borderwidth=4,relief=RAISED)
b8.pack(side="left",anchor="w",padx=10)
b8.bind("<Button-1>",click)

b9=Button(f3,text="1",font="Lucida 20 bold",padx=10,pady=10,borderwidth=4,relief=RAISED)
b9.pack(side="left",anchor="w")
b9.bind("<Button-1>",click)
f3.pack()

f4=Frame(root,bg="grey",width=300,height=250)
b10=Button(f4,text="=",font="Comic 20 bold",borderwidth=4,padx=15,relief=RAISED)
b10.pack(side=LEFT,pady=4)
b10.bind("<Button-1>",click)
b11=Button(f4,text="C",font="Comic 20 bold",borderwidth=4,padx=15,relief=RAISED)
b11.pack(side=LEFT,pady=4)
b11.bind("<Button-1>",click)
b12=Button(f4,text="0",font="Comic 20 bold",borderwidth=4,padx=15,relief=RAISED)
b12.pack(side=LEFT,pady=4)
b12.bind("<Button-1>",click)
b12=Button(f4,text="00",font="Comic 20 bold",borderwidth=4,padx=15,relief=RAISED)
b12.pack(side=LEFT,pady=4)
b12.bind("<Button-1>",click)
f4.pack(pady=20)

f4=Frame(root,bg="grey",width=300,height=250)
b13=Button(f4,text="-",font="Comic 20 bold",borderwidth=4,padx=15,relief=RAISED)
b13.pack(side=LEFT,pady=5)
b13.bind("<Button-1>",click)
b14=Button(f4,text="*",font="Comic 20 bold",borderwidth=4,padx=15,relief=RAISED)
b14.pack(side=LEFT)
b14.bind("<Button-1>",click)
b15=Button(f4,text="/",font="Comic 20 bold",borderwidth=4,padx=15,relief=RAISED)
b15.pack(side=LEFT)
b15.bind("<Button-1>",click)
b16=Button(f4,text="%",font="Comic 20 bold",borderwidth=4,padx=15,relief=RAISED)
b16.pack(side=LEFT)
b16.bind("<Button-1>",click)
f4.pack()

b17=Button(root,text=" + ",font="Comic 30 bold",borderwidth=4,padx=15,relief=RAISED)
b17.pack(side=BOTTOM,pady=10,padx=40)
b17.bind("<Button-1>",click)

# b17=Button(root,text="Exit",font="Comic 19 bold",borderwidth=4,padx=1,relief=RAISED)
# b17.pack(side=LEFT,pady=10)
# b17.bind("<Button-1>",quit)

root.mainloop()