from LR2.lab_python_oop.geomFigure import GeomFigure
from LR2.lab_python_oop.figureColor import FigureColor

class Rectangle(GeomFigure):

    fig = "Прямоугольник"

    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.figureColor = FigureColor()
        self.figureColor.set(color)

    def square(self):
        return self.h * self.w

    def about(self):
        print("Фигура: \033[31m{}\033[0m, Ширина: {}, Высота: {}, Площадь: {}, Цвет: {}".format(self.fig, self.w, self.h, self.square(), self.figureColor.get()))
