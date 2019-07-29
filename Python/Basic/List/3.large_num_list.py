# Write a Python program to get the largest number from a list.


def largest_num_in_list(items):
    max = items[0] 
    for i in items:
        if i > max:
            max = i
    return max

l = [3, 4, 9, 1, 12]
print(largest_num_in_list(l))
