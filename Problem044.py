import time

vals = []

def p_list(list, count):
    for i in range(count):
        list.append(p(i+1))
    print("func done")
    return list

def p(n):
    return n*(3*n-1)//2


p_list(vals, 10000)

r = True

while r:
    for j in vals:
        for k in vals:
            if k + j in vals:
                print(f'{j} - {k} = {j - k}')
                if j - k in vals:
                    print(j - k)
                    exit()
            if k > j:
                break
            