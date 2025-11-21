price = float(input())

priceBoots = price - (price * 0.4)
priceDress = priceBoots - (priceBoots * 0.2)
priceBall = priceDress / 4
priceAll = priceBall / 5
result = priceBoots + priceDress + priceBall + priceAll + price

print(f"{result:.2f}")