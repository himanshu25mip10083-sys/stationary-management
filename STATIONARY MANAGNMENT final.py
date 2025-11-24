from tkinter import*
root=Tk()
root.geometry("1200x600")
root.title("stationary managnment")
root.resizable(False,False)

def Reset():
    entry_pencil.delete(0,END)
    entry_eraser.delete(0,END)
    entry_pen.delete(0,END)
    entry_ruler.delete(0,END)
    entry_sharpner.delete(0,END)
    entry_pencilbox.delete(0,END)
    entry_paintcolours.delete(0,END)
    entry_whitner.delete(0,END)
    entry_sketchpen.delete(0,END)
    total_bill.set("")

def Total():
    try:a1=int(pencil.get())
    except:a1=0

    try:a2=int(eraser.get())
    except:a2=0

    try:a3=int(pen.get())
    except:a3=0

    try:a4=int(ruler.get())
    except:a4=0

    try:a5=int(sharpner.get())
    except:a5=0

    try:a6=int(pencilbox.get())
    except:a6=0

    try:a7=int(paintcolours.get())
    except:a7=0

    try:a8=int(whitner.get())
    except:a8=0

    try:a9=int(sketchpen.get())
    except:a9=0

    #define cost per item
    c1=5*a1
    c2=3*a2
    c3=5*a3
    c4=10*a4
    c5=5*a5
    c6=50*a6
    c7=50*a7
    c8=30*a8
    c9=20*a9

    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="yellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7+c8+c9
    total_bill.set(f"Rs. {totalcost}")


Label(text="STATIONARY MANAGNMENT",bg="red",fg="white",font=("algebra",33),
      highlightbackground="black",highlightthickness=2,width="300",height="2").pack()

#main menu
f=Frame(root,bg="orange",highlightbackground="red",highlightthickness=2,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Main Menu",font=("gabriola",40,"bold","underline"),fg="white",bg="orange").place(x=60,y=0)
Label(f,text="1.  pencil.......5/-",font=("arial",15,"bold"),fg="black",bg="orange").place(x=30,y=80)
Label(f,text="2.  eraser.......3/-",font=("arial",15,"bold"),fg="black",bg="orange").place(x=30,y=110)
Label(f,text="3.  pen.......5/-",font=("arial",15,"bold"),fg="black",bg="orange").place(x=30,y=140)
Label(f,text="4.  ruler.......10/-",font=("arial",15,"bold"),fg="black",bg="orange").place(x=30,y=170)
Label(f,text="5.  sharpner.......5/-",font=("arial",15,"bold"),fg="black",bg="orange").place(x=30,y=200)
Label(f,text="6.  pencil box.......50/-",font=("arial",15,"bold"),fg="black",bg="orange").place(x=30,y=230)
Label(f,text="7.  paint colours.......50/-",font=("arial",15,"bold"),fg="black",bg="orange").place(x=30,y=260)
Label(f,text="8.  whitner.......30/-",font=("arial",15,"bold"),fg="black",bg="orange").place(x=30,y=290)
Label(f,text="9.  sketch pen.......20/-",font=("arial",15,"bold"),fg="black",bg="orange").place(x=30,y=320)

#entry work
f1=Frame(root,bd=5,bg="blue",height=370,width=300,relief=RAISED)
f1.pack()

pencil=StringVar()
eraser=StringVar()
pen=StringVar()
ruler=StringVar()
sharpner=StringVar()
pencilbox=StringVar()
paintcolours=StringVar()
whitner=StringVar()
sketchpen=StringVar()
total_bill=StringVar()

#label
Label(f1,font=("aria",20,"bold"),text="pencil",width=12,fg="blue4").grid(row=1,column=0)
Label(f1,font=("aria",20,"bold"),text="eraser",width=12,fg="blue4").grid(row=2,column=0)
Label(f1,font=("aria",20,"bold"),text="pen",width=12,fg="blue4").grid(row=3,column=0)
Label(f1,font=("aria",20,"bold"),text="ruler",width=12,fg="blue4").grid(row=4,column=0)
Label(f1,font=("aria",20,"bold"),text="sharpner",width=12,fg="blue4").grid(row=5,column=0)
Label(f1,font=("aria",20,"bold"),text="pencil box",width=12,fg="blue4").grid(row=6,column=0)
Label(f1,font=("aria",20,"bold"),text="paint colours",width=12,fg="blue4").grid(row=7,column=0)
Label(f1,font=("aria",20,"bold"),text="whitner",width=12,fg="blue4").grid(row=8,column=0)
Label(f1,font=("aria",20,"bold"),text="sketch pen",width=12,fg="blue4").grid(row=9,column=0)

#entry boxes (corrected)
entry_pencil=Entry(f1,font=("aria",20,"bold"),textvariable=pencil,bd=4,width=6,bg="lightpink")
entry_pencil.grid(row=1,column=1)

entry_eraser=Entry(f1,font=("aria",20,"bold"),textvariable=eraser,bd=4,width=6,bg="lightpink")
entry_eraser.grid(row=2,column=1)

entry_pen=Entry(f1,font=("aria",20,"bold"),textvariable=pen,bd=4,width=6,bg="lightpink")
entry_pen.grid(row=3,column=1)

entry_ruler=Entry(f1,font=("aria",20,"bold"),textvariable=ruler,bd=4,width=6,bg="lightpink")
entry_ruler.grid(row=4,column=1)

entry_sharpner=Entry(f1,font=("aria",20,"bold"),textvariable=sharpner,bd=4,width=6,bg="lightpink")
entry_sharpner.grid(row=5,column=1)

entry_pencilbox=Entry(f1,font=("aria",20,"bold"),textvariable=pencilbox,bd=4,width=6,bg="lightpink")
entry_pencilbox.grid(row=6,column=1)

entry_paintcolours=Entry(f1,font=("aria",20,"bold"),textvariable=paintcolours,bd=4,width=6,bg="lightpink")
entry_paintcolours.grid(row=7,column=1)

entry_whitner=Entry(f1,font=("aria",20,"bold"),textvariable=whitner,bd=4,width=6,bg="lightpink")
entry_whitner.grid(row=8,column=1)

entry_sketchpen=Entry(f1,font=("aria",20,"bold"),textvariable=sketchpen,bd=4,width=6,bg="lightpink")
entry_sketchpen.grid(row=9,column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=('arial',16,'bold'),width=10,text="reset",command=Reset)
btn_reset.grid(row=10,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="total",command=Total)
btn_total.grid(row=10,column=1)

#bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=800,y=118)

bill=Label(f2,text="bill",font=("calibri",20),bg="lightyellow")
bill.place(x=120,y=10)

root.mainloop()
