rate = input("What is the current exchange rate from a Euro to a Dollar? ")
rate = float(rate)
amount = input("What is the amount of currency you want to exchange? ")
amount = float(amount)
total = amount * rate
result = total - 3.00
print(result)