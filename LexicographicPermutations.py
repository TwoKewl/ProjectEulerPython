import itertools

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_permutations(lst):
    return list(itertools.permutations(lst))[999999]
    
a = get_permutations(nums)

number = ''.join(a)

print(int(number))