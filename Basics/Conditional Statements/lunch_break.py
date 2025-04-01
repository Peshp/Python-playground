import math


series = input()
episode = int(input())
time = int(input())

lunch = time / 8
rest = time / 4

result = time - (lunch + rest)

if result >= episode:
    print(f'You have enough time to watch {series} and left with {round(result - episode)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(episode - result)} more minutes.")