function solve(input) {

    function getEngine(power) {
        const engines = [
            { power: 90, volume: 1800 },
            { power: 120, volume: 2400 },
            { power: 200, volume: 3500 },
        ]

        for(let i=0; i< engines.length; i++) {
            if(engines[i].power >= power){
                return engines[i];
            }
        }
    }
    if(input.wheelsize % 2 == 0){
        input.wheelsize -= 1;
    }
    let wheels = [];
    for(let i = 0; i < 4; i++){
        wheels.push(input.wheelsize);
    }

    return {
        model: input.model,
        engine: getEngine(input.power),
        carriage: {type: input.carriage, color: input.color},
        wheels: wheels,
    }

}

console.log(solve({
    model: 'VW Golf II',
    power: 90,
    color: 'blue',
    carriage: 'hatchback',
    wheelsize: 14
}
));

console.log(solve({ model: 'Opel Vectra',
power: 110,
color: 'grey',
carriage: 'coupe',
wheelsize: 17 }
));