def quicksort(arr, lo, hi):
    """
    Sorts the given array in ascending order using the Quicksort algorithm.

    Parameters:
    arr (list): The array to be sorted
    lo (int): The index of the first element in the sub-array to be sorted
    hi (int): The index of the last element in the sub-array to be sorted

    """

    if lo < hi:
        # Partition the array and get the index of the pivot element
        p = partition(arr, lo, hi)

        # Recursively sort the left and right partitions
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)


def partition(arr, lo, hi):
    """
    Partition the sub-array by selecting the last element as the pivot, and rearranging the array so that all elements to the left of the pivot are less than or equal to the pivot, and all elements to the right of the pivot are greater than the pivot.

    Parameters:
    arr (list): The array to be partitioned
    lo (int): The index of the first element in the sub-array to be partitioned
    hi (int): The index of the last element in the sub-array to be partitioned

    Returns:
    int: The index of the pivot element after partitioning

    """

    # Select the last element as the pivot
    pivot = arr[hi]
    i = lo - 1

    # Loop through the sub-array and partition it
    for j in range(lo, hi):
        if arr[j] <= pivot:
            # Move the element to the left partition
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Move the pivot element to its final position in the array
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    # Return the index of the pivot element
    return i + 1


arr = [10, 7, 8, 9, 1, 5, 0, 23, 14, 12]  
n = len(arr)  
quicksort(arr, 0, n-1)  
print("Sorted array:", arr)  
