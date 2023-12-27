number = 1

running = True

while running:
    number += 1
    
    for i in range(2, 16):
        if i == 10:
            running = False
        if number % (16-i) != 0:
            break
    
    if number % 1000000 == 0:
        print(number)
    
print(number)