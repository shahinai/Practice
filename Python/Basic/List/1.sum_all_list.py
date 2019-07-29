# Write a Python program to sum all the items in a list.


def sum_list(items):
    sum_num = 0
    for x in items:
        sum_num += x
    return sum_num

print(sum_list([4, 5, -2, 6]))
