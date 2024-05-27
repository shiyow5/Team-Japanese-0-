import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.master.geometry("1140x600")
        self.master.title("Authorchip Analysis")
        self.widget()
        
    def widget(self):
        self.label_1 = tk.Label(self.master, text="search word: ", font = ('Times New Roman',20))
        self.label_1.place(x=20, y=30)
        
        self.entry_1 = tk.Entry(self.master, font = ('Times New Roman',20), width = 33)
        self.entry_1.place(x=200, y=30)
        
        self.botton_1 = tk.Button(self.master, text = 'OK', command=lambda:self.search(), width = 10)
        self.botton_1.place(x=680, y=32)
        
    def search(self):
        return
    
def main():
    win = tk.Tk()
    app = Application(master = win)
    app.mainloop()
    
if __name__ == "__main__":
    main()