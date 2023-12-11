import math

grid_size = 2


def path_count(count):
    numerator = math.factorial(2*count)
    denominator = math.factorial(count)**2
    
    print(numerator//denominator)


path_count(20)