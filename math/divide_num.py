def divide(dividend, divisor):
    multiplicant = -1 if (dividend < 0) ^ (divisor < 0) else 1
    output = 0
    dividend = abs(dividend)
    divisor = abs(divisor)
    while divisor <= dividend:
        dividend -= divisor
        output += 1
    return output * multiplicant


def e_divide(dividend, divisor):
    multiplicant = -1 if (dividend < 0) ^ (divisor < 0) else 1
    output = 0
    dividend = abs(dividend)
    divisor = abs(divisor)

    while divisor <= dividend:
        tmp = divisor
        mul = 1
        while tmp <= dividend:
            dividend -= tmp
            output += mul
            tmp += tmp
            mul += mul
    return output * multiplicant


if __name__ == '__main__':
    print(e_divide(100, 5))
