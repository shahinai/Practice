# Write a Python program to multiplies all the items in a list


def multiple_list(items):
    mul = 1
    for x in items:
        mul *= x
    return mul

print(multiple_list([1,2,3]))
