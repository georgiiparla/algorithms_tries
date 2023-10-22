def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


my_arr = [4, 1, 2, 645, 12, 3432, 11, 124, 54, 21]
print(bubble_sort(my_arr))
