# функция проверки коэффициентов уровнения
def checkCoefficients(a, b, c):
    if (a, b, c) == (0, 0, 0):
        print("\033[33mВведите ненулевые аргументы\033[0m")
        return -1

    if (a, b) == (0, 0):
        print("\033[31mКорней нет!\033[0m")
        return 1
    if (a, c) == 0 and (b, c) == 0:
        print("\033[32mx = 0\033[0m")
        return 1
    if a == 0:
        if c < 0:
            root = pow(-c/b, 0.5)
            print(f"\033[32mКорни: x1 = {root}, x2 = {-root}\033[0m")
            return 1
        elif c == 0:
            print("\033[32mx = 0\033[0m")
            return 1
        else:
            print("\033[31mКорней нет!\033[0m")
            return 1
    if b == 0:
        if c < 0:
            root = pow(pow(-c/b, 0.5), 0.5)
            print(f"\033[32mКорни: x1 = {root}, x2 = {-root}\033[0m")
            return 1
        elif c == 0:
            print("\033[32mx = 0\033[0m")
            return 1
        else:
            print("\033[31mКорней нет!\033[0m")
            return 1
    if c == 0:
        print("\033[33mПопробуйте другие коэфициенты...\033[0m")
        return -1
    return 0
# функция вычисления дискриминанта
def discriminant(a, b, c):

    D = pow(b, 2) - (4 * a * c)

    if D > 0:
        # Производим замену t = x^2
        t1 = (-b + pow(D, 0.5)) / (2 * a)
        t2 = (-b - pow(D, 0.5)) / (2 * a)
        if t1 < 0 and t2 < 0:
            print("\033[31mКорней нет\033[0m")
            return 1
        elif t1 < 0 and t2 > 0:
            root = pow(t2, 0.5)
            print(f"\033[32mКорни: x1 = {root}, x2 = {-root}\033[0m")
            return 1
        elif t1 > 0 and t2 < 0:
            root = pow(t1, 0.5)
            print(f"\033[32mКорни: x1 = {root}, x2 = {-root}\033[0m")
            return 1
        else:
            root1 = pow(t1, 0.5)
            root2 = pow(t2, 0.5)
            print(f"\033[32mКорни: x1 = {root1}, x2 = {-root1}\033[0m")
            print(f"\033[32mКорни: x3 = {root2}, x4 = {-root2}\033[0m")
            return 1

    elif D == 0:
        t = -b / (2 * a)
        if t < 0:
            print("\033[31mКорней нет!\033[0m")
            return 1
        else:
            root = pow(t, 0.5)
            print(f"\033[32mКорни: x1 = {root}, x4 = {-root}\033[0m")
            return 1
    else:
        print("\033[31mДействительных корней нет!\033[0m")
        return 1

# функция проверки аргументов командной строки
def checkArgs(a, b, c, firstRunWithArgs):
    if a == None and b == None and c == None:
        firstRunWithArgs = True
    elif a == None and b == None:
        a = 0; b = 0;
    elif a == None and c == None:
        a = 0; c= 0;
    elif b == None and c == None:
        b = 0; c = 0;
    elif a == None:
        a = 0
    elif b == None:
        b = 0
    elif c == None:
        c = 0
    return (a, b, c, firstRunWithArgs)