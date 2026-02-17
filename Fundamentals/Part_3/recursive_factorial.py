def factorial(arr, i):
    if i == len(arr) - 1:
        return arr[i]
    return arr[i] * factorial(arr, i + 1)

num = int(input())
arr = [int(x) for x in range(1, num + 1)]

print(factorial(arr, 0))

# finds the sum of all elements in an integer array. Use recursion