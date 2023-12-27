import time

start = time.time()

def count_divisors(n):
    count = 1
    i = 2
    
    while i * i <= n:
        exponent = 0
        while n % i == 0:
            n //= i
            exponent += 1
        count *= (exponent + 1)
        
        i += 1
    
    if n > 1:
        count *= 2
        
    return count
    
def get_triangular_number(n):
    return (n * (n + 1)) // 2
 
n = 1   
    
while True:
    number = get_triangular_number(n)
    count = count_divisors(number)
    if count > 2000:
        print(number)
        break
    
    n += 1
    
    if n % 1000 == 0:
        print(number)
    
      
print(f'Time Taken: {time.time()-start}')