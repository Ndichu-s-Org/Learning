// Functions are the first class citizens in Javascript - they can be assigned too variables, 
// passed as argumeents, and returned from other functions

//Function Declaration - hoisted callable before definition

function greet(name) {

    return 'Hello, ' +  name;
}

//Function Expression  - not hoisted

const greet2 = function(name) {

    return 'Hello, ' + name;

};

//Arrow function - shorter syntax, no own 'this'

const greet3 = (name) => 'Hello' + name;

//Multiline arrow function
const greet4 = name => {

    const message = 'Hello,' + name;
    
    return message
}


