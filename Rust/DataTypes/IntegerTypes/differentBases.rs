fn main() {
    // DECIMAL (base 10) - most common
    let decimal = 98_222;  // underscores for readability
    let decimal2 = 255;
    
    // HEXADECIMAL (base 16) - prefix: 0x
    // digits: 0-9, A-F (a-f)
    let hex = 0xff;        // 255 in decimal
    let hex2 = 0x1A;       // 26 in decimal
    let hex3 = 0xDEADBEEF; // common in systems programming
    
    // OCTAL (base 8) - prefix: 0o
    // digits: 0-7
    let octal = 0o77;      // 63 in decimal (7*8 + 7)
    let octal2 = 0o123;    // 83 in decimal
    
    // BINARY (base 2) - prefix: 0b
    // digits: 0, 1
    let binary = 0b1111_0000;  // 240 in decimal
    let binary2 = 0b1010;       // 10 in decimal
    
    // BYTE LITERAL (u8 only) - b'X'
    // Only works for ASCII characters
    let byte: u8 = b'A';    // 65 (ASCII value of 'A')
    let byte2 = b'\n';       // 10 (newline)
    let byte3 = b'9';        // 57 (digit character)
    
    // Printing them all
    println!("=== Different Bases ===");
    println!("Decimal:   {}", decimal);
    println!("Hex:       {} = 0x{:X}", hex, hex);
    println!("Octal:     {} = 0o{:o}", octal, octal);
    println!("Binary:    {} = 0b{:b}", binary, binary);
    println!("Byte:      {} = '{}'", byte, byte as char);
    
    println!("\n=== Same number in different bases ===");
    let number = 255;
    println!("Decimal: {}", number);
    println!("Hex:     0x{:X}", number);
    println!("Octal:   0o{:o}", number);
    println!("Binary:  0b{:b}", number);
}