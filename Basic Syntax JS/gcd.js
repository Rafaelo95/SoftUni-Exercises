function solve(firstNum, secondNum) {

    let smallerNum = Math.min(firstNum, secondNum);

    let biggestDivider = 1;

    for(let i = 1; i <= smallerNum; i++) {

        if (firstNum % i == 0 && secondNum % i == 0) {
            biggestDivider = i;
        }
    }

    console.log(biggestDivider)

}

solve(24, 125152)