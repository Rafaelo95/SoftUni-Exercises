function calculate(speed, area) {

    let speedDifference;
    let speedLimit;

    if (area === 'motorway') {
        speedLimit = 130;
    } else if (area === 'interstate') {
        speedLimit = 90;
    } else if (area === 'city') {
        speedLimit = 50;
    } else if (area === 'residential') {
        speedLimit = 20;
    }

    speedDifference = speed - speedLimit

    if (speedDifference <= 0) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`)
    } else if (speedDifference <= 20) {
        console.log(`The speed is ${speedDifference} km/h faster than the allowed speed of ${speedLimit} - speeding`)
    } else if (speedDifference <= 40) {
        console.log(`The speed is ${speedDifference} km/h faster than the allowed speed of ${speedLimit} - excessive speeding`)
    } else {
        console.log(`The speed is ${speedDifference} km/h faster than the allowed speed of ${speedLimit} - reckless driving`)
    }

}

calculate(40, 'city')