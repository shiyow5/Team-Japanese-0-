from tkinter import *
from tkinter import ttk

def get_id_pass():
    id = text_1.get()
    text_2.set(id)

root = Tk()
root.title("Search window")

root.geometry("640x480")

label_1 = ttk.Label(root, text="search word: ", font = ('Times New Roman',20), padding = (10,10))
text_1 = StringVar()
entry_1 = ttk.Entry(root,textvariable=text_1, font = ('Times New Roman',20))

text_2 = StringVar()
label_2 = ttk.Label(root, textvariable=text_2, font=('Times New Roman',20), foreground = '#1155ee', padding = (10,10))

button_1 = ttk.Button(root,text = 'OK', command=lambda:get_id_pass())

label_1.grid(row=0,column=0)
entry_1.grid(row=0,column=1)
button_1.grid(row=0,column=2)
label_2.grid(row=1,column=1)

root.mainloop()