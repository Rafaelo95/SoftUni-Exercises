function solve(arr) {

    let result = {};

    arr.forEach(element =>{
        let firstLetter = element[0];
        let [name, price] = element.split(' : ');
        price = Number(price);
        if(!result[firstLetter]){
            result[firstLetter] = [];
        }
        
        result[firstLetter].push({name, price});
        result[firstLetter].sort((a, b) => (a.name).localeCompare(b.name));
    })
    

    let r = [];
    Object.entries(result).sort((a, b) => a[0].localeCompare(b[0])).forEach(entry => {
        let values = entry[1]
        .sort((a, b)=> a.name.localeCompare(b.name))
        .map(product=>`  ${product.name}: ${product.price}`)
        .join('\n')

        let string = `${entry[0]}\n${values}`

        r.push(string);
    })

    return r.join('\n');
    
}


console.log(solve(['Appricot : 20.4',
'Fridge : 1500',
'TV : 1499',
'Deodorant : 10',
'Boiler : 300',
'Apple : 1.25',
'Anti-Bug Spray : 15',
'T-Shirt : 10']


));