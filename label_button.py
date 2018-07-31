from tkinter import *

window = Tk()

window.geometry('500x500')
window.title('TKinter Window')

button = Button(text='Submit')
label = Label(text='Welcome to my TKinter window')

button.place(relx=0.5, rely=0.5, anchor=CENTER)
label.pack()

window.mainloop()