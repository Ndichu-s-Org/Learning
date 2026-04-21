//const - block scoped, not reasignable

const PI = 3.14159;

//PI = 3; //TypeError: Assignment to constant variable

//IMPORTANT: const on objects only prevents reassignment of the binding. 
//The object itself can still be mutated.

const user = {name: 'Alice'};

user.name = 'Bob'; //mutating the object is allowed

console.log(user)

//user = {} //TypeError - cannot reassign the variable