import math

primes = [2]
num = 2


while num < 2000000:
    for i in primes:
        if num % i == 0:
            prime = False
            break
        else:
            prime = True
            
        if i > math.sqrt(num):
            break
            
    if prime == True:
        primes.append(num)
        
    num += 1 
    if num % 1000 == 0:
        print(primes)

print(sum(primes))