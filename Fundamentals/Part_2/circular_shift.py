def rotate_list(items, m, d):
    if not isinstance(items, list): return items

    m = m % len(items)

    for i in range(m + 1):
        element = items[0]
        items.remove(element)
        items.append(element)

    if d == 'right': return items 
    elif d == 'left': return items[::-1] # [start;end;step]

print(rotate_list([1, 2, 3, 4, 5], 10, 'right'))

# Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. 
# The direction can be ‘left’ or ‘right’.