import random

# функция рандомайзер
def gen_random(num_count, begin, end):
    result = []     # лист для результата
    if begin > end: temp = begin; begin = end; end = temp; # проверка границ интервала (корректирование)
    for i in range(0, num_count):
        result.append(random.randint(begin, end))
    return result

print(gen_random(1, 0, 100))