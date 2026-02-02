# Frequency Counter - sameFrequency
# Write a function called sameFrequency. Given two positive integers, find out if the two numbers
# have the same frequency of digits.
#
# Your solution MUST have the following complexities:
#
# Time: O(N)
#
# Sample Input:
#
# sameFrequency(182,281) // true
# sameFrequency(34,14) // false
# sameFrequency(3589578, 5879385) // true
# sameFrequency(22,222) // false

def num_freq_counter(num):
    frequency = {}
    while num > 0:
        last_digit = num % 10
        if frequency.get(last_digit):
            frequency[last_digit] += 1
        else:
            frequency[last_digit] = 1

        num //= 10

    return frequency

def same_frequency(num_1, num_2):
    num_1_freq = num_freq_counter(num_1)
    num_2_freq = num_freq_counter(num_2)

    for i in num_1_freq.keys():
        if i not in num_2_freq.keys() or num_1_freq[i] != num_2_freq[i]:
            return False

    return True


# Frequency Counter / Multiple Pointers - areThereDuplicates
# Implement a function called, areThereDuplicates which accepts a variable number of arguments,
# and checks whether there are any duplicates among the arguments passed in.  You can solve this
# using the frequency counter pattern OR the multiple pointers pattern.
#
# Examples:
#
# areThereDuplicates(1, 2, 3) // false
# areThereDuplicates(1, 2, 2) // true
# areThereDuplicates('a', 'b', 'c', 'a') // true
# Restrictions:
#
# Time - O(n)
#
# Space - O(n)
#
# Bonus:
#
# Time - O(n log n)
#
# Space - O(1)

def are_there_duplicates(*args):
    freq = {}
    for i in args:
        if freq.get(i):
            freq[i] += 1
        else:
            freq[i] = 1

    for i in freq.keys():
        if freq[i] > 1:
            return True;

    return False


# print(are_there_duplicates(1, 2, 3, 3, 1))
# print(are_there_duplicates( 2, 3, 1))
# print(are_there_duplicates( '1', '2', '3'))


# Frequency Counter - constructNote
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

def freq_counter(string):
    freq = {}
    for i in string:
        if freq.get(i):
            freq[i] += 1
        else:
            freq[i] = 1

    return freq

def construct_note(message, letter):
    freq_message = freq_counter(message)
    freq_letter = freq_counter(letter)

    for i in freq_message.keys():
        if i not in freq_letter.keys() or not(freq_letter[i] >= freq_message[i]):
            return False

    return True


# print(construct_note('aa', 'abc'))
# print(construct_note('abc', 'dcba'))
# print(construct_note('aabbcc', 'bcabcaddff'))

# Frequency Counter - findAllDuplicates
# Given an array of positive integers, some elements appear twice and others appear once.
# Find all the elements that appear twice in this array. Note that you can return the
# elements in any order.
#
# findAllDuplicates([4,3,2,7,8,2,3,1]) // array with 2 and 3
# findAllDuplicates([4, 3, 2, 1, 0]) // []
# findAllDuplicates([4, 3, 2, 1, 0, 1, 2, 3]) // array with 3, 2, and 1
# Time Complexity - O(n)

def freq_count(arr):
    freq = {}
    for i in arr:
        if freq.get(i):
            freq[i] += 1
        else:
            freq[i] = 1

    return freq

def find_all_duplicates(arr):
    duplicates = []
    arr_freq = freq_count(arr)
    for i in arr_freq.keys():
        if arr_freq[i] > 1:
            duplicates.append(i)

    return duplicates

# print(find_all_duplicates([4, 2, 7, 2, 7]))
# print(find_all_duplicates([4, 3, 2, 1, 0, 1, 2, 3]))
# print(find_all_duplicates([4, 3, 2, 1, 0]))

