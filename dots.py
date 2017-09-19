"""По данным nn отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит
хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих nn строк содержит по два числа
0≤l≤r≤10^9, задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек.
Если таких множеств точек несколько, выведите любое из них."""


segments = []
n = int(input())
for i in range(1, n + 1):
    x, y = map(int, input().split())
    segments.append([x, y])


def get_key(item):
    return item[1]

segments.sort(key=get_key)

i = 0
while i != len(segments) - 1:
    if segments[i][1] >= segments[i + 1][0]:
        new_segment = [segments[i + 1][0], segments[i][1]]
        del segments[i + 1], segments[i]
        segments.insert(i, new_segment)
    else:
        i += 1


print(len(segments))
for segment in segments:
    print(segment[1], end=' ')
