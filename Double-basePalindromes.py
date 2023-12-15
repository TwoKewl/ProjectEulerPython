
def binary(x):
    return int(bin(x)[2:])

s = 0

for i in range(1, 1000001):
    a = list(str(i))
    
    
    if a == a[::-1] and list(str(binary(i))) == list(str(binary(i)))[::-1]:
        s += i
        
print(s)