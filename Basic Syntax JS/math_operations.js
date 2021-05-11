function calculate(num1, num2, operator) {
    if (operator == '+') {
        console.log(num1 + num2);
    } else if (operator == '-') {
        console.log(num1 - num2);
    } else if (operator == '*') {
        console.log(num1 * num2);
    } else if (operator == '/') {
        console.log(num1 / num2); 
    } else if (operator == '%') {
        console.log(num1 % num2);
    } else if (operator == '**') {
        console.log(num1 ** num2)
    }
}

function calculateSwitch(n1, n2, op) {
    let result;
    switch (op) {
        case '+': result = n1 + n2;
        case '*': result = n1 * n2
    }

    console.log(result)
}

calculate(5, 6, '+')
calculate(3, 5.5, '*')

calculateSwitch(5, 6, '*')