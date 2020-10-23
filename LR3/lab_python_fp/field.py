def field(items, *args):
    assert len(args) > 0, 'No Args'
    for i in items:
        for arg in args:
            yield i[arg]
            #rint(arg, '->', i[arg], end = ", ")
        #print("\b\b;")

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

temp = field(goods, 'title', 'price')
print(field(goods))

for i in range(2):
    j = next(temp)
    print(j)
