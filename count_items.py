def count_items(arr):
    if not arr[1:]:
        return 1
    else:
        return 1 + count_items(arr[1:])


print(count_items([2, 4]))
