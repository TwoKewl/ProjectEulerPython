
def trunc_left(num):
    a = list(str(num))
    a.pop(0)
    b = ''.join(map(str, a))
    return b

def trunc_right(num):
    a = list(str(num))
    a.pop(len(a)-1)
    b = ''.join(map(str, a))
    return b

def get_next(prime_list):
    nums = [int(x) for x in prime_list]
    a = len(prime_list)
    i = max(nums) + 1
    
    while len(prime_list) == a:
        prime = True
        for p in nums:
            if i % p == 0:
                prime = False
                break
            else:
                prime = True
        
        if prime:
            prime_list.append(str(i))
            
        i += 1
    
    return prime_list

primes = ['2', '3', '5', '7', '11']

trunc_primes = []

j = 0

while len(trunc_primes) != 11:
    nums = [int(x) for x in primes]
    a = max(nums)
    
    for i in range(len(str(a)) - 1):
        a = trunc_left(a)
        
        if a not in primes:
            trunc_l = False
            break
        else:
            trunc_l = True
    
    trunc_r = False
    
    if trunc_l:
        a = max(nums)
        
        for i in range(len(str(a)) - 1):
            a = trunc_right(a)
            
            if a not in primes:
                trunc_r = False
                break
            else:
                trunc_r = True
           
         
    if trunc_r:
        trunc_primes.append(max(nums))
        print(max(nums))
    
    get_next(primes)
    j += 1

print(f'Sum: {sum(trunc_primes)}')