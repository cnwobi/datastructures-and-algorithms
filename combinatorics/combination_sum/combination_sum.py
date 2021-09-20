def combination_sum(a, total):
    result = []
    seen = set()

    def combination(path, index, running_sum):
        key = tuple(path)
        if running_sum == total and key not in seen:
            result.append(path)
            seen.add(key)
            return

        if index == len(a) or running_sum > total:
            return

        for i in range(index, len(a)):
            num = a[i]
            if (num + running_sum) <= total:
                combination(path + [num], i, num + running_sum)
                combination(path + [num], i + 1, num + running_sum)

    combination([], 0, 0)
    print(result)


if __name__ == '__main__':
    combination_sum([2, 3, 5, 9], 9)
