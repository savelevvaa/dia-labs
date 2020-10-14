def field(items, *args):
    assert len(args) > 0, 'No Args'
    for i in items:
        for arg in args:
            print(arg, '->', i[arg], end = ", ")
        print("\b\b;")

# goods = [
#     {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#     {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
#
# field(goods, 'title', 'price')
# field(goods)
