pencils = int(input())
pens = int(input())
litres = int(input())
discount = int(input())

sum = pencils * 5.8 + pens * 7.2 + litres * 1.2
result = sum - (sum * (discount / 100))

print(result)