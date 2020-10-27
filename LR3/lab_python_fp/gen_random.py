import random

# функция рандомайзер
def gen_random(num_count, begin, end):
    result = []     # лист для результата
    if begin > end: temp = begin; begin = end; end = temp; # проверка границ интервала (корректирование)
    for i in range(0, num_count):
        result.append(random.randint(begin, end))
    return result

def main():
    print(gen_random(10, 0, 12))
    print(gen_random(15, 0, 1))
    print(gen_random(5, -5, 0))

if __name__ == "__main__":
    main()