import time

start = time.time()

a, b, c = 1, 2, 3

while True:
    if a + b + c == 1000 and a*a + b*b == c*c:
        print(f'{a} + {b} + {c} = {a+b+c}')
        print(f'Time Taken: {time.time()-start}s')
        break
        
    a += 1
    
    if a == b:
        b += 1
        a = 1
    if b == c:
        c += 1
        b = 2
    