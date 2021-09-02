def permute(digits, result=None, curr=None):
    if curr is None:
        curr = []

    if result is None:
        result = []

    if not digits:
        result.append(curr)
        return result

    for i in range(len(digits)):
        result = permute(digits[:i] + digits[i + 1:], result, curr + [digits[i]])

    return result


def valid_hours(digits):
    return digits[0] * 10 + digits[1] < 24


def valid_minutes(digits):
    return digits[2] * 10 + digits[3] < 60


def valid_time(digits):
    return valid_hours(digits) and valid_minutes(digits)


def largest_time_from_digits(digits):
    all_possible = permute(sorted(digits))
    valid_combinations = list(filter(valid_time, all_possible))
    if not valid_combinations:
        return ""
    hour_1, hour_2, minute_1, minute_2 = valid_combinations[-1]
    return "{0}{1}:{2}{3}".format(hour_1, hour_2, minute_1, minute_2)


if __name__ == '__main__':
    print(largest_time_from_digits([5, 5, 5, 5]))
    print(largest_time_from_digits([0, 0, 0, 1]))
