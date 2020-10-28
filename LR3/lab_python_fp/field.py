def field(items, *args):
    assert len(args) > 0, 'No Args'
    if len(args) > 1:
        for item in items:
            dict = {}
            for arg in args:
                if (arg in item) and (item[arg] is not None):
                    dict[arg] = item[arg]
            if len(dict.keys()) > 0:
                yield dict
    elif len(args) == 1:
        for item in items:
            for arg in args:
                if (arg in item) and (item[arg] is not None):
                    yield item[arg]

def main():
    print(list(field(goods, 'title', 'price')))
    print(list(field(goods, 'color')))
    print(list(field(goods, 'title')))

goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': None},
    ]

if __name__ == '__main__':
    main()


