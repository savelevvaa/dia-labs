import time

class ComputerState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        success = False
        if state.name in self.allowed:
            print('\033[33mТекущее стостояние:\033[0m', self, ' => \033[32mизменено на \033[35m', state.name, "\033[0m")
            self.__class__ = state
            success = True
        else:
            print('\033[33mТекущее стостояние:\033[0m', self, ' => \033[31m переключение на \033[35m', state.name, '\033[31mневозможно.\033[0m')
        return success

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = "off"
    allowed = ['on']


class On(ComputerState):
    """ State of being powered on and working """
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    """ State of being in suspended mode after switched on """
    name = "suspend"
    allowed = ['on']


class Hibernate(ComputerState):
    """ State of being in hibernation after powered on """
    name = "hibernate"
    allowed = ['on']


class Computer(object):
    """ A class representing a computer """

    def __init__(self, model='Dell'):
        self.model = model
        # State of the computer - default is off.
        self.state = Off()

    def change(self, state):
        """ Change state """
        prevState = self.state.name
        success = self.state.switch(state)
        if prevState != "off" and success == True:
            tok = time.perf_counter()
            self.t = f"{tok - self.tic:0.4f}"
            print(f"Прошедшее время в состоянии \033[35m{prevState}\033[0m: {self.t} sec\n")
        if success == True:
            self.tic = time.perf_counter()


if __name__ == "__main__":
    print("\033[36mПАТТЕРН 'СОСТОЯНИЕ'\033[0m")
    comp = Computer()
    comp.change(On)
    time.sleep(3)
    comp.change(Off)
    comp.change(On)
    time.sleep(0.5)
    comp.change(Suspend)
    time.sleep(2)
    comp.change(Hibernate)
    comp.change(On)
    time.sleep(1)
    comp.change(Hibernate)
    time.sleep(4)
    comp.change(On)
    time.sleep(1)
    comp.change(Off)