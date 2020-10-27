def print_result(func):
  def wrapper(*args, **kwargs):
    res = func(*args, **kwargs)
    print("\033[31m" + func.__name__ + "\033[0m")
    if isinstance(res, dict):
      for k in res.keys():
        print("{} = {}".format(k, res[k]))
    elif isinstance(res, list):
      for val in res:
        print(val)
    else:
      print(res)
    return res
  return wrapper



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