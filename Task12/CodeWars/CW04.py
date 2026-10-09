# def century(year):
#     return -(-year // 100)


# print(century(2000.1))

# from math import ceil


# def century(year):
#     return ceil(year / 100)


# def century(year):
#     return (year + 99) // 100


# print(century(2000.1))


def sum_array(arr):
    if type(arr) is not list:
        return 0
    elif len(arr) >= 2:
        arr.remove(min(arr))
        arr.remove(max(arr))
        return sum(arr)
    else:
        return 0


print(sum_array(None))
