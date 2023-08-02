#GUI
from tkinter import *

def dell():
    text=Label(window,text="peppo to you, you fellow passenger", fg="black", bg="Lightgrey", font=("helvetica",10))
    text.grid(row=1, column=0)

def get_input():
    input_value=entry.get()
    print(input_value)

window=Tk()
button=Button(text="peppo",command=get_input, bg="Lightgrey")
button.pack()
entry=Entry(window)
entry.pack()



window.title("Gesù")
window.geometry("500x300")
window.configure(bg='lightgrey')
button.grid(row=0, column=0)
mainloop()

