racket = float(input())
count = int(input())
boots = int(input())

priceRacket = count * racket
priceBoots = racket / 6
priceAll = boots * priceBoots
price = (priceRacket + priceAll) * 0.2
result = priceRacket + priceAll + price

print(f"Price to be paid by Djokovic {result/8:.2f}")