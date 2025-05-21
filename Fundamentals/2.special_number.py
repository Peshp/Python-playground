number = int(input())

for i in range(1, number + 1):
    sum = 0
    for digit in str(i):
        sum += int(digit)
    print(f"{i} -> {sum == 5 or sum == 7 or sum == 11}")
    
    


    