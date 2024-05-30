#!/usr/bin/env python3

import tkinter as tk
import File
import NLP

class Main_Win(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(anchor="center")
        
        master.geometry("570x300")
        master.title("Authorchip Analysis")
        
        self.button_search = tk.Button(master, command=self.search_window, text="Search", width=10)
        self.button_search.pack()
        
    def search_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.subapp_1 = Search_Win(self.newWindow)
        self.subapp_1.botton_1["command"] = self.subapp_1_functions[0]
        self.subapp_1.botton_2["command"] = self.subapp_1_functions[1]
        
    def set_winController(self, winName:str, functions:list):
        if (winName == 'search_window'):
            self.subapp_1_functions = functions

class Search_Win(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(anchor="center")
        
        self.result_num = 10
        
        master.geometry("1140x600")
        master.title("Search Window")
        
        self.label_1 = tk.Label(master, text="search word: ", font = ('Times New Roman',20))
        self.label_1.place(x=20, y=30)
        
        self.word = tk.StringVar()
        self.search = tk.Entry(master, textvariable=self.word, font = ('Times New Roman',20), width = 33)
        self.search.place(x=200, y=30)
        
        self.botton_1 = tk.Button(master, text = 'OK', width = 10)
        self.botton_1.place(x=680, y=32)
        
        self.results_c = [tk.Label(master, font=('Times New Roman',20), foreground = '#1155ee', width=10, anchor="center") for i in range(self.result_num)] # relief=tk.SOLID
        for i, result_c in enumerate(self.results_c):
            result_c.place(x=550, y=100+i*40, anchor="center")
            
        self.results_l = [tk.Label(master, font=('Times New Roman',20), width=30, anchor="e") for i in range(self.result_num)]
        for i, result_l in enumerate(self.results_l):
            result_l.place(x=450, y=100+i*40, anchor="e")
            
        self.results_r = [tk.Label(master, font=('Times New Roman',20), width=30, anchor="w") for i in range(self.result_num)]
        for i, result_r in enumerate(self.results_r):
            result_r.place(x=650, y=100+i*40, anchor="w")
            
        self.botton_2 = tk.Button(master, text = 'Next', width = 10)
        self.botton_2.place(x=550, y=550, anchor="center")
        
        
    def set_LR_sentences(self, LR_sentences:list=None):
        self.LR_sentences = LR_sentences[:self.result_num]
        
        return
        
    def set_result(self):
        for i, LR_sentence in enumerate(self.LR_sentences):
            self.results_c[i]["text"] = self.word.get()
            self.results_l[i]["text"] = LR_sentence[0]
            self.results_r[i]["text"] = LR_sentence[1]
        
        return
        
    def clear(self):
        for results in [self.results_c, self.results_l, self.results_r]:
            for result in results:
                result["text"] = ""
                
        return

    
def main():
    # View
    win = tk.Tk()
    app = Main_Win(master = win)
    
    # Controller
    def search():
        global LR_sentences, cursol
        cursol = 0
        LR_sentences = NLP.search_word(app.subapp_1.word.get(), ['K1'])
        app.subapp_1.clear()
        app.subapp_1.set_LR_sentences(LR_sentences[cursol:cursol+app.subapp_1.result_num])
        app.subapp_1.set_result()
        cursol += app.subapp_1.result_num
        return
    
    def next_result():#nextボタン実装する
        global LR_sentences, cursol
        app.subapp_1.clear()
        app.subapp_1.set_LR_sentences(LR_sentences[cursol:cursol+app.subapp_1.result_num])
        app.subapp_1.set_result()
        cursol += app.subapp_1.result_num
        return
        
    app.set_winController(winName='search_window', functions=[search, next_result])
    
    app.mainloop()
    
if __name__ == "__main__":
    main()