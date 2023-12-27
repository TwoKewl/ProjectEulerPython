
# UL = 4n^2-6n+3
# UR = 4n^2-4n+1
# DR = 4n^2-10n+7
# DL = 4n^2-8n+5

s = 1

for n in range(2, 502):
    s += 4*n**2 - 6*n + 3
    
for n in range(2, 502):
    s += 4*n**2 - 4*n + 1
    
for n in range(2, 502):
    s += 4*n**2 - 10*n + 7

for n in range(2, 502):
    s += 4*n**2 - 8*n + 5
    
print(s)