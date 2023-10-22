def selection_sort(arr):
    for i in range(len(arr)):   # We go through all elements this time
        min_index = i   # Save very first item cell to swap them with the smallest element
        for j in range(i + 1, len(arr)):    # Check further elements
            if arr[min_index] > arr[j]:     # Comparison whether one element is less or not
                arr[min_index], arr[j] = arr[j], arr[min_index]     # Swapping
    return arr


my_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(selection_sort(my_list))
