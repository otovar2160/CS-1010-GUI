import tkinter 

bob= tkinter.Tk()
bob.geometry('200x200')
bob.title("CS1010 - GUI")


def doBut1():
    label_1.configure(text = "7")
    
def doBut2():
    label_1.configure(text = "4")

def doBut3():
    label_1.configure(text = "1")

def doBut4():
    label_1.configure(text = ".")

def doBut5():
    label_1.configure(text = "+/-")
    
def doBut6():
    label_1.configure(text = "8")
    
def doBut7():
    label_1.configure(text = "5")
    
def doBut8():
    label_1.configure(text = "2")

def doBut9():
    label_1.configure(text = "0")

def doBut10():
    label_1.configure(text = "CLEAR")

def doBut11():
    label_1.configure(text = "9")

def doBut12():
    label_1.configure(text = "6")

def doBut13():
    label_1.configure(text = "3")

def doBut14():
    label_1.configure(text = "AC")

def doBut15():
    label_1.configure(text = "/")
    
def doBut16():
    label_1.configure(text = "*")

def doBut17():
    label_1.configure(text = "-")

def doBut18():
    label_1.configure(text = "+")

def doBut19():
    label_1.configure(text = "=")

#Bar at the top.
label_1 = tkinter.Label(bob,text="empty")
label_1.grid(row=0,column=0)

but1 = tkinter.Button(bob,text="7",command=doBut1,width=5, height= 2)
but1.grid(row=1, column=0)

but2 = tkinter.Button(bob,text="4",command=doBut2, width=5, height= 2)
but2.grid(row=2, column=0)

but3 = tkinter.Button(bob,text="1",command=doBut3, width=5, height= 2)
but3.grid(row=3, column=0)

but4 = tkinter.Button(bob,text=".",command=doBut4,width=5, height= 2)
but4.grid(row=4, column=0)

but5 = tkinter.Button(bob,text="+/-",command=doBut5,width=5, height= 2)
but5.grid(row=5, column=0)

but6 = tkinter.Button(bob,text="8",command=doBut6,width=5, height= 2)
but6.grid(row=1, column=1)

but7 = tkinter.Button(bob,text="5",command=doBut7,width=5, height= 2)
but7.grid(row=2, column=1)

but8 = tkinter.Button(bob,text="2",command=doBut8,width=5, height= 2)
but8.grid(row=3, column=1)

but9 = tkinter.Button(bob,text="0",command=doBut9,width=5, height= 2)
but9.grid(row=4, column=1)

but10= tkinter.Button(bob,text="C",command=doBut10,width=5, height= 2)
but10.grid(row=5, column=1)

but11= tkinter.Button(bob,text="9",command=doBut11,width=5, height= 2)
but11.grid(row=1, column=2)

but12= tkinter.Button(bob,text="6",command=doBut12,width=5, height= 2)
but12.grid(row=2, column=2)

but13= tkinter.Button(bob,text="3",command=doBut13,width=5, height= 2)
but13.grid(row=3, column=2)

but14 = tkinter.Button(bob,text="AC",command=doBut14,width=5, height= 2)
but14.grid(column=2,row=5)

but15 = tkinter.Button(bob,text="/",command=doBut15,width=5, height= 2)
but15.grid(row=1, column=3)

but16 = tkinter.Button(bob,text="*",command=doBut16,width=5, height= 2)
but16.grid(row=2, column=3)

but17 = tkinter.Button(bob,text="-",command=doBut17,width=5, height= 2)
but17.grid(row=3, column=3)

but18 = tkinter.Button(bob,text="+",command=doBut18,width=5, height= 2)
but18.grid(row=4, column=3)

but19= tkinter.Button(bob,text="=",command=doBut19,width=5, height= 2)
but19.grid(row=5, column=3)


bob.mainloop()
