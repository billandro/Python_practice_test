
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

def longest_word_in_sentence(sentence):
    """Return the longest word in a sentence"""
    longest_word = 0
    words = sentence.split(" ")
    the_index = 0
    j = len(words) - 1
    count = 0

    while len(words[j]) == 1:
        count += 1
        if count == len(words):
            return words[-1]

    for i in range(len(words)):
        if len(words[i]) > longest_word:
            longest_word = len(words[i])
            the_index = i

    return words[the_index]


# print(longest_word_in_sentence("Quick"))