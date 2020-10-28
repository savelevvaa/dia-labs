def print_result(func):
  def decoratedFunc(*args, **kwargs):
    result = func(*args, **kwargs)
    print("\033[31m" + func.__name__ + "\033[0m")
    if isinstance(result, dict):
      for key in result.keys():
        print("{} = {}".format(key, result[key]))
    elif isinstance(result, list):
      for value in result:
        print(value)
    else:
      print(result)
    return result
  return decoratedFunc



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


def main():
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()