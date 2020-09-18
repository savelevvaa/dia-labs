import requests
from LR2.lab_python_oop.rectangle import Rectangle
from LR2.lab_python_oop.squad import Squad
from LR2.lab_python_oop.circle import Circle

# Функция для демонстрации методов всех созданных классов
def main():
    print(requests.__license__ + "\n")

    rect = Rectangle(10,15, "Blue")
    sqd = Squad(10,"Black")
    circ = Circle(5, "Red")

    rect.about()
    sqd.about()
    circ.about()


if __name__ == "__main__":
    main()