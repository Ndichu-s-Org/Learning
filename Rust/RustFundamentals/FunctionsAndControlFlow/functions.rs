//Functions - typed parameters and return type

fn add(c: i32, y:i32) -> i32 {
    x+y //expressions dont need semicolons - last expr is the return value
}

//statements vs expressions
//statement: does not return a value; ends with;

let y = 6

//expression: evaluates to a value; no semicolon
let z = {let a = 3; a * 2}; //z = 6


//if is an expression - can be used in let

let condition = true;
let number = if condition { 5 } else { 6 };

//loop returns a value via break
let mut counter = 0
let result = loop {
    counter += 1;
    if counter = 10 {break counter * 2} //returns 20
};

//for loops use iterator - the idiomatic way to loop

let arr = [10, 20, 30, 40]

for element in arr {
    println!("{element}");
}

//Range-based for

for i in 0..5 { print!("{i}"); } //0 1 2 3 4

for i in 0..= { print!("{i}"); } //0 1 2 3 4 5