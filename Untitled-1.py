from tkinter import *
window=Tk()
window.title("day 3 project")
window.geometry("700x700")
window.minsize(700,700)
window.maxsize(700,700)
i=PhotoImage(file="off.png")
i2=PhotoImage(file="on.png")
li=Label(image=i)

def on ():
    window.config(bg="yellow")
    li.config(image=i2,bg="yellow")
    li.pack()
    b.config(text="Bulb off",command=off)
    b.pack()
def off ():
    window.config(bg="black")
    li.config(image=i,bg="black")
    li.pack()
    b.config(text="Bulb on",command=on)
    b.pack()

b=Button(text="Bulb On",command=on)
b.pack()


window.mainloop()