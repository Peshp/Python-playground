a = int(input())
b = int(input())
h = int(input())
percent = float(input()) / 100

v = a * b * h
sum = v - (v * percent)
result = sum / 1000
print(result)