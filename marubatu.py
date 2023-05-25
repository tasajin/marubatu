from tkinter import *
from tkinter import ttk
from tkinter import messagebox

squares = 3

class TictacApp(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.button_masu()
        self.value()

    def button_masu(self):
        for i in range(squares):
            for j in range(squares):
                button = ttk.Button(self, command=lambda i=i, j=j: self.record(i, j))
                button.bind('<Button-1>', self.mark)
                button.grid(column=i, row=j, sticky=(N, S, E, W))

        for i in range(squares):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.grid(column=0, row=0, sticky=(N, S, E, W))

    def mark(self, event):
        if not event.widget['text']:
            if self.player == 1:
                event.widget['text'] = '〇'
            else:
                event.widget['text'] = '×'
            self.turn()

    def value(self):
        self.player = 1
        self.field = []
        for t in range(squares): 
            self.field.append(['' for t in range(squares)])
        self.finish = 0

    def record(self, i, j):
        def x():
            if not self.field[i][j]:
                self.field[i][j] = self.player
                self.winner_check()
                self.turn()
                self.clear()
        return x

    def winner_check(self):
        naname = 0
        for i in range(squares):
            yoko = 0
            tate = 0
            for j in range(squares):
                if self.field[i][j] == self.player:
                    yoko += 1
                if self.field[j][i] == self.player:
                    tate += 1
            if self.field[i][i] == self.player:
                naname += 1
            if yoko == 3 or tate == 3 or naname == 3:
                self.result()
        if self.field[0][2] == self.field[1][1] == self.field[2][0] == self.player:
            self.result()

    def turn(self):
        if self.finish == 0:
            self.player = -self.player

    def result(self):
        if self.player == 1:
            messagebox.showinfo('〇のプレイヤーの勝利！')
        else:
            messagebox.showinfo('×のプレイヤーの勝利！')
        self.finish = 1

    def clear(self):
        if self.finish == 1:
            self.button_masu()  
            self.value()


def main():
    root = Tk()
    root.title('目並べ、〇×ゲーム')
    TictacApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()