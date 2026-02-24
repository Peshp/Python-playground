a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

is_subset = set(a).issubset(b)
is_superset = set(a).issuperset(b)

print(is_subset)
print(is_superset)

# Write a script that takes two lists of integers from a user, 
# converts them to sets, and determines if the first set is a Subset, a Superset, or Disjoint from the second.