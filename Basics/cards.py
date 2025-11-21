name_first = input()
name_second = input()
points_first = 0
points_second = 0

command = ""
while command != "End of game":
    command = input()
    if command == "End of game":
        break
    card_first = int(command)
    card_second = int(input())

    if card_first > card_second:
        points_first += card_first - card_second
    elif card_second > card_first:
        points_second += card_second - card_first
    else:
        card_first = int(input())
        card_second = int(input())
        if card_first > card_second:
            print("Number wars!")
            print(f"{name_first} is win points: {points_first}")
        elif card_second > card_first:
            print(f"{name_second} is win points: {points_second}")
        
        break

if command == "End of game":
    if points_first > points_second:
        print(f"{name_first} is win points: {points_first}")
    else:
        print(f"{name_second} is win points: {points_second}")

        

