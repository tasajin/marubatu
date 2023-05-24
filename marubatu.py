from tkinter import *
from tkinter import ttk


squaers = 3

class TictacApp(ttk,Frame):
    def __init__(self, master=None):
        super()._init__(master)
        self.button_masu()


    def button_masu(self):
        for i in range(squares):
            for j in range(squaers):
                button = ttk.Button(self,command=self.record(i,j))
                button.bind('<Button-1>', self.mark)
                button.grid(column=i, row=j, sticky=(N, S, E, W))

            for i in range(squaers):
                self.columnconfigure(i, weight=1)
                self.rowconfigure(i,weight=1)

            self.master.columnconfigure(0, weight=1)
            self.master.rowconfigure(0,weight=1)

            self.grid(column=0, row=0, sticky(N, S, E, W))






#ウィンドウを表示し続ける？
def main():
    root = Tk()
    root.title('目並べ、〇×ゲーム')
    TictapApp(root)
    root.mainloop()

if __name__ == ' __main__ ':
    main()

        
