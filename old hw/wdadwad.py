arr = {1, 3, -6, 7}
def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum