def duplicated(arr):
    elements = []
    for el in arr:
        if el in elements:
            arr.remove(el)
            continue

        elements.append(el)
    
    return sorted(arr)

print(duplicated([1, 2, 2, 3, 1, 4, 2]))

# Write a function that removes duplicate elements from a list. 