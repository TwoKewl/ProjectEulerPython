import time

start = time.time()

primes = [2]
num = 2

while len(primes) <= 10001:
    for i in range(len(primes)):
        if num % primes[i] == 0:
            prime = False
            break
        else:
            prime = True
            
    if prime == True:
        primes.append(num)
        
    num += 1
    

print(primes[10000])
print(f'Time Taken: {time.time()-start}s')