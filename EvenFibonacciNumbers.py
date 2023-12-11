import time

start = time.time()

def get_fib_nums():
    nums = []

    a = 0
    b = 1

    while True:
        ans = a + b
        a = b
        b = ans
        
        if ans > 4000000:
            break
        if ans % 2 == 0:
            nums.append(ans)
    
    
    
    return nums

print(sum(get_fib_nums()))
print(f'Time Taken: {time.time()-start}s')