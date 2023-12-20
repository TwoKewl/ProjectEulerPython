def frac(num, den):
    
    numer = list(str(num))
    denom = list(str(den))    
  
    for n in numer:
        if n in denom:
            if n != 0:
                numer.remove(n)
                denom.remove(n)
                    
                numer = int(''.join(map(str, numer)))
                denom = int(''.join(map(str, denom)))
                
                return num/den == numer/denom
            
    return False

def get_divisors(number):
    divisors = []
    
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
                
    divisors = sorted(divisors)
    
    return divisors

def simplify(numerator, denominator):
    a = get_divisors(numerator)
    b = get_divisors(denominator)
    
    for i in a:
        if i in b:
            highest = i
            
    numerator //= highest
    denominator //= highest
    
    return [numerator, denominator]

def product(lst):
    a = 1
    
    for i in lst:
        a *= i
        
    return a
    
nums, dens = [], []

for d in range(10, 100):
    for n in range(10, 100):
        
        if n > d:
            break
        
        if n % 10 == 0 or d % 10 == 0 or n == d:
            pass
        else:
            if frac(n, d):
                nums.append(n)
                dens.append(d)
    
denominators = []
numerators = []
           
for i in range(len(dens)):
    numerators.append(simplify(nums[i], dens[i])[0])
    denominators.append(simplify(nums[i], dens[i])[1])

print(product(denominators) // product(numerators))