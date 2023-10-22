def find_max_num_rec(sampleArray, n):
    if n == 1:
        return sampleArray[0]
    return max(sampleArray[n-1], find_max_num_rec(sampleArray, n - 1))
