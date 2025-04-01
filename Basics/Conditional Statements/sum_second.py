import math


first = int(input())
second = int(input())
third = int(input())

sum = first + second + third
seconds = sum % 60
minutes = sum / 60

if seconds < 10:
    print(f'{math.floor(minutes)}:0{seconds}')
else:
    print(f'{math.floor(minutes)}:{seconds}')

