def field(items, *args):
    assert len(args) > 0
    
    if len(args) == 1:
        for item in items:
            if args[0] in item.keys():
                yield item.get(args[0])

    else:
        for item in items:
            res = {key: item.get(key) for key in args if key in item.keys()}
            if len(res) != 0:
                yield res


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'Название': 'Stol', 'Цена': 'Бесценно'},
    {'title': 'Стул', 'price': 1200, 'Цвет': 'жолтый'}
]

if __name__ == '__main__':
    gen = field(goods, 'title')
    for el in gen:
        print(el)

    gen = field(goods, 'title', 'price', 'color')
    for el in gen:
        print(el)
