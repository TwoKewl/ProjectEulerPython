
sum_of_strings = 0

for i in range(1, 1001):
    string = ''
    
    teen = False
    
    if i == 1000:
        string += 'onethousand'
    else:
        if i // 100 == 1:
            string += 'onehundred'
        if i // 100 == 2:
            string += 'twohundred'
        if i // 100 == 3:
            string += 'threehundred'
        if i // 100 == 4:
            string += 'fourhundred'
        if i // 100 == 5:
            string += 'fivehundred'
        if i // 100 == 6:
            string += 'sixhundred'
        if i // 100 == 7:
            string += 'sevenhundred'
        if i // 100 == 8:
            string += 'eighthundred'
        if i // 100 == 9:
            string += 'ninehundred'
        
        if int(str(i)[-2:]) != 0 and i > 100:
            string += 'and'
        

    
    if 10 <= int(str(i)[-2:]) <= 19:
        teen = True
        match int(str(i)[-2:]):
            case 10:
                string += 'ten'
            case 11:
                string += 'eleven'
            case 12:
                string += 'twelve'
            case 13:
                string += 'thirteen'
            case 14:
                string += 'fourteen'
            case 15:
                string += 'fifteen'
            case 16:
                string += 'sixteen'
            case 17:
                string += 'seventeen'
            case 18:
                string += 'eighteen'
            case 19:
                string += 'nineteen'
        
                
    
    match int(str(i)[-2:]) // 10:
        case 2:
            string += 'twenty'
        case 3:
            string += 'thirty'
        case 4:
            string += 'forty'
        case 5:
            string += 'fifty'
        case 6:
            string += 'sixty'
        case 7:
            string += 'seventy'
        case 8:
            string += 'eighty'
        case 9:
            string += 'ninety'
    
    if teen == False:
        match i % 10:
            case 1:
                string += 'one'
            case 2:
                string += 'two'
            case 3:
                string += 'three'
            case 4:
                string += 'four'
            case 5:
                string += 'five'
            case 6:
                string += 'six'
            case 7:
                string += 'seven'
            case 8:
                string += 'eight'
            case 9:
                string += 'nine'
                
    print(f'{string} - {i}')
    sum_of_strings += len(string)
    
    
print(sum_of_strings)