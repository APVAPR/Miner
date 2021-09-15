import tkinter as tk


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
                btn = tk.Button(MineSweeper.window, width=3, font='Calibry 15 bold')
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

    def start(self):
        """
        Метод запуска основного цикла игры
        """
        MineSweeper.window.mainloop()


game = MineSweeper()
game.create_wigets()
game.start()
for row_btn in game.buttons:
    print(row_btn)
