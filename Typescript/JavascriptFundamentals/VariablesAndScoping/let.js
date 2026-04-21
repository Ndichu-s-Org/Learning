//let - block-scoped, reassignable

let count = 0

count = 1; //OK - reassignment is allowed

if (true) {
    let blockVar = 'only here';
}

console.log(blockVar); //ReferenceError - not accesible outside block

//Temporal Dead Zone (TDZ) - cannot be used before declaration
console.log(age) //Reference Error
let age = 25