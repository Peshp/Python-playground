tournaments = int(input())
beginning = int(input())

winning = 0
points = beginning

for x in range(tournaments):
    text = input()
    if text == "W":
        winning += 1
        points += 2000
    elif text == "F":
        points += 1200
    elif text == "SF":
        points += 720

print(f"Final points: {points} \nAverage points: {(points - beginning) / tournaments}\n {winning / tournaments * 100}%")