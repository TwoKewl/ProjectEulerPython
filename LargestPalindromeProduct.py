import time

start = time.time()

def palindrome(num):
    x = str(num)
    x = x[::-1]
    
    if x == str(num):
        return True
    
maximum = 0

for a in range(1000):
    for b in range(1000):
        if palindrome(a*b):
            if maximum < a * b:
                maximum = a * b
                print(f'{a}x{b}={maximum}')
                
print(f'Time Taken: {time.time()-start}s')