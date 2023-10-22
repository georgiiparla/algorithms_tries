'''One brute force approach is to consider every pair of elements and check if their sum equals the target. This can be done using nested loops, where the outer loop iterates from the first element to the second-to-last element, and the inner loop iterates from the next element to the last element. However, this approach has a time complexity of O(n^2).'''

# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n-1):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []


'''Create an empty hash table to store elements and their indices.
Iterate through the array from left to right.
For each element nums[i], calculate the complement by subtracting it from the target: complement = target - nums[i].
Check if the complement exists in the hash table. If it does, we have found a solution.
If the complement does not exist in the hash table, add the current element nums[i] to the hash table with its index as the value.
Repeat steps 3-5 until we find a solution or reach the end of the array.
If no solution is found, return an empty array or an appropriate indicator.
This approach has a time complexity of O(n) since hash table lookups take constant time on average. It allows us to solve the Two Sum problem efficiently by making just one pass through the array.'''

def twoSum(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if hash_table.get(complement) is not None:
            return [i, hash_table[complement]]
        else:
            hash_table[nums[i]] = i
    return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = {}
#         n = len(nums)

#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap:
#                 return [numMap[complement], i]
#             numMap[nums[i]] = i

#         return []  # No solution found

print(twoSum(nums = [2,7,11,15], target = 9))
