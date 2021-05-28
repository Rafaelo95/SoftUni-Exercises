function solve(arr) {
    let log = {};
    arr.forEach(element =>{
        let [town, product, price] = element.split(' | ');
        price = Number(price);

        if (!log[product]) {
            log[product] = { town, price };
        } else {
            log[product] = log[product].price <= price ? log[product] : {town, price};
        }
        
        
    })

    let result = [];
    for (const item in log) {
        result.push(`${item} -> ${log[item].price} (${log[item].town})`)
    }

    return result.join('\n');
}

console.log(solve(['Sample Town | Sample Product | 1000',
    'Sample Town | Orange | 2',
    'Sample Town | Peach | 1',
    'Sofia | Orange | 3',
    'Sofia | Peach | 2',
    'New York | Sample Product | 1000.1',
    'New York | Burger | 10']));