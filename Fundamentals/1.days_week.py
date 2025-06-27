
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

num = int(input())
found = False

for i in range(1, 8):
    if num == i:
        print(days[i - 1])
        found = True
        break

if not found:
    print("Invalid day!")