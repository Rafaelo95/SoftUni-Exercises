function calculate(steps, footLenghtMeters, speedKmPerH) {

    let distanceInMeters = (Number(steps) * Number(footLenghtMeters));
    let speedForMeterInSecond = speedKmPerH / 3.6;
    let breaks = Math.floor(distanceInMeters / 500);
    let time = distanceInMeters / speedForMeterInSecond + breaks * 60;

    let timeInHours = Math.floor(time / 3600);
    let timeInMins = Math.floor(time / 60);
    let timeInSecs = Math.floor(time % 60);

    console.log(`${timeInHours < 10 ? 0 : ''}${timeInHours}:${timeInMins < 10 ? 0 : ''}${timeInMins}:${timeInSecs < 10 ? 0 : ''}${timeInSecs}`)

}

calculate(4000, 0.60, 5)