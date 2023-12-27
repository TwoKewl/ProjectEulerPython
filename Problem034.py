import math
import time

start = time.time()



def check(number):
    s = 0
    
    for i in str(number):
        s += math.factorial(int(i))
    
    if s == number:
        return True
    return False
        
s = 0
i = 0

for i in range(5, 100000000):

    if check(i) == True:
        print(i)
        s += i
        
print(s)
print(f'Time Taken: {time.time()-start}')