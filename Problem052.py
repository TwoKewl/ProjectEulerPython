import time

i = 1


while True:
    n = list(str(i))
    
    for a in range(1, 7):
        for b in list(str(a*i)):
            if b in n:
                p = True
            else:
                p = False
                break
            
        if p == False:
            break
        
    i += 1
    
    if p:
        print(n)
        break