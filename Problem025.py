
def fib():
    fibs = [0, 1]
    i = 1
    
    while len(str(fibs[1])) < 1000:
        i += 1
        fibs.append(fibs[0] + fibs[1])
        fibs.pop(0)
    
    return i

print(fib())