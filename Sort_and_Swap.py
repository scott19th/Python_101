# Python Coding Challenge - Sort and Swap

# sort the unsorted list and swap the 2nd largest / smallest numbers

unsorted_list1 = [8, 7, 22, 16, 3, 24, 56, 17, 23, 6, 72]


def list_sorter(unsorted_list):
    sorted_list = sorted(unsorted_list)
    second_largest_number = sorted_list.pop(-2)
    sorted_list.insert(1, second_largest_number)
    second_smallest_number = sorted_list.pop(2)
    sorted_list.insert(-1, second_smallest_number)
    print(sorted_list)


list_sorter(unsorted_list1)
