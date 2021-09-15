import math

def days_required(car_size, weights):
    days = 1
    curr_capacity = 0
    for weight in weights:
        if curr_capacity + weight > car_size:
            days += 1
            curr_capacity = weight
        else:
            curr_capacity += weight
    return days

def find_min_car_size(weights, days):
    min_car_size = max(weights)
    max_car_size = sum(weights)
    result = math.inf
    while min_car_size <= max_car_size:
        mid = min_car_size + ((max_car_size - min_car_size) // 2)
        required = days_required(mid, weights)
        if required <= days:
            result = min(result, mid)
            max_car_size = mid - 1
        else:
            min_car_size = mid + 1
    return result


if __name__ == '__main__':
    print(find_min_car_size([1, 5, 7, 3, 2, 9], 3))
