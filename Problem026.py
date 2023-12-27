from decimal import getcontext, Decimal

getcontext().prec = 5000

def check_rec(float):
    digits = list(str(float))
    a = digits.index('.')
    
    for i in range(a+1):
        digits.pop(0)
    
    for i in range(1, 1000):
        for j in range(1, 100, i):
            a = digits[j-1:j+i-1]
            b = digits[j+i-1:j+2*i-1]
            c = digits[j+2*i-1:j+3*i-1]
            d = digits[j+3*i-1:j+4*i-1]

            if a == b == c == d:
                return True
                
            break

    return False

def len_rec(float):
    digits = list(str(float))
    a = digits.index('.')
    
    for i in range(a+1):
        digits.pop(0)
    
    for i in range(1, 1000):
        for j in range(1, 100, i):
            for k in range(i+1):
                a = digits[j-1+k:j+i-1+k]
                b = digits[j+i-1+k:j+2*i-1+k]
                c = digits[j+2*i-1+k:j+3*i-1+k]
                d = digits[j+3*i-1+k:j+4*i-1+k]

                if a == b == c == d:
                    return len(a)

                
            break

    return 0

vals = [0]
largest = 0

for d in range(2, 1001):
    if check_rec(Decimal(1) / Decimal(d)):
        print(f'1 / {d} is Recurring, {len_rec(Decimal(1) / Decimal(d))} digits long.')
        
        if len_rec(Decimal(1) / Decimal(d)) > largest:
            largest = len_rec(Decimal(1) / Decimal(d))
            term = d
            
print(f'Longest recurring decimal: {largest}, D = {term}')