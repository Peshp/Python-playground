teams = input().split()
team_a = 11
team_b = 11
terminated = False

for team in teams:
    player = team.split("-")
    if player[0] == "A":
        team_a -= 1
    elif player[0] == "B":
        team_b -= 1
    if team_a < 7 or team_b < 7:
        terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if terminated:
    print("Game was terminated")
