numbers = list(map(int, input().split()))

def change(parts):
    if parts[0] == "Delete":
        number = int(parts[1])
        numbers[:] = [n for n in numbers if n != number]

while True:
    command = input()
    if command == 'end':
        break

    parts = command.split()
    if parts[0] == "Delete":
        change(parts)
    elif parts[0] == "Insert":
        index = int(parts[1])
        value = int(parts[2])
        numbers.insert(index, value)

print(' '.join(map(str, numbers)))