import argparse
import funcs
#from LR1 import funcs # для запуска через терминал изменить на "import funcs"


print("\033[34mРешаем биквадратные уравнения \033[0m")

# Переменная для выхода из цикла
stop = 0

parser = argparse.ArgumentParser()
# Описываем аргументы командной строки (для -h)
parser.add_argument("--a", help = "Коэффициент А Биквадратного уравнения", default=None, type=float)
parser.add_argument("--b", help = "Коэффициент B Биквадратного уравнения", default=None, type=float)
parser.add_argument("--c", help = "Коэффициент C Биквадратного уравнения", default=None, type=float)
# Парсим аргументы
args = parser.parse_args()
# Логическая переменная первого прогона с аргументами
firstRunWithArgs = False

# Бесконечный цикл основной программы
while stop == 0:

    # Кортеж для проверенных введенных аргументов командной строки
    argsValues = funcs.checkArgs(args.a, args.b, args.c, firstRunWithArgs)

    # Ветвление получения коэфициентов уравнения (либо из cmd, либо при в воде)
    if argsValues[3] == False:
        a = argsValues[0]
        b = argsValues[1]
        c = argsValues[2]
        firstRunWithArgs = True
    else:
        a = float(input("\nВведите первый аргумент: "))
        b = float(input("Введите второй аргумент: "))
        c = float(input("Введите третий аргумент: "))

    print(f"\n\033[33mУравнение:\033[0m {a}X^4 + {b}X^2 + {c} = 0\n")

    # Проверка коэфициентов (возвращает -1, 0 или 1) и далее var stop обрабатывается в ветвлении
    stop = funcs.checkCoefficients(a, b, c)

    if stop == 0:
        # если вернулся 0, значит с коэфициентами все нормально, для дальнейшего нахождения корней с вычислением
        # дискриминанта
        stop = funcs.discriminant(a, b, c)
    if stop == -1:
        # вернулся -1, значит надо ввести аргументы заного
        stop = 0
    elif stop == 1:
        # предлагается завершить работу программы
        choice = ""
        while True:
            choice = input("\nХотите завершить? (y/n) ")
            if choice == "y":
                break
            elif choice == "n":
                stop = 0
                break
            else:
                print("\033[33mВведите правильный символ\033[0m \n")









