cinema = input()
rows = int(input())
cols = int(input())

result = rows * cols

if cinema == "Premiere":
    result *= 12
elif cinema == "Normal":
    result *= 7.5
else:
    result *= 5

print("%.2f" % round(result, 2))