data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data)
    print(result)

    #result_with_lambda = data.sort(key = lambda x: x.modified)
    #print(result_with_lambda)