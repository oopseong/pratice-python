high = 100
bounce = 3 / 5
i = 1

while i <= 10:
    high = high * bounce
    print(i, round(high, 4))
    i = i + 1