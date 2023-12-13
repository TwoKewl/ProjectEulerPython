
am_numbers = []

def d(number):
    divisors = []
    
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    
    for i in divisors:
        if i == max(divisors):
            divisors.remove(i)
            break
           
    divisors = sorted(divisors)
    
    return sum(divisors)

s = 0

for a in range(1, 10001):
    b = d(a)
    if a == d(b):
        if a != b:
            print(a)
            s += a
            
print(s)