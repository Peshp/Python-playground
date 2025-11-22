import math

tournaments = int(input())
begin_points = int(input())
all_points = 0
wins = 0

for i in range(tournaments):
    stage_of = input()
    if stage_of == "F":
        all_points += 1200
    elif stage_of == "W":
        wins += 1
        all_points += 2000
    else:
        all_points += 720

average_points = all_points / tournaments
percent_wins = wins / tournaments * 100

print(f"Final: {all_points + begin_points}")
print(f"Average: {math.floor(average_points)}")
print(f"{percent_wins:.2f}%")