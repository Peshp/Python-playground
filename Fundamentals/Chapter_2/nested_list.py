
new_a = []
def new_array(arr):
    for i, val in enumerate(arr):
        if isinstance(val, list):
            new_array(val)
        else:
            new_a.append(val)
    return new_a

nested = [1, [2, 3], [4, [5, 6]], 7]
print(new_array(nested))

# Write a recursive function that takes a list containing other 
# lists (of any depth) and returns a single “flat” list of all elements.