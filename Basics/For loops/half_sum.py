n = int(input())
sum = 0
biggest = 0

for x in range(n):
    num = int(input())
    if num >= biggest:
        biggest = num
    sum += num

if sum - biggest == biggest:
    print(f"Yes \nSum = {sum - biggest}")
else:
    sum -= biggest
    print(f"No \nDiff = {abs(biggest - sum)}")
