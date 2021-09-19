from typing import List


def fraction_to_decimal(num, denom):
    result = [abs(num) // abs(denom)]
    remainder = num % denom

    if num < 0 ^ denom < 0:
        result.append("-")

    if remainder == 0:
        return "".join(list(map(str, result)))
    result.append(".")

    repeat = {}
    while remainder != 0:
        if remainder in repeat:
            result.insert(repeat[remainder], "(")
            result.append(")")
            break
        repeat[remainder] = len(result)
        remainder *= 10
        result.append(remainder // denom)
        remainder %= denom
    return "".join(list(map(str, result)))


if __name__ == '__main__':
    print(fraction_to_decimal(2,3))
