def array_sum(arr, i):
    if i == len(arr) - 1:
        return print("*" * i)
    return arr[i] + array_sum(arr, i + 1)

arr = [int(x) for x in input().split()]

print(array_sum(arr, 0))

# finds the sum of all elements in an integer array. Use recursion