number = int(input())
guests = []

for _ in range(n):
    command = input().strip()
    if command.endswith(" is going!"):
        name = command[:-len(" is going!")]
        if name in guests:
            print(f"{name} is already in the list!")
        else:
            guests.append(name)
    elif command.endswith(" is not going!"):
        name = command[:-len(" is not going!")]
        if name in guests:
            guests.remove(name)
        else:
            print(f"{name} is not in the list!")

# Print final guest list, each on a new line
for guest in guests:
    print(guest)
        
    