import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

def button_event():
    res = "Welcome to " + tktxt.get()
    tklabel.configure(text=res)
    messagebox.showinfo('This button','was Clicked')

window = tk.Tk()

window.geometry('1080x720')

window.title("Bem vindo! Tkinter first app")

tklabel = tk.Label(window, text="This is a Label", font=("Arial Bold", 16))

tklabel.grid(column=0, row=0)

tktxt = tk.Entry(window, width=10)
tktxt.grid(column=0, row=1)

ttkcombo = ttk.Combobox(window)
ttkcombo['values']= ("Item 1", "Item 2", 43, 4.42, 1e3, ["List"])
ttkcombo.current(1) #set the selected item

ttkcombo.grid(column=0, row=2)

ttkchk = ttk.Checkbutton(window, text='Choose')
ttkchk.grid(column=0, row=3)


ttkrad1 = ttk.Radiobutton(window,text='First', value=1)
ttkrad2 = ttk.Radiobutton(window,text='Second', value=2)
ttkrad3 = ttk.Radiobutton(window,text='Third', value=3)

ttkrad1.grid(column=0, row=4)
ttkrad2.grid(column=1, row=4)
ttkrad3.grid(column=2, row=4)



tkbtn = tk.Button(window, text="This is a Button",
                  bg="orange", fg="red", command=button_event)

tkbtn.grid(column=0, row=5)

window.mainloop()
