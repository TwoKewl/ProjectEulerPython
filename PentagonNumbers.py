

def get_pentagon():
    vals = []
    for n in range(1,10001):
        vals.append(n*(3*n-1)//2)
        
    return vals

vals = get_pentagon()

for val1 in vals:
    for val2 in vals:
        if abs(val1 - val2) in vals and val1 + val2 in vals:
            print(abs(val1-val2))