def figure(num):
    if num <= 0:
        return
    print("*" * num)
    figure(num - 1)
    print("0" * num)

2num = int(input())

figure(num)

# calculates the recursively factorial of a given number.