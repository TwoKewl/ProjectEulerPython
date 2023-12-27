import time

start = time.time()

a = 0
b = 0

for i in range(1, 101):
    a += i * i
    

for j in range(1, 101):
    b += j
b *= b

print(b - a)
print(f'Time Taken: {time.time()-start}s')