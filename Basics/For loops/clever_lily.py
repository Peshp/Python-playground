age = int(input())
price = float(input())
toy = int(input())

money = 0

for x in range(1, age + 1):
    if x % 2 != 0:
        money += toy
    else:
        money += (10 * (x / 2)) - 1

if money >= price:
    print(f"Yes! {money - price}")
else:
    print(f"No! {price - money}")
    