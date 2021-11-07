import math
from typing import List


def optimum_fitting(packages, boxes):
    result = []
    for package in packages:
        result.append(minimum_size_wasted(package, boxes))
    return result


def optimum_across_suppliers(packages: List[int], supplier_boxes: List[List[int]]):
    result = math.inf
    for boxes in supplier_boxes:
        result = min(result, optimum_fitting(packages, sorted(boxes)))
    return result


def minimum_size_wasted(package, boxes):
    box_size = math.inf
    lo = 0
    hi = len(boxes) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if boxes[mid] >= package:
            box_size = min(box_size, boxes[mid])
            hi = mid - 1
        else:
            lo = mid + 1
    print(hi)
    return box_size - package


if __name__ == '__main__':
    # packs = [3, 5, 8, 10, 11, 12]
    # boxes = [5,8,10, 14]
    # packages = [2, 3, 5]
    # s_boxes = [[4, 8], [2, 8]]

    packages = [3, 5, 8, 10, 11, 12]
    boxes = [[12], [11, 9], [10, 5, 14]]

    print(optimum_fitting(packages, [5, 10, 14]))
    # print(optimum_across_suppliers(packages, boxes))
