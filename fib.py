""" поиск числа фибоначчи """
# Дано целое число 1≤n≤40, необходимо вычислить n-е число Фибоначчи (напомним, что F0=0, F1=1 и Fn= Fn−1 + Fn−2 при n≥2).


def fib(n):
    if n == 1:
        return 1
    else:
        fib_lst = list(range(n + 1))
        fib_lst[0] = 0
        fib_lst[1] = 1
        for i in range(3, n + 1):
            fib_lst[i] = fib_lst[i - 1] + fib_lst[i - 2]
        return fib_lst[n - 1]


def main1():
    n = int(input())
    print(fib(n))

""" последняя цифра большого числа Фибоначчи """


def fib_digit(n):
    if n == 1:
            return 1
    else:
        fib_lst = list(range(n + 1))
        fib_lst[0] = 0
        fib_lst[1] = 1
        for i in range(3, n + 1):
            fib_lst[i] = fib_lst[i - 1] % 10 + fib_lst[i - 2] % 10
        return fib_lst[n - 1] % 10


def main2():
    n = int(input())
    print(fib_digit(n))


""" декоратор для рекурсивного вычисления """


def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner

