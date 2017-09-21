""" По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно представить как сумму k различных
натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.
"""

n = int(input())
n_sum = [1]
s = 1
i = 2

while n != s:
    n_sum.append(i)
    s += i
    if s > n:
        s -= (i + n_sum[-2])
        del n_sum[-2:]
        continue
    i += 1

print(len(n_sum))
print(" ".join(map(str, n_sum)))
