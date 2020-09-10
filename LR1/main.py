import argparse
#import funcs
from LR1 import funcs # для запуска через терминал изменить на "import funcs"


print("\033[34mРешаем биквадратные уравнения \033[0m")

stop = 0

parser = argparse.ArgumentParser()
parser.add_argument("--a", help = "Коэффициент А Биквадратного уравнения", default=None, type=float)
parser.add_argument("--b", help = "Коэффициент B Биквадратного уравнения", default=None, type=float)
parser.add_argument("--c", help = "Коэффициент C Биквадратного уравнения", default=None, type=float)
args = parser.parse_args()
firstRunWithArgs = False

while stop == 0:

    argsValues = funcs.checkArgs(args.a, args.b, args.c, firstRunWithArgs)

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

    stop = funcs.checkCoefficients(a, b, c)

    if stop == 0:
        stop = funcs.discriminant(a, b, c)
    if stop == -1:
        stop = 0
    elif stop == 1:
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









