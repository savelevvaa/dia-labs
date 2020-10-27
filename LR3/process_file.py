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
def f1(arg):
    # return [unique.Unique(field.field(i, 'job-name'), ignore=False) for i in data]
    # return sorted(set(line["job-name"].lower() for line in arg))
    return sorted(set(i for i in unique.Unique(field.field(data, 'job-name'), ignore=False)))


@print_result.print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("программист"), arg))


@print_result.print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result.print_result
def f4(arg):
    return list(i + f", зарплата {gen_random.gen_random(1,100000,200000)[0]} руб." for i in arg)


if __name__ == '__main__':

    with open(path) as f, cm_timer.cm_timer_1():
        data = json.load(f)

    with cm_timer.cm_timer_1():
        temp1 = f1(data)
        temp2 = f2(temp1)
        temp3 = f3(temp2)
        temp4 = f4(temp3)
        print()
