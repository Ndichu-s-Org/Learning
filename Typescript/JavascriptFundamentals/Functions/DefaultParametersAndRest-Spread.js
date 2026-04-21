//Default Parameters
function createUser(name, role = 'viewer', active = 'true') {
    return {name, role, active};
}

createUser('Alice'); // { name: 'Alice', role: 'viewer', active: true }

createUser('Bob', 'admin'); //{ name: 'Bob',role: 'admin',active: true }

//Rest parameters - collect remaining args into an array

function sum(...numbers) {
    return numbers.reduce((total, n) => total + n, 0);
}

console.log(sum(1, 2, 3, 4)); //10

//Spread operator - expand array into arguments
const nums = [1, 2, 3];

Math.max(...nums); //3