// RULE 1: Each value has exactly one owner

//RULE 2: There can only be one owner at a time

//RULE 3: When the owber goes out of scope, the value is dropped (freed)

fn main () {
    {
        let s = String::from("hello"); //s owns the string

        // s is valid here
    
    } // s goes out of scope - Rust calls drop(), memory is freed automatically
    
    // s is no longer valid here

}