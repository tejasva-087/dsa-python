# Sliding Window - maxSubarraySum
# Given an array of integers and a number, write a function called maxSubarraySum,
# which finds the maximum sum of a subarray with the length of the number passed to the function.
#
# Note that a subarray must consist of consecutive elements from the original array.
# In the first example below, [100, 200, 300] is a subarray of the original array, but [100, 300] is not.
#
# maxSubarraySum([100,200,300,400], 2) // 700
# maxSubarraySum([1,4,2,10,23,3,1,0,20], 4)  // 39
# maxSubarraySum([-3,4,0,-2,6,-1], 2) // 5
# maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2) // 5
# maxSubarraySum([2,3], 3) // null
# Constraints:
#
# Time Complexity - O(N)
#
# Space Complexity - O(1)

# maxSubarraySum([100,200,300,400], 2) # 700
# maxSubarraySum([1,4,2,10,23,3,1,0,20], 4)  # 39
# maxSubarraySum([-3,4,0,-2,6,-1], 2) # 5
# maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2) # 5
# maxSubarraySum([2,3], 3) # null

def max_subarray_sum(arr, num):
    if num > len(arr): return None

    total = 0
    for i in range(0, num):
        total += arr[i]

    current_total = total
    for i in range(num, len(arr)):
        current_total += arr[i] - arr[abs(num - i)]

        if current_total > total:
            total = current_total

    return total


# print(max_subarray_sum([100,200,300,400], 2))
# print(max_subarray_sum([1,4,2,10,23,3,1,0,20], 4))
# print(max_subarray_sum([-3,4,0,-2,6,-1], 2))
# print(max_subarray_sum([3,-2,7,-4,1,-1,4,-2,1],2))
# print(max_subarray_sum([2,3], 3))

# Sliding Window - minSubArrayLen
# Write a function called minSubArrayLen which accepts two parameters - an array of positive integers
# and a positive integer.
#
# This function should return the minimal length of a contiguous subarray of which the sum is greater than
# or equal to the integer passed to the function. If there isn't one, return 0 instead.
# Examples:
#
# minSubArrayLen([2,3,1,2,4,3], 7) // 2 -> because [4,3] is the smallest subarray
# minSubArrayLen([2,1,6,5,4], 9) // 2 -> because [5,4] is the smallest subarray
# minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52) // 1 -> because [62] is greater than 52
# minSubArrayLen([1,4,16,22,5,7,8,9,10],39) // 3
# minSubArrayLen([1,4,16,22,5,7,8,9,10],55) // 5
# minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11) // 2
# minSubArrayLen([1,4,16,22,5,7,8,9,10],95) // 0
# Time Complexity - O(n)
#
# Space Complexity - O(1)

def min_subarray_len(arr, target):
    start = 0
    end = 0
    total = 0
    min_len = float('inf')


    while start < len(arr):
        if total < target and end < len(arr):
            total += arr[end]
            end += 1
        elif total >= target:
            if min_len > end - start:
                min_len = end - start
            total -= arr[start]
            start += 1
        else:
            break

    if min_len == float('inf'):
        return 0
    else:
        return min_len


# print(min_subarray_len([2,3,1,2,4,3], 7))
# print(min_subarray_len([2,1,6,5,4], 9))
# print(min_subarray_len([3,1,7,11,2,9,8,21,62,33,19], 52))
# print(min_subarray_len([1,4,16,22,5,7,8,9,10],39))
# print(min_subarray_len([1,4,16,22,5,7,8,9,10],55))
# print(min_subarray_len([4, 3, 3, 8, 1, 2, 3], 11))
# print(min_subarray_len([1,4,16,22,5,7,8,9,10],95))

# Sliding Window - findLongestSubstring
# Write a function called findLongestSubstring, which accepts a string and returns the length of the longest
# substring with all distinct characters.
#
# findLongestSubstring('') // 0
# findLongestSubstring('rithmschool') // 7
# findLongestSubstring('thisisawesome') // 6
# findLongestSubstring('thecatinthehat') // 7
# findLongestSubstring('bbbbbb') // 1
# findLongestSubstring('longestsubstring') // 8
# findLongestSubstring('thisishowwedoit') // 6
# Time Complexity - O(n)


def find_longest_substring(string):
    start = 0
    longest = 0
    seen = {}

    for i in range(len(string)):
        char = string[i]

        if char in seen and seen[char] >= start:
            start = seen[char] + 1

        seen[char] = i

        longest = max(longest, i - start + 1)


    return longest


print(find_longest_substring(''))
print(find_longest_substring('rithmschool'))
print(find_longest_substring('thisisawesome'))
print(find_longest_substring('thecatinthehat'))
print(find_longest_substring('bbbbbb'))
print(find_longest_substring('longestsubstring'))
print(find_longest_substring('thisishowwedoit'))
