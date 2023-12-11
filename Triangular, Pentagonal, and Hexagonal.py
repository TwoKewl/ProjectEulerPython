import time

def get_triangle():
    
    tri = []    
    
    for i in range(1, 100001):
        tri.append(i*(i+1)//2)
        
    return tri

def get_pentagonal():
    
    pent = []
    
    for i in range(1, 100001):
        pent.append(i*(3*i-1)//2)
        
    return pent
        
def get_hexagonal():
    
    hexa = []
    
    for i in range(1, 100001):
        hexa.append(i*(2*i-1))

    return hexa

p = get_pentagonal()
h = get_hexagonal()

for t in get_triangle():
    if t in p:
        if t in h:
            print(t)