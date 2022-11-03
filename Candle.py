max=0

for i in candles:
    if i > max:
        max=i

print(candles.count(max))
