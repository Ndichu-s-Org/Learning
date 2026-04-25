//&T - immutable (shared) reference

fn calculate_length(s: &String) -> usize {
    
    s.len() //we can read but not modify

} //s goes out of scope here, but the string it refers to is not dropped


fn main () {
    let s1 = String::from("hello");

    let len = calculate_length(&s1); //pass a reference - s1 is still owned here
    
    println!("Length of '{s1}' is {len}"); //s1 is still valid!
}


//&mut T - mutable reference - allows modification

fn append_world(s: &mut String) {
    
    s.push_str(", world")
}

fn main () {
    let mut s = String::from("hello");

    append_world(&mut s);
    
    println!("{s}"); //hello world
}