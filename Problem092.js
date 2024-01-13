function digitChain(number){
    while (true){
        if (number == 89){
            return 89;
        }
        if (number == 1){
            return 1;
        }

        number = squareDigits(number);
    }
}

function squareDigits(number){
    let num = String(number);
    let sum = 0;
    for (let i = 0; i < num.length; i++){
        sum += num[i]**2;
    }
    return sum;
}

let count = 0;

for (let i = 1; i < 10000000; i++){
    if (digitChain(i) == 89){
        count += 1;
    }
}

console.log(count)