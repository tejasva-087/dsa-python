def are_there_duplicates(*args):
    sorted_arr = sorted(args)

    i = 0
    for j in range(1, len(sorted_arr)):
        if sorted_arr[i] == sorted_arr[j]:
            return True
        else:
            i = j

    return False


# print(are_there_duplicates(1, 2, 3, 3, 1))
# print(are_there_duplicates(2, 3, 1))
# print(are_there_duplicates('1', '2', '3'))

# constructNote
# Write a function called constructNote, which accepts two strings, a message and some letters.
# The function should return true if the message can be built with the letters that you are given,
# or it should return false.
#
# Assume that there are only lowercase letters and no space or special characters in
# both the message and the letters.
#
# Bonus Constraints:
#
# If M is the length of message and N is the length of letters:
#
# Time Complexity: O(M+N)
#
# Space Complexity: O(N)
#
# Examples:
#
# constructNote('aa', 'abc') // false
# constructNote('abc', 'dcba') // true
# constructNote('aabbcc', 'bcabcaddff') // true

def construct_note(message, letter):
    sorted_message = ''.join(sorted(message))
    sorted_letter = ''.join(sorted(letter))

    letter_ptr = 0
    message_ptr = 0

    while letter_ptr < len(sorted_letter):
        if sorted_letter[letter_ptr] == sorted_message[message_ptr]:
            message_ptr += 1

        letter_ptr += 1

        if message_ptr == len(sorted_message):
            return True

    return False

# print(construct_note('aa', 'abc'))
# print(construct_note('abc', 'dcba'))
# print(construct_note('aabbcc', 'bcabcaddff'))


# findAllDuplicates
# Given an array of positive integers, some elements appear twice and others appear once.
# Find all the elements that appear twice in this array. Note that you can return the
# elements in any order.
#
# findAllDuplicates([4,3,2,7,8,2,3,1]) // array with 2 and 3
# findAllDuplicates([4, 3, 2, 1, 0]) // []
# findAllDuplicates([4, 3, 2, 1, 0, 1, 2, 3]) // array with 3, 2, and 1
# Time Complexity - O(n)

def find_all_duplicates(arr):
    sorted_arr = sorted(arr)
    duplicates = []

    i = 0
    for j in range(1, len(sorted_arr)):
        if sorted_arr[i] == sorted_arr[j]:
            duplicates.append(sorted_arr[i])

        else:
            i = j

    return duplicates

# print(find_all_duplicates([4, 2, 7, 2, 7]))
# print(find_all_duplicates([4, 3, 2, 1, 0, 1, 2, 3]))
# print(find_all_duplicates([4, 3, 2, 1, 0]))


# Multiple Pointers - averagePair
# Write a function called averagePair. Given a sorted array of integers and a target average,
# determine if there is a pair of values in the array where the average of the pair equals
# the target average. There may be more than one pair that matches the average target.
#
# Bonus Constraints:
#
# Time: O(N)
#
# Space: O(1)
#
# Sample Input:
#
# averagePair([1,2,3],2.5) // true
# averagePair([1,3,3,5,6,7,10,12,19],8) // true
# averagePair([-1,0,3,4,5,6], 4.1) // false
# averagePair([],4) // false


def average_pair(nums, target):
    if not len(nums):
        return False

    left_ptr = 0
    right_ptr = len(nums) - 1

    while left_ptr != right_ptr:
        avg = (nums[left_ptr] + nums[right_ptr]) / 2

        if avg == target:
            return True
        elif avg > target:
            right_ptr -= 1
        else:
            left_ptr += 1

    return False

# print(average_pair([1,2,3],2.5))
# print(average_pair([1,3,3,5,6,7,10,12,19],8))
# print(average_pair([-1,0,3,4,5,6], 4.1))
# print(average_pair([],4))


# Multiple Pointers - isSubsequence
# Write a function called isSubsequence which takes in two strings and checks whether the characters
# in the first string form a subsequence of the characters in the second string. In other words, the
# function should check whether the characters in the first string appear somewhere in the second string,
# without their order changing.
#
# Examples:
#
# isSubsequence('hello', 'hello world'); // true
# isSubsequence('sing', 'sting'); // true
# isSubsequence('abc', 'abracadabra'); // true
# isSubsequence('abc', 'acb'); // false (order matters)
# Your solution MUST have AT LEAST the following complexities:
#
# Time Complexity - O(N + M)
#
# Space Complexity - O(1)

def is_subsequence(sub_string, string):
    sub_str_ptr = 0

    for i in string:
        if i == sub_string[sub_str_ptr]:
            sub_str_ptr += 1

        if sub_str_ptr == len(sub_string):
            return True

    return False

# print(is_subsequence('Hello', 'Hello world'))
# print(is_subsequence('sing', 'sting'))
# print(is_subsequence('abc', 'abracadabra'))
# print(is_subsequence('abc', 'acb'))

# Frequency Counter / Multiple Pointer - findPair
# Given an unsorted array and a number n, find if there exists a pair of elements in the array whose
# difference is n. This function should return true if the pair exists or false if it does not.
#
# findPair([6,1,4,10,2,4], 2) // true
# findPair([8,6,2,4,1,0,2,5,13],1) // true
# findPair([4,-2,3,10],-6) // true
# findPair([6,1,4,10,2,4], 22) // false
# findPair([], 0) // false
# findPair([5,5], 0) // true
# findPair([-4,4], -8) // true
# findPair([-4,4], 8) // true
# findPair([1,3,4,6],-2) // true
# findPair([0,1,3,4,6],-2) // true
# findPair([1,2,3], 0) // false
# Part 1 - solve this with the following requirements:
#
# Time Complexity Requirement - O(n)
#
# Space Complexity Requirement - O(n)
#
# Part 2 - solve this with the following requirements:
#
# Time Complexity Requirement - O(n log n)
#
# Space Complexity Requirement - O(1)

def find_pair(nums, target):
    if len(nums) < 2:
        return False

    nums.sort()
    target = abs(target)

    left_ptr = 0
    right_ptr = 1

    while left_ptr < len(nums) and right_ptr < len(nums):
        if left_ptr != right_ptr:
            difference = nums[right_ptr] - nums[left_ptr]
            if difference == target:
                return True
            elif difference < target:
                right_ptr += 1
            else:
                left_ptr -= 1
        else:
            right_ptr += 1

    return False


print(find_pair([6, 1, 4, 10, 2, 4], 2))
print(find_pair([8,6,2,4,1,0,2,5,13],1))
print(find_pair([4,-2,3,10],-6))
print(find_pair([6,1,4,10,2,4], 22))
print(find_pair([], 0))
print(find_pair([5,5], 0))
print(find_pair([-4,4], -8))
print(find_pair([-4,4], 8))
print(find_pair([1,3,4,6],-2))
print(find_pair([0,1,3,4,6],-2))
print(find_pair([1,2,3], 0))