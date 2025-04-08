searched = input()

book = ""
count = 0

while book != searched and book != "No More Books":
    book = input()
    count += 1
    
if book == searched:
    print(f"You checked {count} books and found it")
    count -= 1
else:
    count -= 1
    print("The book you search is not here")
    print(f"You checked {count} books.")
    
        
    