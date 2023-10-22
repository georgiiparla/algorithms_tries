def recursive_sum(arr):
    total = arr[0]
    if len(arr) <= 1:
        return arr[0]
    else:
        return total + recursive_sum(arr[1:])
    

print(recursive_sum([2, 4, 5, 1, 5, 7, 7, 12, 3]))


# def recursive_sum(arr):
#     return arr[0] if len(arr) == 1 else arr[0] + recursive_sum(arr[1:])

# print(recursive_sum([2, 4, 5, 1, 5, 7, 7, 12, 3]))
