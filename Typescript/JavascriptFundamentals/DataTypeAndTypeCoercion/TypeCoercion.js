// JS automatically converts types in many situations. 
// this is one of JS's most error-prone features 
// and exactly why typescript exists

//Addition with a string: coerces number to string (concatenation)

console.log('5' + 1); //'51' - number becomes string

console.log('5' + true); //5true

//other math operators: coerce string to number
console.log('5' - 1);  //4

console.log('5' * 2); // 10

console.log('5' - true); // 4 true becomes 1

//Equality Coercion: == vs ===

console.log(5 == '5'); // true - loose equality (coerces types)

console.log(5 === '5'); // false - strict equality (no coercion)

console.log(null == undefined); //true

console.log(null === undefined); //false