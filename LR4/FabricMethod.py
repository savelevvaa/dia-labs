from abc import ABC, abstractmethod

# Паттерн "Фабрика"
class Manufacturer(ABC):

    @abstractmethod
    def toProduce(self):
        pass

    def output(self):
        product = self.toProduce()
        result = [f"Этот производитель производит: {product.info()[0]}", product.info()[1]]
        return result

class Product(ABC):

    @property
    @abstractmethod
    def movement(self):
        pass

    @property
    @abstractmethod
    def model(self):
        pass

    def info(self) -> []:
        return [f"{self.model}, it's {self.movement}", (self.model, self.movement)]


class AutoManufacturer(Manufacturer):

    def toProduce(self) -> Product:
        return Auto()

class Auto(Product):

    @property
    def movement(self) -> str:
        return "ездиет"

    @property
    def model(self) -> str:
        return "Inspire350"

class PlaneManufacturer(Manufacturer):

    def toProduce(self) -> Product:
        return Plane()

class Plane(Product):

    @property
    def movement(self) -> str:
        return "летает"

    @property
    def model(self) -> str:
        return "Dreamweawer770"

def clientCode1(m: Manufacturer):

    return m.output()


if __name__ == "__main__":
    print("\033[36mПАТТЕРН 'ФАБРИКА'\033[0m")
    print("\033[32mApp: Запущенно с AutoManufacturer.\033[0m")
    print("\033[33mКлиент: Я не щарю за класс Производителя, но это все еще работает...\033[0m")
    print(clientCode1(AutoManufacturer())[0])
    print()

    print("\033[32mApp: Запущенно с PlaneManufacturer.\033[0m")
    print("\033[33mКлиент: Я не щарю за класс Производителя, но это все еще работает...\033[0m")
    print(clientCode1(PlaneManufacturer())[0])