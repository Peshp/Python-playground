def bit(arr, id):
    if all(x == 1 for x in arr):
        print(''.join(map(str, arr)))  # Print the final vector
        return arr
    
    # Print current state
    print(''.join(map(str, arr)))
    
    if arr[id] == 1:
        return bit(arr, len(arr) - 1)
    if id + 1 < len(arr):
        arr[id + 1] = 0
    arr[id] = 1
    return bit(arr, id - 1)


num = int(input())
arr = "0" * num
arr = [int(x) for x in arr]

bit(arr, len(arr) - 1)

