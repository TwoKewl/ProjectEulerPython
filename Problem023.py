import math

def find_divisors(n):
    divisors = []
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)

    if n in divisors:
        divisors.remove(n)
    
    return sorted(list(set(divisors)))

def check_abundant(n):
    return n < sum(find_divisors(n))

abundant_nums = []
for i in range(12, 28123):
    if check_abundant(i):
        abundant_nums.append(i)

abundant_sums = []
for a in abundant_nums:
    for b in abundant_nums:
        abundant_sum = a + b
        if abundant_sum > 28123:
            break
        else:
            abundant_sums.append(abundant_sum)

abundant_sums = list(set(abundant_sums))
non_abundant_nums = []

for i in range(28124):
    if i not in abundant_sums:
        non_abundant_nums.append(i)
        
print(sum(non_abundant_nums))