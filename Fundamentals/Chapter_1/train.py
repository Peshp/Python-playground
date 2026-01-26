wagons = list(map(int, input().split()))
max_capacity = int(input())

while True:
    command = input()
    if command == "end":
        break

    parts = command.split()

    if parts[0] == "Add":
        wagons.append(int(parts[1]))
    else:
        passengers = int(parts[0])
        for i in range(len(wagons)):
            if wagons[i] + passengers <= max_capacity:
                wagons[i] += passengers
                break

print(' '.join(map(str, wagons)))
    

