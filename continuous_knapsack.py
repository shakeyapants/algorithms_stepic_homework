# coding=utf-8

"""Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6.
Каждая из следующих nn строк задаёт стоимость 0≤ci≤2⋅10^6 и объём 0<wi≤2⋅10^6 предмета
(nn, WW, cici, wiwi — целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно
отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
с точностью не менее трёх знаков после запятой. """


items = []
n, w = map(int, input().split())
c_sum = 0
for i in range(1, n + 1):
    x, y = map(int, input().split())
    price = x / y
    items.append([x, y, price])


def get_key(item):
    return item[2]

items.sort(key=get_key)
for item in items:
    if n > 0 and w > 0:
        put = items.pop()
        if put[1] <= w:
            w -= put[1]
            n -= 1
            c_sum += put[0]
        else:
            space = w
            w = 0
            c = put[0] / put[1] * space
            c_sum += c
            n -= 1


print('%.3f' % c_sum)
