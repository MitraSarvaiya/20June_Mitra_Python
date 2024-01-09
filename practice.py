import tkinter
from tkinter import ttk

screen=tkinter.Tk()

screen.title("FirstApp")
screen.geometry('600x500')
screen.config(bg='red')

tkinter.Label(text='Firstname:',bg='white', font='calibri 10 bold').grid(row=0, column=0,sticky='W')
tkinter.Label(text='Lastname:',bg='white', font='calibri 10 bold').grid(row=2, column=0,sticky='W')

tkinter.Entry().grid(row=0,column=2,sticky='w')
tkinter.Entry().grid(row=2,column=2,stick='w')

tkinter.Radiobutton(text="Male",value=0,bg='white', font='calibri 10 bold').grid(row=4,column=0,sticky='W')
tkinter.Radiobutton(text="Female",value=1,bg='white', font='calibri 10 bold').grid(row=4,column=2,sticky='W')

tkinter.Checkbutton(text="Gujarati",bg='white', font='calibri 10 bold').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text="Hindi",bg='white', font='calibri 10 bold').grid(row=6,column=0,sticky='W')
tkinter.Checkbutton(text="English",bg='white', font='calibri 10 bold').grid(row=7,column=0,sticky='W')

city=["Gujarat","Rajasthan","MadhyaPradesh"]
ttk.Combobox(value=city).grid(row=9,column=0,sticky='W')

def button():
    print("Button Clicked")
tkinter.Button(text='Submit',bg='white', font='calibri 10 bold',command=button).place(x=300, y=250)
tkinter.mainloop()
