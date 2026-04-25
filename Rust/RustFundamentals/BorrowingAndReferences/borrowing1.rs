//RULE: You can have EITHER
// - Any number of immutable refernces (&T), OR
// - Exactly ONE mutable reference (&mut T)
//But NEVER both at the same time


let mut s = String::from("hello");

let r1 = &s; //OK - first immutable referece

let r2 = &s; //OK - second immutable reference

let r3 = &mut s; //ERROR - cannot borrow as mutable while immutable refs exist

print!("{r1} and {r2}"); //r1 and r2 used here - their life ends

let r3 = &mut s; // OK now - r1 and r2 no longer used
println!("{r3}");

// Dangling reference - Rust prevents this at compile time
// fn dangle () -> &String {
// let s = String::from("hello");
// &s
//  }


//&str is a reference to a portion of a String (or a string literal)
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes()
    for (i, &byte) in bytes.iter().enumerate() {
        if byte == b' ' {
            return &s[..i]; // return slice up to the space
        }
    }
    &s[..] // return the whole string if no space found
}


let sentence = String::frorm("hello world");


let word = first_word(&sentence); //works with both &String and &str

println!("{word}"); //hello