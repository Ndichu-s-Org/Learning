// floating poing - IEEE 754

let x: f64 = 3.14;

let y: f32 = 2.0;


//Boolean

let t: bool = true;
let f: bool = false;

//char -  a Unicode, scalar value (4 bytes, not 1 !)

let letter: char = 'z';

let emoji: char = '😻';

let kanji: char = '国';

//Compoind: Tuple - fixed length, can mix types

let tup: (i32, f64, bool) = (500, 6.4, true);

let (x, y, z) = tupl; //destructures

let first = tup.0;  //index access


//compound: Array - fixed length, same type, stack-allocated
let arr: [132; 5] = [1, 2, 3, 4];

let zeroes = [0; 10]; //[0,0,0,0,0,0,0,0,0,0]

let third = arr[2]; //3 - zero - indexed

//arr[10];  //panics at runtime: index out of bounds