
def power(number):
    lst = []
    s = 0
    
    for nums in str(number):
        lst.append(int(nums))
    
    for vals in lst:
        s += vals**5
        
    if s == number:
        return True
        
    return False

i = 1
s = 0

while True:
    i += 1
    if power(i):
        s += i
        print(f'{i}, New sum: {s}')