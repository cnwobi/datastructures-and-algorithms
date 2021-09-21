from typing import List


def permutation(num, path, curr, target, result, operand=False):
    if curr == target:
        if path and operand:
            result.append(path)

    for i in range(len(num)):
        for j in range(i, len(num)):
            if not path and num[i:j + 1]:
                permutation(num[j + 1:], path + num[i:j + 1], int(num[i:j + 1]), target, result, False)
            elif path and num[i:j + 1]:
                if curr + int(num[i:j + 1]) <= target:
                    permutation(num[j + 1:], path + "+" + num[i:j + 1], curr + int(num[i:j + 1]), target, result, True)
                if curr * int(num[i:j + 1]) <= target:
                    permutation(num[j + 1:], path + "*" + num[i:j + 1], curr * int(num[i:j + 1]), target, result, True)
                if curr - int(num[i:j + 1]) <= target:
                    permutation(num[j + 1:], path + "-" + num[i:j + 1], curr - int(num[i:j + 1]), target, result, True)


def addOperators(num: str, target: int) -> List[str]:
    result = []
    permutation(num, "", 0, target, result)
    return result


if __name__ == '__main__':
    num = "123"
    target = 6

    print(addOperators(num, target))
