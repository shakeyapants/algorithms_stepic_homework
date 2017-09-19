""" наибольший общий делитель """


def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd(a % b, b)
    elif a < b:
        return gcd(a, b % a)


def gcd2(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return gcd2(b % a, a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
