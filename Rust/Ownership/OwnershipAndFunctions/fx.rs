fn takes_ownership(s: String) { //s comes in
    
    println!("{s}")

} //s is dropped here

fn makes_copy(x: i32) { //i32 is Copy, so a copy is made

    println!("{x}");

}

fn main () {
    let s = String::from("hello");

    takes_ownership(s) //s is moved into the function

    //println!("{s}") //error - s was moved

    let x = 5;

    makes_copy(x);  //x is copied

    println!("{x}");  //fine - x is still valid
}

fn takes_and_gives_back(s: String) -> String {
    s //return transfers ownership back to the caller
}
