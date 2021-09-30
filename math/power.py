def recur(x, n):
    if not n:
        return 1.0
    half = recur(x, n // 2)
    return half ** 2 if n % 2 == 0 else x * (half ** 2)


def power(x, n):
    return recur(1 / x, -n) if n < 0 else recur(x, n)


if __name__ == '__main__':
    print(power(2, 5))
