dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

def merge(dict1, dict2):
    common = 'a'
    output = dict()
    for i, (key, val) in enumerate(dict1.items()):
        if(common != key):
            common = key
            output[key] = val
        else:
            output[key] = val
    for i, (key, val) in enumerate(dict2.items()):
        if(common == key):
            output[key] += val
        else:
            output[key] = val
    
    print(output)
            
merge(dict_a, dict_b)

# Write a function that merges two dictionaries. 
# If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.

def merge_two(dict1, dict2):
    result = dict1.copy()

    for key, val in dict2.items():
        result[key] = result.get(key, 0) + val

    return result

output = merge_two(dict_a, dict_b)
print(output)