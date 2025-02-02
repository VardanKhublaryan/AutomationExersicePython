def max_value(numbers):
    maximum = numbers[0]
    for i in numbers:
        if i > maximum:
            maximum = i
    return maximum


def binary_search(arr, low, high, x):
    if high >= low:
        mid = high - low // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return binary_search(arr, mid, high - 1, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1


def fibonachi(num):
    if num <= 0:
        return 0
    elif num <= 1:
        return 1
    return fibonachi(num - 1) + fibonachi(num - 2)


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


arr = [2, 3, 4, 10, 40]
print(max_value([3, 5, 4, 7, 8, 7]))
print(fibonachi(4))
print(factorial(5))
print(binary_search(arr, 0, len(arr) - 1, 40))
