
fn main () {

    //immutable by default

    let x = 5;

    println!("{x}");

    //x = 6; // error[E0384]: cannot assigntwice to immutable variable

    //Opt into mutability with `mut`

    let mut count = 0;
    
    count += 1;

    count += 1;

    println!("Count: {count}");

    //Shadowing - re-declare with the same name
    //unlike mut, shadowing can change the type

    let spaces = " ";   //&str

    let spaces = spaces.len(); //usize - new variable, same name

    println!("Spaces: {spaces}");

    //constants - always immutable, must have a type, computed at compile time

    const MAX_POINTS: u32 = 100_00;
    
    println!("{MAX_POINTS}");




}