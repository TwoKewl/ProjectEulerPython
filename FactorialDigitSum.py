import math
number = math.factorial(100)
number = str(number)
sums = 0
for digit in number:
    sums += int(digit) 
print(sums)