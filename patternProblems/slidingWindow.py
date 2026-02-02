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

def maxSubarraySum(arr, num):
    if num > len(arr):
        return None

    max_sum = 0
    for i in range(0, num):
        max_sum += arr[i]

    i = 0
    j = num
    while j < len(arr) - 1:
        window_sum = window_sum + arr[j] - arr[i]

        if window_sum > max_sum:
            max_sum = window_sum

        i += 1
        j += 1

    print(max_sum)



# maxSubarraySum([100,200,300,400], 2) # 700
# maxSubarraySum([1,4,2,10,23,3,1,0,20], 4)  # 39
maxSubarraySum([-3,4,0,-2,6,-1], 2) # 5
# maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2) # 5
# maxSubarraySum([2,3], 3) # null