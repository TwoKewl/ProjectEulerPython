num = 2**1000
num = str(num)
sums = 0
length = 0
for digit in num:
    sums += int(digit)
    length += 1
print(sums)
print(f'Length = {length}')