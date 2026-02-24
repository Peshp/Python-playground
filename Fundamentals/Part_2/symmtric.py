list1 = [101, 102, 103]
list2 = [103, 104, 105]

elements = []

for i, x in enumerate(list1):
    if x not in list2:
        elements.append(x)

for i, x in enumerate(list2):
    if x not in list1:
        elements.append(x)

print(elements)

# Given two lists of student IDs, find the IDs that appear in either the first or the second list, but not in both.

def get_exclusive_ids(ids1, ids2):
    set1 = set(ids1)
    set2 = set(ids2)
    
    # Symmetric difference
    return set1 ^ set2

january_visitors = [10, 20, 30, 40]
february_visitors = [30, 40, 50, 60]

exclusive = get_exclusive_ids(january_visitors, february_visitors)
print(f"{exclusive}")