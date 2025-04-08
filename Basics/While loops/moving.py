a = int(input())
b = int(input())
h = int(input())

v = a * b * h
boxes = input()

while True:
    if v > 0 and boxes == "Done":
        print(f"{v} Cubic meters left.")
        break
    elif v <= 0:
        print(f"No more free space! You need {abs(v)} Cubic meters more.")
    v -= int(boxes)
    boxes = input()
    

    
    