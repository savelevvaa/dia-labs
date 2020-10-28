from LR3.lab_python_fp import print_result, unique, gen_random, field, cm_timer
import json

# Путь к json файлу
path = "/Users/dlnwlkmn/Desktop/dia-labs/LR3/data_light.json"

# парсим файл, получется список словарей
with open(path) as f, cm_timer.cm_timer_1():
    data = json.load(f)


@print_result.print_result
def f1(arg):
    # return [unique.Unique(field.field(i, 'job-name'), ignore=False) for i in data]
    # return sorted(set(line["job-name"].lower() for line in arg))
    # Используем ранее разработанные функции, возващаем отсортированный набор названий вакансий
    return sorted(set(i for i in unique.Unique(field.field(data, 'job-name'), ignore=False)))


@print_result.print_result
def f2(arg):
    # отбираем только те названия, которые начинаются со слова "программист"
    return list(filter(lambda x: x.startswith("Программист"), arg))


@print_result.print_result
def f3(arg):
    # используя map дописываем "с опытом работы" к каждой вакансии
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result.print_result
def f4(arg):
    # дописываем ЗП к каждой вакансии
    return list(i + f", зарплата \033[34m{gen_random.gen_random(1,100000,200000)[0]}\033[0m руб." for i in arg)


def main():
    # вызываем функции с таймером
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))

# точка входа
if __name__ == '__main__':
    main()
