# Given an array of 1s and 0s which has all 1s first followed by all 0s, write a function
# called countZeroes, which returns the number of zeroes in the array.
#
# countZeroes([1,1,1,1,0,0]) // 2
# countZeroes([1,0,0,0,0]) // 4
# countZeroes([0,0,0]) // 3
# countZeroes([1,1,1,1]) // 0
# Time Complexity - O(log n)

import math

def count_zeroes(arr):

    def first_zero(array, start, end):
        if start <= end:
            mid = start + (end - start) // 2

            if array[mid] == 0 and (array[mid - 1] == 1 or mid == 0):
                return mid

            if array[mid] == 1:
                return first_zero(array, mid + 1, end)

            else:
                return first_zero(array, start, mid - 1)

        return -1

    first_0 = first_zero(arr, 0, len(arr) - 1)

    if first_0 == -1: return 0

    return len(arr) - first_0




# print(count_zeroes([1,1,1,1,0,0]))
# print(count_zeroes([1,0,0,0,0]))
# print(count_zeroes([0,0,0]))
# print(count_zeroes([1,1,1,1]))

# Divide and Conquer - sortedFrequency
# Given a sorted array and a number, write a function called sortedFrequency that counts
# the occurrences of the number in the array
#
# sortedFrequency([1,1,2,2,2,2,3],2) // 4
# sortedFrequency([1,1,2,2,2,2,3],3) // 1
# sortedFrequency([1,1,2,2,2,2,3],1) // 2
# sortedFrequency([1,1,2,2,2,2,3],4) // -1
# Time Complexity - O(log n)


def sorted_frequency(arr, target):
    def first_occurrence(array, value, start, end):
        if start <= end:
            mid = start + (end - start) // 2

            if (mid == 0 or arr[mid - 1] < value) and arr[mid] == value:
                return mid
            elif arr[mid] < value:
                return first_occurrence(array, value,mid + 1, end)
            else:
                return first_occurrence(array, value,start, mid - 1)
        else:
            return -1


    def last_occurrence(array, value, start, end):
        if start <= end:
            mid = start + (end - start) // 2

            if arr[mid] == value and (mid == len(array) - 1 or arr[mid + 1] > value):
                return mid
            elif arr[mid] > value:
                return last_occurrence(array, value, start, mid - 1)
            else:
                return last_occurrence(array, value, mid + 1, end)

        else:
            return -1


    first = first_occurrence(arr, target, 0, len(arr) - 1)
    last = last_occurrence(arr, target, 0, len(arr) - 1)

    if first == -1 or last == -1:
        return 0
    else:
        return last - first + 1


# print(sorted_frequency([1,1,2,2,2,2,3],2))
# print(sorted_frequency([1,1,2,2,2,2,3],3))
# print(sorted_frequency([1,1,2,2,2,2,3],1))
# print(sorted_frequency([1,1,2,2,2,2,3],4))

# Divide and Conquer - findRotatedIndex
# Write a function called findRotatedIndex which accepts a rotated array of sorted numbers and an integer.
# The function should return the index of the integer in the array. If the value is not found, return -1.
#
# Constraints:
#
# Time Complexity - O(log n)
#
# Space Complexity - O(1)
#
# findRotatedIndex([3,4,1,2],4) // 1
# findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8) // 2
# findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3) // 6
# findRotatedIndex([37,44,66,102,10,22],14) // -1
# findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12) // -1
# findRotatedIndex([11,12,13,14,15,16,3,5,7,9], 16) // 5

def find_rotated_index(arr, value):

    def find_index(array, target, start, end):
        if start <= end:
            mid = start + (end - start) // 2

            if array[mid] == value:
                return mid

            if array[start] <= array[mid]:
                if array[start] <= target <= array[mid]:
                    return find_index(array, target, start, mid - 1)
                else:
                    return find_index(array, target, mid + 1, end)

            else:
                if array[mid] <= target <= array[end]:
                    return find_index(array, target, mid + 1, end)
                else:
                    return find_index(array, target, start, mid - 1)

        else:
            return -1

    return find_index(arr, value, 0, len(arr) - 1)


print(find_rotated_index([3,4,1,2],4))
print(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 8))
print(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 3))
print(find_rotated_index([37,44,66,102,10,22],14))
print(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 12))
print(find_rotated_index([11,12,13,14,15,16,3,5,7,9], 16))
