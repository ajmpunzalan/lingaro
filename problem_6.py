# What could go wrong about this code?

def sort(iterable):
    return sorted(iterable, key=lambda x: try:  x[1])

# This will throw an IndexError Exception if your iterable input is less than 2 because of the hardcoded index - 1
# Example:
# print(sort([[3], [2], [1]]))
# print(sort([['a'], ['b'], ['c']]))
