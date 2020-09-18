from LR2.lab_python_oop.rectangle import Rectangle
from LR2.lab_python_oop.figureColor import FigureColor


# Класс описывающий сущность "Квадрат"
class Squad(Rectangle):

    fig = "Квадрат"

    # Конструктор класса
    def __init__(self, side_length, color):
        self.side = side_length
        self.figureColor = FigureColor()
        self.figureColor.set(color)

    # Переопределение метода нахождения площади
    def square(self):
        return self.side * self.side

    # Метода печати информации об объекте класса на консоль
    def about(self):
        print("Фигура: \033[31m{}\033[0m, Сторона: {}, Площадь: {}, Цвет: {}".format(self.fig, self.side, self.square(), self.figureColor.get()))
