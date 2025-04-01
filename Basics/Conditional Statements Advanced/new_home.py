flower = input()
count = int(input())
budget = float(input())

price = 0
match flower:
    case "Roses":
        price = 5.00 * count
    case "Dahlias":
        price = 3.8 * count
    case "Tulips":
        price = 2.8 * count
    case "Narcissus":
        price = 3.0 * count
    case "Gladiolus":
        price = 2.5 * count

if flower == "Roses" and count > 80:
    price -= price * 0.1
elif flower == "Dahlias" and count > 90:
    price -= price * 0.15
elif flower == "Tulips" and count > 80:
    price -= price * 0.15
elif flower == "Narcissus" and count < 120:
    price += price * 0.15
elif flower == "Gladiolus" and count < 80:
    price += price * 0.2

result = price - budget

if(budget >= price):
    print(f"Hey, you have a great garden with {count} {flower} and {'%.2f' % round(result, 2)} leva left.")
else:
    print(f"Not enough money, you need {abs(result)} leva more.")