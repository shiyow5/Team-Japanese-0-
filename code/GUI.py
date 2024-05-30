#!/usr/bin/env python3

import tkinter as tk
import File
import NLP

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.display_num = 10
        
        master.geometry("1140x600")
        master.title("Authorchip Analysis")
        
        self.label_1 = tk.Label(master, text="search word: ", font = ('Times New Roman',20))
        self.label_1.place(x=20, y=30)
        
        self.word = tk.StringVar()
        self.search = tk.Entry(master, textvariable=self.word, font = ('Times New Roman',20), width = 33)
        self.search.place(x=200, y=30)
        
        self.botton_1 = tk.Button(master, text = 'OK', width = 10)
        self.botton_1.place(x=680, y=32)
        
        self.results_c = [tk.Label(master, font=('Times New Roman',20), foreground = '#1155ee', width=10, anchor="center") for i in range(self.display_num)] # relief=tk.SOLID
        for i, result_c in enumerate(self.results_c):
            result_c.place(x=500, y=100+i*40, anchor="center")
            
        self.results_l = [tk.Label(master, font=('Times New Roman',20), width=30, anchor="e") for i in range(self.display_num)]
        for i, result_l in enumerate(self.results_l):
            result_l.place(x=400, y=100+i*40, anchor="e")
            
        self.results_r = [tk.Label(master, font=('Times New Roman',20), width=30, anchor="w") for i in range(self.display_num)]
        for i, result_r in enumerate(self.results_r):
            result_r.place(x=600, y=100+i*40, anchor="w")
        
        
        self.pack(anchor="center")
        
        
    def set_LR_sentences(self, LR_sentences:list=None):
        self.LR_sentences = LR_sentences[:10]
        
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
    app = Application(master = win)
    
    # Controller
    def search():
        global LR_sentences, cursol
        cursol = 0
        LR_sentences = NLP.search_word(app.word.get(), ['K1'])
        app.clear()
        app.set_LR_sentences(LR_sentences[cursol:cursol+10])
        app.set_result()
        cursol += 10
        return
    
    def next_result():#nextボタン実装する
        app.clear()
        app.set_LR_sentences(LR_sentences[cursol:cursol+10])
        app.set_result()
        cursol += 10
        return
        
    
    app.botton_1["command"] = search
    
    app.mainloop()
    
if __name__ == "__main__":
    main()