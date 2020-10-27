from LR3.lab_python_fp import print_result, unique, gen_random, field, cm_timer
import json


path = "/Users/dlnwlkmn/Desktop/dia-labs/LR3/data_light.json"

with open(path) as f, cm_timer.cm_timer_1():
    data = json.load(f)


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
    return list(i + f", зарплата \033[34m{gen_random.gen_random(1,100000,200000)[0]}\033[0m руб." for i in arg)


def main():

    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))


if __name__ == '__main__':
    main()
