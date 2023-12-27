import math

def get_primes():
    count = 2
    primes = []
    for i in range(1, 1000001):
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            primes.append(count)
        
        count += 1
    
    print("func done")
    return primes

def to_back(lst, indx):
    a = lst[indx]
    lst.pop(indx)
    lst.append(a)
    return lst
    
primes = get_primes()

circ_primes = 0

for p in primes:
    a = list(str(p))
    
    for b in range(len(a)):
        
        if int(''.join(map(str, a))) in primes:
            r = True
        else:
            r = False
            break
            
        to_back(a, 0)
        
    if r == True:
        circ_primes += 1
        
print(circ_primes)
print(len(primes))