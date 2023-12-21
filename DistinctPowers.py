
orig_vals = []

for b in range(2, 101):
    for a in range(2, 101):
        orig_vals.append(a**b)
        
new_vals = []
    
for i in orig_vals:
    if i not in new_vals:
        new_vals.append(i)
        
print(len(new_vals))