def insertion_sort(arr):
    for i in range(1, len(arr)):  # TRICKY! We implicitly moved one element to the left
        # (sorted array) by starting main array from 1 (so element 0 - first element of
        # sorted array)
        key = arr[i]  # Then we save for future the element that we will compare with
        # all elements in sorted array
        j = i - 1  # This is generally the largest element of sorted array ( 1 element to
        # the left
        while j >= 0 and key < arr[j]:  # j >= 0 condition for the first time to do not get
            # further to -1 index, key < arr[j] to determine if saved element is smaller
            # than the largest element in the sorted part
            arr[j + 1] = arr[j]  # If it is smaller, basically, we don't need it in that
            # unsorted sequence, so we substitute it with the largest one from sorted part
            # and afterward (as now we have two same largest elements) we can freely
            # substitute one copy with the element which will be larger than the new element
            # from unsorted part
            j -= 1  # prepare index for the next element which smaller than the largest
            # in sorted part to compare it with the new element from unsorted part
        arr[j + 1] = key  # eventually (as the sorted part is shifted to the right and we have
        # one extra copied element in the sequence, we can freely substitute it with the new
        # element from unsorted part)
    return arr


def insertion_sort2(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# my_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
# print(insertion_sort2(my_list))
