from LR2.lab_python_oop.geomFigure import GeomFigure
from LR2.lab_python_oop.figureColor import FigureColor

class rectangle(GeomFigure):

    fig = "Прямоугольник"

    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.figureColor = FigureColor()
        self.figureColor.set(color)

    def square(self):
        return self.h * self.w

    def about(self):
        print("Фигура: {}, Ширина: {}, Высота: {}, Цвет: {}".format(self.fig, self.w, self.h, self.figureColor.get()))

rect=rectangle(1,4,"green")
print(rect.square())
print(rect.about())