function stringLength (el1, el2, el3) {
    let sumLength;
    let averageLength;

    sumLength = el1.length + el2.length + el3.length;
    averageLength = Math.floor(sumLength / 3);
    
    console.log(sumLength);
    console.log(averageLength);
}


stringLength('chocolate', 'ice cream', 'cake')