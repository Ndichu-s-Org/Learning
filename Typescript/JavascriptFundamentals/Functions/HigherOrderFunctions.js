//Functions that take or return other functions

function multiply (factor) {
    return (number) => number * factor; // returns a function 
}

const double = multiply(2);
