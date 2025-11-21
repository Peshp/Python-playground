wins = losses = draws = 0

for _ in range(3):
    line = input().strip()
    if not line:
        continue
    parts = line.split(':')
    home = int(parts[0])
    away = int(parts[1])
    if home > away:
        wins += 1
    elif home < away:
        losses += 1
    else:
        draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")
    
