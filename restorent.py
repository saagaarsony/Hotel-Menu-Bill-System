from tkinter import*
win = Tk()
win.title('The Restorent')
win.geometry('1000x300')
win.resizable(False,False)
win.iconbitmap('S:\p project\icon\icon.ico')

menu1 = Menu(win)
win.config(menu=menu1)

def show():
    win.geometry('1000x530')

def hide():
    win.geometry('1000x280')    

menu2 = Menu(menu1)
menu1.add_cascade(label='Rate List', menu=menu2)
menu2.add_command(label='Show Rate List', command=show)
menu2.add_command(label='Hide Rate List', command=hide)

lbl1 = Label(win, text="WlCOME TO THE RESTORENT", font=('Bell MT', 30, 'bold'), fg='#063970')
lbl1.pack()

# food
f1 = Frame(win , highlightbackground='#063970', highlightthickness='3', width=300, height=200)
f1.place(x=20, y=60)

Dosa = StringVar()
Jinny = StringVar()
Masala = StringVar()
Gol = StringVar()
Raj = StringVar()
Samosa = StringVar()
Gtotal = StringVar()
Water = StringVar()
Soda = StringVar()
Mozito = StringVar()
Gpani = StringVar()
Lassi = StringVar()
Chass = StringVar()

ldosa = Label(f1, text='Dosa', font=('Arial', 15), width=10, height=1 )
ldosa.grid(row=0, column=0)

ldosa = Label(f1, text='Jinny Dosa', font=('Arial', 15), width=10, height=1 )
ldosa.grid(row=1, column=0)

ldosa = Label(f1, text='Masala Dosa', font=('Arial', 15), width=10, height=1 )
ldosa.grid(row=2, column=0)

ldosa = Label(f1, text='Goll Gappa', font=('Arial', 15), width=10, height=1 )
ldosa.grid(row=3, column=0)

ldosa = Label(f1, text='Raj Kachoori', font=('Arial', 15), width=10, height=1 )
ldosa.grid(row=4, column=0)

ldosa = Label(f1, text='Samosa', font=('Arial', 15), width=10, height=1 )
ldosa.grid(row=5, column=0)

edosa = Entry(f1, textvariable=Dosa, width=10, font=('time new roman', 15, 'bold'))
edosa.grid(row=0, column=1, padx=20)

ejdosa = Entry(f1, textvariable=Jinny, width=10, font=('time new roman', 15, 'bold'))
ejdosa.grid(row=1, column=1, padx=20)

emdosa = Entry(f1, textvariable=Masala, width=10, font=('time new roman', 15, 'bold'))
emdosa.grid(row=2, column=1, padx=20)

egol = Entry(f1, textvariable=Gol, width=10, font=('time new roman', 15, 'bold'))
egol.grid(row=3, column=1, padx=20)

eraj = Entry(f1, textvariable=Raj, width=10, font=('time new roman', 15, 'bold'))
eraj.grid(row=4, column=1, padx=20)

esamosa = Entry(f1, textvariable=Samosa, width=10, font=('time new roman', 15, 'bold'))
esamosa.grid(row=5, column=1, padx=20)

lwater = Label(f1, text='Water', font=('Arial', 15), width=10, height=1 )
lwater.grid(row=0, column=3)

lsoda = Label(f1, text='Soda', font=('Arial', 15), width=10, height=1 )
lsoda.grid(row=1, column=3)

lmozi = Label(f1, text='Mozito', font=('Arial', 15), width=10, height=1 )
lmozi.grid(row=2, column=3)

lpani = Label(f1, text='Nibu Pani', font=('Arial', 15), width=10, height=1 )
lpani.grid(row=3, column=3)

llassi = Label(f1, text='Lassi', font=('Arial', 15), width=10, height=1 )
llassi.grid(row=4, column=3)

lchas = Label(f1, text='Chass', font=('Arial', 15), width=10, height=1 )
lchas.grid(row=5, column=3)

ewater = Entry(f1, textvariable=Water, width=10, font=('time new roman', 15, 'bold'))
ewater.grid(row=0, column=4, padx=20)

esoda = Entry(f1, textvariable=Soda, width=10, font=('time new roman', 15, 'bold'))
esoda.grid(row=1, column=4, padx=20)

emozi = Entry(f1, textvariable=Mozito, width=10, font=('time new roman', 15, 'bold'))
emozi.grid(row=2, column=4, padx=20)

epani = Entry(f1, textvariable=Gpani, width=10, font=('time new roman', 15, 'bold'))
epani.grid(row=3, column=4, padx=20)

elassi = Entry(f1, textvariable=Lassi, width=10, font=('time new roman', 15, 'bold'))
elassi.grid(row=4, column=4, padx=20)

echass = Entry(f1, textvariable=Chass, width=10, font=('time new roman', 15, 'bold'))
echass.grid(row=5, column=4, padx=20)

def reset():
    edosa.delete(0, END)
    ejdosa.delete(0,END)
    emdosa.delete(0,END)
    egol.delete(0,END)
    eraj.delete(0,END)
    esamosa.delete(0,END)

rbtn = Button(f1, text='Reset', font=('Arial', 12, 'bold'), width=15, bg='red', fg='white',command=reset)
rbtn.grid(row=6, column=0)

def total():
    try:
        a1 = int(Dosa.get())
    except:
        a1 = 0

    try:
        a2 = int(Jinny.get())
    except:
        a2 = 0    

    try:
        a3 = int(Masala.get())
    except:
        a3 = 0

    try:
        a4 = int(Gol.get())
    except:
        a4 = 0

    try:
        a5 = int(Raj.get())
    except:
        a5 = 0

    try:
        a6 = int(Samosa.get())
    except:
        a6 = 0

    try:
        b1 = int(Water.get()) 
    except:
        b1 = 0    

    try:
        b2 = int(Soda.get())
    except:
        b2 = 0

    try:
        b3 = int(Mozito.get())
    except:
        b3 = 0

    try:
        b4 = int(Gpani.get())
    except:
        b4 = 0

    try:
        b5 = int(Lassi.get())
    except:
        b5 = 0

    try:
        b6 = int(Chass.get()) 
    except:
        b6 = 0                                           

    cost1 = 50* a1
    cost2 = 100* a2
    cost3 = 80* a3
    cost4 = 40* a4
    cost5 = 60* a5
    cost6 = 30* a6
    cost7 = 10 * b1
    cost8 = 50 * b2
    cost9 = 80 * b3
    cost10 = 15 * b4
    cost11 = 55 * b5
    cost12 = 20 * b6

    totalcost = cost1+cost2+cost3+cost4+cost5+cost6+cost7+cost8+cost9+cost10+cost11+cost12
    string_bill= 'Rs.', str('%s' %totalcost)
    Gtotal.set(string_bill)

tbtn = Button(f1, text='Total', font=('Arial',12, 'bold'),width=15, bg='green', fg='white', command=total)
tbtn.grid(row=6, column=1, columnspan=6)        



f2 = Frame(win , highlightbackground='#063970', highlightthickness='3', width=300, height=200)
f2.place(x=680, y=60)

Flbl = Label(f2, text='All Total is', font=('Arial', 30, 'bold'))
Flbl.place(x=50, y=40)

Ftotal = Entry(f2, textvariable=Gtotal, font=('time new roman', 25), width=15)
Ftotal.place(x=10, y=100)

lbl2 = Label(win, text='Rate List Of All Food That We Have...........', font=('Bell MT', 25), fg='#063970')
lbl2.place(x=20,y=280)

lbl3 = Label(win, text='FOODS...........', font=('arial', 12, 'bold'), fg='#063970')
lbl3.place(x=20,y=315)

lbl4 = Label(win, text='Dosa         --50\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl4.place(x=20,y=340)

lbl5 = Label(win, text='Jinny Dosa--100\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl5.place(x=20,y=370)

lbl6 = Label(win, text='Masala Dosa--80\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl6.place(x=20,y=400)

lbl7 = Label(win, text='GolGappa     --40\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl7.place(x=20,y=430)

lbl8 = Label(win, text='Raj Kachoori    --60\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl8.place(x=20,y=460)

lbl9 = Label(win, text='Samosa    --30\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl9.place(x=20,y=490)

lbl10 = Label(win, text='Drinks...........', font=('arial', 12, 'bold'), fg='#063970')
lbl10.place(x=250,y=315)

lbl11 = Label(win, text='water         --10\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl11.place(x=250,y=340)

lbl12 = Label(win, text='Soda          --50\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl12.place(x=250,y=370)

lbl13 = Label(win, text='Mozito        --80\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl13.place(x=250,y=400)

lbl14 = Label(win, text='GolGappa Pani --15\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl14.place(x=250,y=430)

lbl15 = Label(win, text='Lassi         --55\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl15.place(x=250,y=460)

lbl16 = Label(win, text='Chaas         --20\-', font=('arial', 10), fg='blue',highlightbackground='blue', highlightthickness=1)
lbl16.place(x=250,y=490)



win.mainloop()