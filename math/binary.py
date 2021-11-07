import dis


def char_to_binary(word):
    result = []
    for letter in word:
        result.append(str(bin(ord(letter))))

    result = [r[2:] for r in result]

    return result[::-1]


def char_to_binary2(word):
    return [str(bin(ord(letter)))[2:] for letter in word]


def power(n, x):
    if x == 0:
        return 1.0
    half = power(n, x // 2)
    return half ** 2 if x % 2 == 0 else n * half ** 2


def find_index(inputs, target):
    def find_lower():
        low = 0
        high = len(inputs) - 1

        while low <= high:
            mid = (low + high) // 2
            if inputs[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def find_higher():
        low = 0
        high = len(inputs) - 1

        while low <= high:
            mid = (low + high) // 2
            if inputs[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return high

    lo = find_lower()
    hi = find_higher()

    return [-1, -1] if lo == len(inputs) else [lo, hi]


if __name__ == '__main__':
    inputs = [4, 6, 9, 11, 11, 11, 11, 21, 40, 60, 60, 80]
    print(find_index(inputs, 9))
