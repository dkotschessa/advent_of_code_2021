file = open('input.txt', 'r')

num = file.read().splitlines()

numbers = [int(x) for x in num]




def positive_difference(arr):
    differences = [y-x for x, y in zip(arr, arr[1:])]
    number_of_positive_differences = [x > 0 for x in differences].count(True)
    return number_of_positive_differences


def three_sums(arr):
    sums = [x+y+z for x, y, z in zip(arr, arr[1:], arr[2:])]
    return sums

