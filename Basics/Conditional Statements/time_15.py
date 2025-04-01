minutes = int(input())
seconds = int(input())

seconds += 15
if seconds > 59:
    minutes += 1
    seconds -= 60
if minutes > 23:
    minutes = 0

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
