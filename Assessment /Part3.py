def merge_arrays(arr1, arr2):
    """Merge two sorted arrays into one sorted array"""
    arr3 = arr1 + arr2
    arr3.sort()
    return arr3
    

def intersection_of_arrays(arr1, arr2):
    """Return the intersection of two arrays"""
    set1 = set(arr1)
    set2 = set(arr2)

    return list(set1.intersection(set2))


def fibonacci_dp(n):
    """Dynamic Programming method to find the nth Fibonacci number"""
    if n <= 0:
        return n
    elif n <= 1:
        return n
    else:
        return fibonacci_dp(n-1) + fibonacci_dp(n-2)


def reverse_string_words(s):
    """Reverse the words in a string"""
    if s == "":
        return ""
    else:
        my_list = s.split()
        my_list.reverse()
        my_string = ""

        for i in range(len(my_list)):
            if i != len(my_list) - 1:
                my_string += my_list[i] + " "
            else:
                my_string += my_list[i]

        return my_string


def remove_duplicates_from_string(s):
    """Remove duplicates from a string"""
    if s == "":
        return ""
    
    my_string = ""

    for char in s:
        if char not in my_string:
            my_string += char

    return my_string

# print(remove_duplicates_from_string("abcabc"))

def merge_sorted_arrays(arr1, arr2):
    """Merge two sorted arrays into one sorted array"""
    pass
def intersection_of_arrays(arr1, arr2):
    """Return the intersection (common elements) of two arrays"""
    pass

def reverse_words(s):
    """Reverse the words in a string"""
    pass

def remove_duplicates_from_string(s):
    """Remove duplicate characters from a string"""
    pass

def is_palindrome(s):
    """Check if a string is a palindrome"""
    lower_string = s.lower().replace(" ", "")
    my_list = []
    my_string = ""

    for char in lower_string:
        my_list.append(char)

    my_list.reverse()
    for char in my_list:
        my_string += char

        if lower_string == my_string:
            return True
    
    return False


def move_zeros(arr):
    """Move all zeros to the end of an array"""
    for number in arr:
        if number == 0:
            arr.remove(number)
            arr.append(number)

    return arr


def reverse_integer(n):
    """Reverse an integer"""
    number_string = str(n)
    my_list = []
    reverse_string_integer = ""

    for i in range(len(number_string)):
        if number_string[i] == "-":
            continue
        elif isinstance(int(number_string[i]), int):
            my_list.append(number_string[i])

    my_list.reverse()
    if number_string[0] == "-":
        my_list.insert(0, number_string[0]) 
        print(my_list)

    for char in my_list:
        reverse_string_integer += char

    return int(reverse_string_integer)


def longest_substring_without_repeating(s):
    """Find the length of the longest substring without repeating characters"""
    count = 0
    my_list = []
    longest_count = 0

    for i in range(len(s)):
        if s[i] not in my_list:
            my_list.append(s[i])
            count += 1
            # print(my_list)
            # print(count)
        else:
            longest_count = len(my_list)
            count = 0
            my_list.clear()
            my_list.append(s[i])

    return longest_count
    
# print(longest_substring_without_repeating("abcabcbb"))

def is_anagram(s1, s2):
    """Check if two strings are anagrams"""
    count = 0
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] in s2:
                count += 1   

    if count == len(s1):
        return True
    return False


def find_missing_number(arr):
    """Find the missing number in an array"""
    pass


def remove_duplicates_from_sorted_array(arr):
    """Remove duplicates from a sorted array"""
    pass
def search_insert_position(arr, target):
    """Find the position to insert the target in a sorted array"""
    pass

def max_subarray_sum(nums):
    """Find the maximum sum of a subarray"""
    pass

def str_str(haystack, needle):
    """Return the index of the first occurrence of needle in haystack"""
    pass

def count_and_say(n):
    """Generate the nth term of the count-and-say sequence"""
    pass

def climbing_stairs(n):
    """Find the number of distinct ways to reach the top of a staircase"""
    pass

def two_sum(nums, target):
    """Find two numbers in the list that add up to a target sum"""
    pass

def is_valid_parentheses(s):
    """Check if the parentheses in a string are valid"""
    pass