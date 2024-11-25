import statistics
def compute_standard_deviation(numbers):
    """Compute the standard deviation of a list of numbers"""
    if numbers == []:
        return None
    return statistics.stdev(numbers)

# print(compute_standard_deviation([1, 2, 3, 4, 5]))

def find_second_largest(numbers):
    """Find the second largest number in a list"""
    numbers.sort()
    dict = {}

    the_count = numbers.count(numbers[0])
    if the_count == len(numbers):\
        return None

    for number in numbers:
        if number not in dict:
            dict[number] = 1
        else:
            dict[number] += 1

    my_list = []
    for key, value in dict.items():
        my_list.append(key)
    
    return my_list[-2]


def character_frequency_per_word(sentence):
    """Return a dictionary of character frequencies for each word in a sentence"""
    dict = {}
    my_list = sentence.split(" ")
    
    for i in range(len(my_list)):
        if my_list[i] not in dict:
            dict[my_list[i]] = {}

    for key, value in dict.items():
        for letter in key:
            if letter not in value:
                dict[key][letter] = 1
            else:
                dict[key][letter] += 1

    return dict


def check_palindrome(numbers):
    """Check if a list of numbers is a palindrome"""
    my_list = []
    for number in numbers:
        my_list.append(number)

    numbers.reverse()
    if numbers == my_list:
        return True
    return False


def longest_word_in_sentence(sentence):
    """Return the longest word in a sentence"""
    longest_word = 0
    words = sentence.split(" ")
    the_index = 0
    for i in range(len(words)):
        if len(words[i]) > longest_word:
            longest_word = len(words[i])
            the_index = i

    return words[the_index]


def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into one sorted list"""
    x = sorted(list1)
    y = sorted(list2)
    return sorted(x + y)


def find_intersection(list1, list2):
    """Find the intersection (common elements) of two lists"""
    list3 = []

    for x in list1:
        for y in list2:
            if x ==y:
                list3.append(x)
    
    return list3

def nth_fibonacci(n):
    """Calculate the nth Fibonacci number using both recursion and iteration"""
    if n <= 0:
        return n
    if n <= 1:
        return n
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)

def reverse_words_in_sentence(sentence):
    """Reverse the words in a sentence while maintaining word order"""
    my_list = sentence.split()
    my_list.reverse()
    the_sentence = ""
    
    for i in range(len(my_list)):
        if i != len(my_list) - 1:
            the_sentence += my_list[i] + ' '
            continue
        the_sentence += my_list[i]

    return the_sentence


def unique_characters_in_string(s):
    """Return all unique characters in a string"""
    new_string = ""
    my_list = []
    for char in s:
        if char not in my_list:
            my_list.append(char)

    my_list.sort()
    for char in my_list:
        new_string += char

    return new_string