import tkinter as tk
from random import shuffle


class MyButton(tk.Button):

    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Clibry 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.is_mine = False
        self.number = number

    def __repr__(self):
        return f'{self.is_mine} [{self.x}] [{self.y}] {self.number} '


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
    MINES = 15

    def __init__(self):
        """
        Создает объекты кнопок и сохраняет в списке buttons
        """
        count = 1
        self.buttons = []
        for i in range(MineSweeper.ROW):
            temp = []
            for j in range(MineSweeper.COLUMNS):
<<<<<<< HEAD
                btn = MyButton(MineSweeper.window, x=i, y=j, number=count)
                btn.config(command=lambda button=btn: self.click(button))
=======
                btn = MyButton(MineSweeper.window, width=3, font='Clibry 15 bold')
>>>>>>> 3092c02fa4df5cf22b8ac3f4efda18eeb404a5b0
                temp.append(btn)
                count += 1
            self.buttons.append(temp)

    def click(self, clicked_button: MyButton):
        print(clicked_button)
        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')

        else:
            clicked_button.config(text=clicked_button.number, disabledforeground='black')
        clicked_button.config(state='disabled')

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

<<<<<<< HEAD
    def insert_mines(self):
        index_mines = self.get_mines_places()
        for row_btn in self.buttons:
            for btn in row_btn:
                if btn.number in index_mines:
                    btn.is_mine = True

    @staticmethod
    def get_mines_places():
        """
        Метод получения рандомных индексов нахождения мин

        """
        indexes = list(range(1, MineSweeper.ROW * MineSweeper.COLUMNS + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]

=======
>>>>>>> 3092c02fa4df5cf22b8ac3f4efda18eeb404a5b0
    def start(self):
        """
        Метод запуска основного цикла игры
        """
        self.create_wigets()
<<<<<<< HEAD
        self.insert_mines()
        self.get_mines_places()
=======
>>>>>>> 3092c02fa4df5cf22b8ac3f4efda18eeb404a5b0
        self.print_buttons()
        game.window.mainloop()


game = MineSweeper()

game.start()
