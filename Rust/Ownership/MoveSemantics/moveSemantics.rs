

fn main () {

    // Heap-allocated types (String, Vec, etc,) are MOVED on assignment

let s1 = String::from("hello");

let s2 = s1; //s1 is MOVED into s2 - s1 is now invalid 

//println!("{s1}") // error [E0382]: borrow of moved value: `s1`

println!("{s2}"); //OK


//Stack-only types (integers, bool, etc.) are COPIED

//because they implement the copy trait

let x = 5;

let y = x; //x is COPIED - both x and y are valid
println!("{x} and {y}");

}