print("\033[34mРешаем биквадратные уравнения \033[0m")

stop = 0

while stop == 0:
    a = float(input("Введите первый аргумент: "))
    b = float(input("Введите второй аргумент: "))
    c = float(input("Введите третий аргумент: "))

    if (a, b, c) == (0, 0, 0):
        print("Введите ненулевые аргументы")
        continue
    if (a, b) == (0, 0):
        print("Корней нет")
        stop = 1
    if (a, c) == 0 and (b, c) == 0:
        print("x = 0")
        stop = 1
    if a == 0:
        if c < 0:
            root = pow(-c/b, 0.5)
            print(f"Корни: x1 = {root}, x2 = {-root}")
            stop = 1
        elif c == 0:
            print("x = 0")
            stop = 1
        else:
            print("Корнец нет!")
            stop = 1
    if b == 0:
        if c < 0:
            root = pow(pow(-c/b, 0.5), 0.5)
            print(f"Корни: x1 = {root}, x2 = {-root}")
            stop = 1
        elif c == 0:
            print("x = 0")
            stop = 1
        else:
            print("Корней нет!")
            stop = 1
    if c == 0:
        print("Попробуйте другие коэфициенты...")

    D = pow(b, 2) - (4 * a * c)

    if D > 0:
# Производим замену t = x^2
        t1 = (-b + pow(D, 0.5)) / 2*a
        t2 = (-b - pow(D, 0.5)) / 2*a
        if t1 < 0 and t2 < 0:
            print("Корней нет")
            stop = 1
        elif t1 < 0 and t2 > 0:
            root = pow(t2, 0.5)
            print(f"Корни: x1 = {root}, x2 = {-root}")
            stop = 1
        elif t1 > 0 and t2 < 0:
            root = pow(t1, 0.5)
            print(f"Корни: x1 = {root}, x2 = {-root}")
            stop = 1
        else:
            root1 = pow(t1, 0.5)
            root2 = pow(t2, 0.5)
            print(f"Корни: x1 = {root1}, x2 = {-root1}")
            print(f"Корни: x3 = {root2}, x4 = {-root2}")
            stop = 1

    elif D == 0:
        t = -b / (2*a)
        if t < 0:
            print("Корней нет!")
            stop = 1
        else:
            root = pow(t, 0.5)
            print(f"Корни: x1 = {root}, x4 = {-root}")
            stop = 1
    else:
        print("\033[31mДействительных корней нет!\033[0m")






