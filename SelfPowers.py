sum = 0

for i in range(1, 1001):
    sum += i**i

last_10 = int(str(sum)[-10:])

print(last_10)