import time
import math

start = time.time()

num = 600851475143

def get_primes():
    primes = [2]
    number = 2
    
    for j in range(math.ceil(math.sqrt(num))):
        for i in primes:
            if math.sqrt(i) > number:
                prime = False
                break
            
            if number % i == 0:
                prime = False
                break
            else:
                prime = True
            
        if prime == True:
            primes.append(number)
        
        number += 1
        
    print(f'Time Taken: {time.time()-start}s')
    return primes

def divide(number, divisor):
    if number % divisor == 0:
        print(divisor)
        return divisor
    else:
        return -1


primes = get_primes()


for p in primes:
    divide(num, p)