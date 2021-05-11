function calculateArea (argument) {
    let result;
    if (typeof(argument) != 'number') {
        console.log(`We can not calculate the circle area, because we receive a ${typeof(argument)}.`);
    } else {
        result = Math.PI * argument * argument;
        console.log(result.toFixed(2));
    }
}

console.log(typeof(5))
calculateArea(5)
calculateArea('name')