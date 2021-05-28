function solve(arr) {
    let result = [];

    arr.forEach(element => {
        let [name, level, items] = element.split(' / ');
        level = Number(level);

        if(items){
            items = items.split(', ');
        } else{
            items = [];
        }
        result.push({ name, level, items });
    })

    return JSON.stringify(result);
}


console.log(solve(['Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara']
));