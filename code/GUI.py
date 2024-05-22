#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
import sqlite3
import File

database_path = __file__.replace('code/GUI.py', 'dataset/text_datas.db')
conn = sqlite3.connect(database_path)

text2s = []
label2s = []
text3s = []
label3s = []
text4s = []
label4s = []

def search():
    word = text_1.get()
    results = File.search_word(conn, word, ['K1'])
    
    global text2s, label2s, text3s, label3s, text4s, label4s
    text2s = []
    label2s = []
    text3s = []
    label3s = []
    text4s = []
    label4s = []
    
    for i in range(len(results)):
        text2s.append(StringVar())
        label2s.append(ttk.Label(root, textvariable=text2s[i], font=('Times New Roman',20), foreground = '#1155ee', padding = (10,10)))
        text3s.append(StringVar())
        label3s.append(ttk.Label(root, textvariable=text3s[i], font=('Times New Roman',20), padding = (10,10)))
        text4s.append(StringVar())
        label4s.append(ttk.Label(root, textvariable=text4s[i], font=('Times New Roman',20), padding = (10,10)))
        
        text2s[i].set(word)
        text3s[i].set(results[i][0])
        text4s[i].set(results[i][1])
        
    for i in range(len(label3s)):
        label2s[i].grid(row=i+1, column=1)
        label3s[i].grid(row=i+1, column=0)
        label4s[i].grid(row=i+1, column=2)

root = Tk()
root.title("Search window")

#root.geometry("640x480")

label_1 = ttk.Label(root, text="search word: ", font = ('Times New Roman',20), padding = (10,10))
text_1 = StringVar()
entry_1 = ttk.Entry(root,textvariable=text_1, font = ('Times New Roman',20))

button_1 = ttk.Button(root,text = 'OK', command=lambda:search())

label_1.grid(row=0,column=0)
entry_1.grid(row=0,column=1)
button_1.grid(row=0,column=2)
    
root.mainloop()