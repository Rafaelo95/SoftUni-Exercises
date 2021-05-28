function rectangle(width, height, color) {

    let r = {
        width: Number(width), 
        height: Number(height), 
        color: color[0].toUpperCase() + color.slice(1),
        calcArea: function calcArea() {
            return this.width * this.height;
        }
    }

    return r;
}


let rect = rectangle(4, 5, 'red');
console.log(rect.width);
console.log(rect.height);
console.log(rect.color);
console.log(rect.calcArea());
