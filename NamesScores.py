alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

names = open('names.txt', 'r').read()
names = names.split('","')
names = sorted(names)

i = 1
total_sum = 0

for name in names:
    name_sum = 0
    for l in name:
        for a in range(len(alphabet)):
            if alphabet[a] == l:
                name_sum += a + 1
                      
    name_sum *= i
    i += 1
    total_sum += name_sum
    
print(total_sum)