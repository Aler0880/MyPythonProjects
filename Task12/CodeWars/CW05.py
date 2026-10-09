def minimum(arr):
    return sorted(arr)[0]


def maximum(arr):
    return sorted(arr, reverse=True)[0]


print(minimum([1, 2, 3, 8, 345, 8, 9, 56]))
print(maximum([1, 2, 3, 8, 345, 8, 9, 56]))
