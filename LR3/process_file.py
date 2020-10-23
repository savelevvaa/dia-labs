from LR3.lab_python_fp import print_result, sort, unique, gen_random, field, cm_timer
import json
import sys
# Сделаем другие необходимые импорты


path = "/Users/dlnwlkmn/Desktop/dia-labs/LR3/data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result.print_result
def f1():
    #return [unique.Unique(field.field(i, 'job-name'), ignore=False) for i in data]
    return [unique.Unique(i, ignore=False) for i in field.field(data, 'job-name')]


@print_result.print_result
def f2():
    raise NotImplemented


@print_result.print_result
def f3():
    raise NotImplemented


@print_result.print_result
def f4():
    raise NotImplemented


if __name__ == '__main__':

    with open(path) as f:
        data = json.load(f)

    with cm_timer.cm_timer_1():
        temp1 = f1()
        for i in temp1[1]:
            print(i)
