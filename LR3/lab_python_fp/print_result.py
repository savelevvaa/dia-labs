# Здесь должна быть реализация декоратора
def print_result(func_to_decorate):
    def decorated_func():
        funcName = str(func_to_decorate).split()[1]
        funcReturn = func_to_decorate()
        print(funcName)
        if type(funcReturn) == dict:
            for k, v in funcReturn.items():
                print(str(k) + " = " + str(v))
        elif type(funcReturn) == list:
            for v in funcReturn:
                print(v)
        else:
            print(funcReturn)
        return funcReturn

    return decorated_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()