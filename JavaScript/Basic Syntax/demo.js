let newArray = [10, 5, 4, 1, 25, 15];

let [firstNum, ...other] = newArray;

console.log(firstNum);

for(let i = 0; i < other.length; i++) {
    console.log(other[i]);
}