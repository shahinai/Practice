# Write a Python program to get the smallest number from a list.


def small_number_in_list(items):
    low = items[0]
    for i in items:
        if i < low:
            low = i
    return low

print(small_number_in_list([8, 3, 5, 2, 9]))
