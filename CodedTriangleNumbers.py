
def get_triangle():
    vals = []
    for n in range(1, 101):
        vals.append((1/2)*n*(n+1))
    return vals
    
nums = get_triangle()
        
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

file = open('ProjectEuler\\words.txt', 'r')
words = file.read().split(',')

triangle_words = 0

for word in words:
    word_sum = 0
    for l in word:
        for a in range(len(alphabet)):
            if alphabet[a] in l:
                if alphabet[a] == l:
                    word_sum += (a + 1)
    
    if word_sum in nums:
        triangle_words += 1
        
print(triangle_words)