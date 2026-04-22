fn main() {
    // Signed overflow example (8-bit)
    let mut signed: i8 = 127;
    println!("i8 max: {}", signed);
    // signed += 1;  // This would panic in debug mode! (overflow)
    
    // Unsigned overflow example
    let mut unsigned: u8 = 255;
    println!("u8 max: {}", unsigned);
    // unsigned += 1;  // This would also panic!
    
    // When to use which:
    let temperature = -5;      // Can be negative → use i32
    let age = 25;              // Never negative → could use u32
    let array_size = 10;       // Indexing → use usize
    
    // Pointer-sized integers (architecture dependent)
    let arch_size: isize = -1; // 64-bit on 64-bit systems
    let arch_usize: usize = 100; // Used for array indexing
    
    println!("isize on this machine: {} bits", 
             std::mem::size_of::<isize>() * 8);
    println!("usize on this machine: {} bits", 
             std::mem::size_of::<usize>() * 8);
}