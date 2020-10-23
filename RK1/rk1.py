from operator import itemgetter

""" Савельев Алескей, группа ИУ5-54Б, Вариант Г-17 """

tasks = [
    "Список оркестров на букву 'А' и их дирижеров",                         # Г1
    "Список оркестров с max ЗП дирижоров, Сортировка по ЗП",                # Г2
    "Список всех связанных дирижеров и оркестров, Сортировка по оркестрам"  # Г3
]

class Сonductor:
    """Дирижер"""

    def __init__(self, id, fio, sal, orc_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.dep_id = orc_id


class Orcestra:
    """Оркестр"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class CondOrc:
    """
    'Дирижер оркестра' для реализации
    связи многие-ко-многим
    """

    def __init__(self, orc_id, cond_id):
        self.orc_id = orc_id
        self.cond_id = cond_id

# Оркестры
orcestras = [
    Orcestra(1, 'Симфонические оркестр'),
    Orcestra(2, 'Духовой оркестр'),
    Orcestra(3, 'Военный оркестр'),

    Orcestra(11, 'Струнный оркестр'),
    Orcestra(22, 'Амфитеатральный оркестр'),
    Orcestra(33, 'Асинхронный оркестр')
]

# Дирижеры
conductors = [
    Сonductor(1, 'Гавриленко ИА', 38000, 1),
    Сonductor(2, 'Воробьев ГА', 42000, 2),
    Сonductor(3, 'Нинтедович ВВ', 45000, 22),
    Сonductor(4, 'Вайбенко КК', 62000, 3),
    Сonductor(5, 'Петрухин НА', 52000, 33)
]

# Связь
conds_orcs = [
    CondOrc(1, 1),
    CondOrc(2, 2),
    CondOrc(3, 3),
    CondOrc(3, 4),
    CondOrc(3, 5),

    CondOrc(11, 1),
    CondOrc(22, 2),
    CondOrc(33, 3),
    CondOrc(33, 4),
    CondOrc(33, 5)
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(c.fio, c.sal, o.name)
                   for o in orcestras
                   for c in conductors
                   if c.dep_id == o.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(o.name, c_o.orc_id, c_o.cond_id)
                         for o in orcestras
                         for c_o in conds_orcs
                         if o.id == c_o.orc_id]

    many_to_many = [(c.fio, c.sal, orc_name)
                    for orc_name, orc_id, cond_id in many_to_many_temp
                    for c in conductors if c.id == cond_id]

    print('\n\033[36mЗадание \033[33mГ1 \033[35m' + tasks[0] + "\033[0m")
    res_11 = list(filter(lambda x: x[2].startswith('А'), one_to_many))
    for i in res_11:
        print(i)


    print('\n\033[36mЗадание \033[33mГ2 \033[35m' + tasks[1] + "\033[0m")
    res_12_unsorted = []
    # Перебираем все оркестры
    for o in orcestras:
        # Список дирижеров орекстра
        o_conds = list(filter(lambda i: i[2] == o.name, one_to_many))
        # Если оркестр не пустой
        if len(o_conds) > 0:
            # Зарплаты дирижеров оркестра
            o_sals = [sal for _, sal, _ in o_conds]
            # мксимальная зарплата дирижеров оркестра
            o_sals_max = max(o_sals)
            res_12_unsorted.append((o.name, o_sals_max))

    # Сортировка по максимальной зарплате
    # itemgetter(0) - сорт. по fio
    # itemgetter(1) - сорт. по зп
    # itemgetter(2) - сорт. по оркестрам
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    for i in res_12:
        print(i)

    print('\n\033[36mЗадание \033[33mГ3 \033[35m' + tasks[2] + "\033[0m")
    res_13 = sorted(many_to_many, key=itemgetter(2))
    for i in res_13:
        print(i)

if __name__ == '__main__':
    main()
