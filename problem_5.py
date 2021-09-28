# What's wrong with this code?
# def (x, l=[]):
#     for i in range(x):
#         l.append(i*i)
#     return l

# 1. There is no function name
# 2. Assigining an empty list/mutable object as a default argument for l. This would reference the same mutable object after the first function call.
# Example:
# print(func(1))
# print(func(1))
# print(func(1))
# Output:
# [0]
# [0, 0]
# [0, 0, 0]
# As a best practice we should not be assigning mutable objects as a default argument in our functions. Instead set it to None:


def func(x, l=None):
    if l is None:
        l = []
    for i in range(x):
        l.append(i*i)
    return l


# print(func(1))
# print(func(1))
# print(func(1))
# Output:
# [0]
# [0]
# [0]
