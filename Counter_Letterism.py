# Python Coding Challenge - Counter Letterism

string = "Alright, but  apart from the sanitation, the medicine, education, wine, public order, irrigation, roads, the fresh-water system, and public health, what have the Romans ever done for us?"


def non_vowel_non_space_counter(statement):
    count = 0
    vowels_and_spaces = ('a', 'e', 'i', 'o', 'u', ' ')
    for x in statement:
        if x.lower() not in vowels_and_spaces:
            count += 1
    print(f'This string countains {count} non space, non vowel characters.')

# original jpeg of challenge states 102 in the answer but publisher confirmed true result is 101


non_vowel_non_space_counter(string)

# Bonus Challenge - count instances of non vowel and non space letters


def character_and_vowel_counter(statement):
    statement_list = []
    count_dictionary = {}
    vowels_and_spaces = ('a', 'e', 'i', 'o', 'u', ' ')
# sort string into a list of relevent letters
    for x in statement:
        if x.lower() not in vowels_and_spaces:
            statement_list.append(x.lower())

# sort list of letters into a dictionary key value pairs, where values is the count
    for x in statement_list:
        if x in count_dictionary:
            count_dictionary[x] += 1
        else:
            count_dictionary[x] = 1

# iterate over sorted dictionary and print
    for x, count in sorted(count_dictionary.items(), key=lambda item: item[1], reverse=True):
        print(f'{x} : {count} times')


character_and_vowel_counter(string)
