//var - old way(avoid in modern code)

// var function is scoped, not block scoped, 

// it also gets 'hoisted' to the top of its function,

// causes bugs

//var is Function scoped

function example() {
    if (true) {
        var x = 10; //declared inside block
    }

    console.log(x); //accessible here! outputs 10
}

example()

//var hoisting - declaration moves to the top, but not value
console.log(name); //undefined (not an error!)

var name = 'Alice';

console.log(name); 'Alice'

//the first example becomes
function example() {
    var x;          // Hoisted to top of function
    if (true) {
        x = 10;     // Assignment happens here
    }
    console.log(x); // 10 - x is accessible anywhere in function
}

