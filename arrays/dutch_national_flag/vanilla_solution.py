def three_way_partion(array):
    small, middle, large = 0, 0, len(array) - 1

    while middle <= large:
        if array[middle] == 0:
            array[small], array[middle] = array[middle], array[small]
            small += 1
            middle += 1
            continue
        if array[middle] == 2:
            array[large], array[middle] = array[middle], array[large]
            large -= 1
            continue
        middle += 1
    return array


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]

    print(three_way_partion(nums))
