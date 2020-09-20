from LR2.lab_python_oop.geomFigure import GeomFigure
from LR2.lab_python_oop.figureColor import FigureColor
import math


#Класс описывающий сущность "Круг"
class Circle(GeomFigure):

    fig = "Круг"

    # Конструктор класса
    def __init__(self, radius, color):
        self.r = radius
        self.figureColor = FigureColor()
        self.figureColor.set(color)

    # Переопределение метода нахождения площади
    def square(self):
        return math.pi*pow(self.r, 2)

    # Метода печати информации об объекте класса на консоль
    def about(self):
        print("Фигура: \033[31m{}\033[0m, Радиус: {}, Площадь: {}, Цвет: {}".format(self.fig, self.r, self.square(), self.figureColor.get()))

    def __repr__(self):
        return "Фигура: \033[31m{}\033[0m, Радиус: {}, Площадь: {}, Цвет: {}".format(
            self.fig,
            self.r,
            self.square(),
            self.figureColor.get())
