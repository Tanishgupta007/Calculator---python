from tkinter import *
from tkinter import messagebox
import math

screen = Tk()
screen.title("Calculator - Tanish Gupta")
screen.configure(bg='yellow')
screen.iconbitmap('icon.ico')
screen.maxsize(width=470, height=485)
screen.minsize(width=363, height=485)
screen.geometry('363x485')


def click(number):
    global operator
    operator += str(number)
    tex.set(operator)


def clear():
    global operator
    operator = ''
    tex.set(operator)


def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong\n or contact: Tanish Gupta', parent=screen)
def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong\n or contact: Tanish Gupta', parent=screen)

def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong\n or contact: Tanish Gupta', parent=screen)
def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong\n or contact: Tanish Gupta', parent=screen)

def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong\n or contact: Tanish Gupta', parent=screen)

def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong\n or contact: Tanish Gupta', parent=screen)

def on_enter1(e):
    btn1.configure(bg='red')
def on_leave1(e):
    btn1.configure(bg='powder blue')
def on_enter2(e):
    btn2.configure(bg='red')
def on_leave2(e):
    btn2.configure(bg='powder blue')
def on_enter3(e):
    btn3.configure(bg='red')
def on_leave3(e):
    btn3.configure(bg='powder blue')
def on_enter4(e):
    btn4.configure(bg='red')
def on_leave4(e):
    btn4.configure(bg='powder blue')
def on_enter5(e):
    btn5.configure(bg='red')
def on_leave5(e):
    btn5.configure(bg='powder blue')
def on_enter6(e):
    btn6.configure(bg='red')
def on_leave6(e):
    btn6.configure(bg='powder blue')
def on_enter7(e):
    btn7.configure(bg='red')
def on_leave7(e):
    btn7.configure(bg='powder blue')
def on_enter8(e):
    btn8.configure(bg='red')
def on_leave8(e):
    btn8.configure(bg='powder blue')
def on_enter9(e):
    btn9.configure(bg='red')
def on_leave9(e):
    btn9.configure(bg='powder blue')
def on_enteradd(e):
    btnadd.configure(bg='red')
def on_leaveadd(e):
    btnadd.configure(bg='powder blue')
def on_enter0(e):
    btn0.configure(bg='red')
def on_leave0(e):
    btn0.configure(bg='powder blue')
def on_enterminus(e):
    btnminus.configure(bg='red')
def on_leaveminus(e):
    btnminus.configure(bg='powder blue')
def on_entermul(e):
    btnmul.configure(bg='red')
def on_leavemul(e):
    btnmul.configure(bg='powder blue')
def on_enterdiv(e):
    btndiv.configure(bg='red')
def on_leavediv(e):
    btndiv.configure(bg='powder blue')
def on_enterC(e):
    btnclear.configure(bg='red')
def on_leaveC(e):
    btnclear.configure(bg='orange')
def on_enterequal(e):
    btnequal.configure(bg='red')
def on_leaveequal(e):
    btnequal.configure(bg='powder blue')
def on_entersin(e):
    btnsin.configure(bg='red')
def on_leavesin(e):
    btnsin.configure(bg='powder blue')
def on_entercos(e):
    btncos.configure(bg='red')
def on_leavecos(e):
    btncos.configure(bg='powder blue')
def on_entertan(e):
    btntan.configure(bg='red')
def on_leavetan(e):
    btntan.configure(bg='powder blue')
def on_entersqrt(e):
    btnsqrt.configure(bg='red')
def on_leavesqrt(e):
    btnsqrt.configure(bg='powder blue')
def on_enterlog(e):
    btnlog.configure(bg='red')
def on_leavelog(e):
    btnlog.configure(bg='powder blue')
tex = StringVar()
operator = ''

# For Entry
entry1 = Entry(screen, bg='orange', font=('arial', 20, 'italic bold'), bd='30', justify='right', textvariable=tex)
entry1.grid(row=0, columnspan=4)
# For First Row
btn7 = Button(screen, bg='powder blue', text='7', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click(7), activebackground='yellow', activeforeground='red')
btn7.grid(row=1, column=0)
btn7.bind('<Enter>', on_enter7)
btn7.bind('<Leave>', on_leave7)

btn8 = Button(screen, bg='powder blue', text='8', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click(8), activebackground='yellow', activeforeground='red')
btn8.grid(row=1, column=1)
btn8.bind('<Enter>', on_enter8)
btn8.bind('<Leave>', on_leave8)

btn9 = Button(screen, bg='powder blue', text='9', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click(9), activebackground='yellow', activeforeground='red')
btn9.grid(row=1, column=2)
btn9.bind('<Enter>', on_enter9)
btn9.bind('<Leave>', on_leave9)

btnadd = Button(screen, bg='powder blue', text='+', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click('+'), activebackground='yellow', activeforeground='red')
btnadd.grid(row=1, column=3)
btnadd.bind('<Enter>', on_enteradd)
btnadd.bind('<Leave>', on_leaveadd)
# For Second Row
btn4 = Button(screen, bg='powder blue', text='4', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click(4), activebackground='yellow', activeforeground='red')
btn4.grid(row=2, column=0)
btn4.bind('<Enter>', on_enter4)
btn4.bind('<Leave>', on_leave4)

btn5 = Button(screen, bg='powder blue', text='5', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click(5), activebackground='yellow', activeforeground='red')
btn5.grid(row=2, column=1)
btn5.bind('<Enter>', on_enter5)
btn5.bind('<Leave>', on_leave5)

btn6 = Button(screen, bg='powder blue', text='6', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click(6), activebackground='yellow', activeforeground='red')
btn6.grid(row=2, column=2)
btn6.bind('<Enter>', on_enter6)
btn6.bind('<Leave>', on_leave6)

btnminus = Button(screen, bg='powder blue', text='-', font=('arial', 15, 'italic bold'), bd=15, padx=18, pady=16, command=lambda: click('-'), activebackground='yellow', activeforeground='red')
btnminus.grid(row=2, column=3)
btnminus.bind('<Enter>', on_enterminus)
btnminus.bind('<Leave>', on_leaveminus)

# For Third Row
btn1 = Button(screen, bg='powder blue', text='1', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click(1), activebackground='yellow', activeforeground='red')
btn1.grid(row=3, column=0)
btn1.bind('<Enter>', on_enter1)
btn1.bind('<Leave>', on_leave1)
btn2 = Button(screen, bg='powder blue', text='2', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click(2), activebackground='yellow', activeforeground='red')
btn2.grid(row=3, column=1)
btn2.bind('<Enter>', on_enter2)
btn2.bind('<Leave>', on_leave2)
btn3 = Button(screen, bg='powder blue', text='3', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=16, command=lambda: click(3), activebackground='yellow', activeforeground='red')
btn3.grid(row=3, column=2)
btn3.bind('<Enter>', on_enter3)
btn3.bind('<Leave>', on_leave3)

btndiv = Button(screen, bg='powder blue', text='/', font=('arial', 15, 'italic bold'), bd=15, padx=18, pady=16, command=lambda: click('/'), activebackground='yellow', activeforeground='red')
btndiv.grid(row=3, column=3)
btndiv.bind('<Enter>', on_enterdiv)
btndiv.bind('<Leave>', on_leavediv)

# For Fourth Row
btnclear = Button(screen, text='C', bg='orange', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=14, command=clear, activebackground='yellow', activeforeground='red')
btnclear.grid(row=4, column=0)
btnclear.bind('<Enter>', on_enterC)
btnclear.bind('<Leave>', on_leaveC)

btn0 = Button(screen, bg='powder blue', text='0', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=14, command=lambda: click('0'), activebackground='yellow', activeforeground='red')
btn0.grid(row=4, column=1)
btn0.bind('<Enter>', on_enter0)
btn0.bind('<Leave>', on_leave0)

btnequal = Button(screen, bg='powder blue', text='=', font=('arial', 15, 'italic bold'), bd=15, padx=16, pady=14, command=equal, activebackground='yellow', activeforeground='red')
btnequal.grid(row=4, column=2)
btnequal.bind('<Enter>', on_enterequal)
btnequal.bind('<Leave>', on_leaveequal)

btnmul = Button(screen, bg='powder blue', text='*', font=('arial', 15, 'italic bold'), bd=15, padx=18, pady=14, command=lambda: click('*'), activebackground='yellow', activeforeground='red')
btnmul.grid(row=4, column=3)
btnmul.bind('<Enter>', on_entermul)
btnmul.bind('<Leave>', on_leavemul)

btnsin = Button(screen, bg='powder blue', text='Sin', font=('arial', 15, 'italic bold'), bd=15, padx=12, pady=16, command=cmsin, activebackground='yellow', activeforeground='red')
btnsin.grid(row=0, column=4)
btnsin.bind('<Enter>', on_entersin)
btnsin.bind('<Leave>', on_leavesin)

btncos = Button(screen, bg='powder blue', text='Cos', font=('arial', 15, 'italic bold'), bd=15, padx=10, pady=16, command=cmcos, activebackground='yellow', activeforeground='red')
btncos.grid(row=1, column=4)
btncos.bind('<Enter>', on_entercos)
btncos.bind('<Leave>', on_leavecos)

btntan = Button(screen, bg='powder blue', text='Tan', font=('arial', 15, 'italic bold'), bd=15, padx=10, pady=16, command=cmtan, activebackground='yellow', activeforeground='red')
btntan.grid(row=2, column=4)
btntan.bind('<Enter>', on_entertan)
btntan.bind('<Leave>', on_leavetan)

btnsqrt = Button(screen, bg='powder blue', text='sqrt', font=('arial', 15, 'italic bold'), bd=15, padx=9, pady=16, command=cmsqrt, activebackground='yellow', activeforeground='red')
btnsqrt.grid(row=3, column=4)
btnsqrt.bind('<Enter>', on_entersqrt)
btnsqrt.bind('<Leave>', on_leavesqrt)


btnlog = Button(screen, bg='powder blue', text='log', font=('arial', 15, 'italic bold'), bd=15, padx=10, pady=16, command=cmlog, activebackground='yellow', activeforeground='red')
btnlog.grid(row=4, column=4)
btnlog.bind('<Enter>', on_enterlog)
btnlog.bind('<Leave>', on_leavelog)



# mainloop
screen.mainloop()
