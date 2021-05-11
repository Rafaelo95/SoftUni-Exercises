function rectangeOfStars(num) {
    let number = num;
    let result = '';
    if (number === undefined) {
        for (let i = 1; i <= 5; i++) {
            result += ('* '.repeat(5) + '\n')
    }
    } else {
    for (let i = 1; i <= num; i++) {
        result += ('* '.repeat(number) + '\n')
    }
    }

    console.log(result)
}

rectangeOfStars(3)