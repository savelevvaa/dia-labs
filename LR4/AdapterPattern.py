# Паттерн "Адаптер"
class Strait:
    def __init__(self, number):
        self.straitNumber = int(number)

    def straitOutput(self):
        return self.straitNumber


class Bin:
    def __init__(self, number):
        self.binNumber = int(number)

    def binOutput(self):
        return self.binNumber


class BinPresenter(Strait, Bin):

    def getBinary(self, n):
        n = int(n)
        if (n == 0):
            return "0"
        elif (n == 1):
            return "1"
        else:
            return self.getBinary(int(n / 2)) + str(n % 2)

    def binOutput(self) -> str:
        return self.getBinary(self.straitNumber)


def clientCode2(target: "Bin"):
    """
    Клиентский код поддерживает все классы, использующие интерфейс Bin.
    """
    return target.binOutput()


if __name__ == "__main__":

    print("\033[36mПАТТЕРН 'АДАПТЕР'\033[0m")
    print("\033[33mКлиент: могу работать с бинарными числами:\033[0m")
    target = Bin(1010)
    print(f"Возврат клиентского кода: \033[32m{clientCode2(target)}\033[0m\n")

    adaptee = Strait(12345)
    print("\033[33mКлиент: класс Adaptee имеет не подходящий мне интерфейс\033[0m")
    print(f"Вывод класса Adaptee: \033[31m{adaptee.straitOutput()}\n\033[0m")

    print("\033[33mКлиент: но я могу работать с этим классом через адаптер:\033[0m")
    adapter = BinPresenter(12345)
    print(f"Неудобное значение: \033[31m{adapter.straitOutput()}\033[0m")
    print(f"Возврат клиентского кода с использованием Адаптера: \033[32m{clientCode2(adapter)}\033[0m")
