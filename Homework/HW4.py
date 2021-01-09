# YOUR NAME HERE

"""
Problem 1
Return the average of a list of values using a while loop.
"""


def while_average(arr):
    t = 0
    i = 0
    while i < len(arr):
        t += arr[i]
        i += 1
    return t / len(arr)


"""
Problem 2
Return the average of a list of values using a for loop.
"""


def loop_average(arr):
    t = 0
    for i in arr:
        t += i
    return t / len(arr)


"""
Problem 3
Return the number of palindromes in a list. A palindrome is a word that is the same when spelled backwards. 
"""


def palindromes(arr):
    t = 0
    for i in arr:
        if i == i[::-1]:
            t += 1
    return t


"""
Problem 4
Return the maximum value of a list. Do not use the max() function.
"""


def list_max(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max


"""
Problem 5
Given a string representing a binary (base 2) number, return its decimal representation as an int. Decimal
numbers (base 10) are the numbers that we are used to, such as 0, 1, 2, 3,...
Binary works using powers of 2, where starting from the right, the first value represents 2 ** 0, 
the second is 2 ** 1, and so on. You multiply that power of 2 by the number in that position
in the string, either 1 or 0, and add it to a sum. 
Let's take 10011 as an example.
Starting from the right:
(2 ** 0) * 1 = 1
(2 ** 1) * 1 = 2
(2 ** 2) * 0 = 0
(2 ** 3) * 0 = 0
(2 ** 4) * 1 = 16
Those numbers add up to 19.
More information here: https://www.tutorialspoint.com/how-to-convert-binary-to-decimal
You should use the function int(), which can convert strings into ints. For example, int("1") returns 1 as an int.
"""


def binary(str):
    i = 0
    t = 0
    while i < len(str):
        t += (2 ** i) * int(str[len(str) - 1 - i])
        i += 1
    return t

str = '100000000'
print(binary(str))
