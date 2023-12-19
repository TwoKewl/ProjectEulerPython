file = open('triangle.txt', 'r')
tri = file.read()

a = tri.split("\n")

triangle = [ ]

for i in a:
    b = i.split(" ")
    triangle.append(b)
    
triangle.pop(-1)    
    
while len(triangle) != 1:
    last = triangle[-1]
    sec_last = triangle[-2]
    
    for i in range(len(sec_last)):
        a = int(last[i])
        b = int(last[i + 1])
        
        sec_last[i] = int(sec_last[i])
        sec_last[i] += max(a, b)
        
    triangle.pop(-1)

print(triangle[0][0])