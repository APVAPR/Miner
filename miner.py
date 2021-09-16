import tkinter as tk


class MyButton(tk.Button):

    def __init__(self, master, x, y, *args, **kwargs):
        super(MyButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.is_mine = False

    def __repr__(self):
        return 'But'


class MineSweeper:
    window = tk.Tk()
    ROW = 10
    COLUMNS = 7

    def __init__(self):
        """
        Создает объекты кнопок и сохраняет в списке buttons
        """

        self.buttons = []
        for i in range(MineSweeper.ROW):
            temp = []
            for j in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.window, width=3, font='Clibry 15 bold')
                temp.append(btn)
            self.buttons.append(temp)

    def create_wigets(self):
        """
        Размещает кнопки в окне GUI
        """
        for i in range(MineSweeper.ROW):
            for j in range(MineSweeper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

    def start(self):
        """
        Метод запуска основного цикла игры
        """
        self.create_wigets()
        self.print_buttons()
        game.window.mainloop()


game = MineSweeper()

game.start()
