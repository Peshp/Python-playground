days = int(input()) - 1
room = input()
grade = input()

price = 0;
match room:
    case "apartment":
        price = 25.0 * days
        if days < 10:
            price -= price * 0.3
        elif days > 10 and days < 15:
            price -= price * 0.35
        elif days > 30:
            price -= price * 0.5
    case "president apartment":
        price = 35.0 * days
        if days < 10:
            price -= price * 0.1
        elif days > 10 and days < 15:
            price -= price * 0.15
        elif days > 30:
            price -= price * 0.2
    case "room for one person":
        price = 18.0 * days

match grade:
    case "positive":
        price += price * 0.25
    case "negative":
        price -= price * 0.1

print("%.2f" % round(price, 2))
