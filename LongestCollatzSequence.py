i = 1

highest_count = 0

while i <= 1000000:
    num = i
    count = 0
    
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = num * 3 + 1
            count += 1
            
    if highest_count < count:
        highest_count = count
        print(highest_count, i)
        
    
    
    i += 1
        