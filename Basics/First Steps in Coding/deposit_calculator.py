deposit = float(input())
month = int(input())
percent = float(input()) / 100

result = deposit + month * ((deposit * percent) / 12)
print("%.2f" % round(result, 2))