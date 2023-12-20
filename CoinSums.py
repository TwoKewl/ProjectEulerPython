
coins = [200, 100, 50, 20, 10, 5, 2, 1]



def get_ways(pence, level):
    result = 0
    coin = coins[level]
    
    for i in range(0, (pence//coin)+1):
        remainder = pence - i * coin
        
        if remainder == 0:
            result += 1
        else:
            if level < len(coins)-1:
                result += get_ways(remainder, level+1)
            
    return result

print(get_ways(200, 0))