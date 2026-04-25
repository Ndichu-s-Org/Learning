//signed integers (can be negative)



fn main() {
    
    let a: i8 = 127; //-128 to 127

    let b: i16 = 32_767;

    let c: i32 = 2_147_483_647; // default for integer literals

    let d: i64 = 9_223_372_036_854_775_807;

    let e: i128 = 170_141_183_460_469_231_731_687_303_715_884_105_727;

    let f: isize = -1; // pointer-sized (64-bit on 64-bit OS)

    //printing like this is not correct. 
    //You need to use a single format string with placeholders, 
    //not multiple separate strings.
    
    //println!("{a}","{b}","{c}","{d}","{e}","{f}");

    //correct way

    println!("i8:    {}", a);
    println!("i16:   {}", b);
    println!("i32:   {}", c);
    println!("i64:   {}", d);
    println!("i128:  {}", e);
    println!("isize: {}", f);

    //other methods

    // Method 1: All on one line
    println!("{} {} {} {} {} {}", a, b, c, d, e, f);

     // Method 2: With labels (more readable)
    println!("a: {}, b: {}, c: {}, d: {}, e: {}, f: {}", a, b, c, d, e, f);

    // Method 3: Each on separate lines
    println!("a = {}", a);
    println!("b = {}", b);
    println!("c = {}", c);
    println!("d = {}", d);
    println!("e = {}", e);
    println!("f = {}", f);

        // Method 4: Using positional arguments
    println!("{0} {1} {2} {3} {4} {5}", a, b, c, d, e, f);
    
    // Method 5: Using named arguments (Rust 1.58+)
    println!("{a} {b} {c} {d} {e} {f}");



    //Unsigned integers (non-negative only)

    let g: u8 = 255

    let h: u32 = 4_294_967_295;

    let i: u64  = 18_446_744_073_709_551_615;

    let j: usize = 8; //used for indexing

    //integer literals in different bases

    let decimal = 98_222;

    let hex = 0xff;

    let octal = 0o77;

    let binary = 0b1111_0000;

    let byte: u8 = b'A' //65

}