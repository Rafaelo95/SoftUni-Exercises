function solve (arr) {
    let towns = [];
    let filteredElements = [];

    arr.forEach(element =>{
        filteredElements.push(element.split('|').filter(function (e) {
            return e ? e : '';
        }))
    })

    for(let i = 1; i < filteredElements.length; i++) {
        let latitude = Number(Number(filteredElements[i][1]).toFixed(2))
        let longitude = Number(Number(filteredElements[i][2]).toFixed(2))
        towns.push({"Town": filteredElements[i][0].trim(), "Latitude": latitude, "Longitude": longitude})
    }

    return JSON.stringify(towns)
}


console.log(solve(['| Town | Latitude | Longitude |',
'| Sofia | 42.696552 | 23.32601 |',
'| Beijing | 39.913818 | 116.363625 |']
));