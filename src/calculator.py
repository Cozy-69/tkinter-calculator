
# Made by @mouaid69 on Twitter

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("330x170")
root.title("Calculator")
root.iconbitmap("../img/icon.ico")
root.resizable(0,0)



entryframe = ttk.Frame(root,height = 100,width = 357)
entryframe.grid()
numbresframe = ttk.Frame(root,height = 372,width = 357)
numbresframe.grid()

def clear():
	mainentry.delete(0,"end")


mainentry = ttk.Entry(entryframe,font=('arial', 16, 'bold'),width=1)
mainentry.grid(column=0,row=1,padx=(12,0),pady=(3,20),ipadx=100)
clearbtn = ttk.Button(entryframe,text="C",command=clear)
clearbtn.grid(column=1,row=1,padx=(0,0),pady=(3,20),ipady=3.4)

def calculate():
	calc_value = mainentry.get()
	mainentry.delete(0,"end")
	mainentry.insert(0,eval(calc_value))

calculbtn = ttk.Button(numbresframe,text="=",command=calculate, cursor = "hand2")
calculbtn.grid(column=3,row=5)





def numbers_value(n):
	entry_value = mainentry.get()
	new = str(entry_value)+str(n)
	mainentry.delete(0, 'end')
	mainentry.insert(0,new)





btn1 = ttk.Button(numbresframe,text="1",command=lambda: numbers_value(1))
btn1.grid(column=1,row=2)
btn2 = ttk.Button(numbresframe,text="2",command=lambda: numbers_value(2))
btn2.grid(column=2,row=2)
btn3 = ttk.Button(numbresframe,text="3",command=lambda: numbers_value(3))
btn3.grid(column=3,row=2)
btnpls = ttk.Button(numbresframe,text="+",command=lambda: numbers_value("+"))
btnpls.grid(column=4,row=2)


btn4 = ttk.Button(numbresframe,text="4",command=lambda: numbers_value(4))
btn4.grid(column=1,row=3)
btn5 = ttk.Button(numbresframe,text="5",command=lambda: numbers_value(5))
btn5.grid(column=2,row=3)
btn6 = ttk.Button(numbresframe,text="6",command=lambda: numbers_value(6))
btn6.grid(column=3,row=3)
btnmin = ttk.Button(numbresframe,text="-",command=lambda: numbers_value("-"))
btnmin.grid(column=4,row=3)



btn7 = ttk.Button(numbresframe,text="7",command=lambda: numbers_value(7))
btn7.grid(column=1,row=4)
btn8 = ttk.Button(numbresframe,text="8",command=lambda: numbers_value(8))
btn8.grid(column=2,row=4)
btn9 = ttk.Button(numbresframe,text="9",command=lambda: numbers_value(9))
btn9.grid(column=3,row=4)
btnmul = ttk.Button(numbresframe,text="*",command=lambda: numbers_value("*"))
btnmul.grid(column=4,row=4)





btn0 = ttk.Button(numbresframe,text="0",command=lambda: numbers_value(0))
btn0.grid(column=1,row=5)
btndiv = ttk.Button(numbresframe,text="/",command=lambda: numbers_value("/"))
btndiv.grid(column=2,row=5)
btnfl = ttk.Button(numbresframe,text=".",command=lambda: numbers_value("."))
btnfl.grid(column=4,row=5)







root.mainloop()