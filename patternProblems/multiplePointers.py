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
    # if len(nums) > 2:
    #     return False
    #
    # i = 0
    # j = len(nums) - 1
    #
    # while i != j:
    #     average = (nums[i] + nums[j]) / 2
    #     if average == target:
    #         return True
    #     elif average > target:
    #         j -= 1
    #     else:
    #         i += 1
    #
    # return False

print(average_pair([1,2,3],2.5))
# print(average_pair([1,3,3,5,6,7,10,12,19],8))
# print(average_pair([-1,0,3,4,5,6], 4.1))
# print(average_pair([],4))
