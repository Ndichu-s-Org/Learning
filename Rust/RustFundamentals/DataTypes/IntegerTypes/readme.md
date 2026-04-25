Great questions! Let me explain each concept clearly.

## 1. What do `i8`, `i16`, etc. mean?

The numbers (8, 16, 32, 64, 128) represent **how many bits** of memory the integer uses:

- **i8** = 8 bits = 1 byte
- **i16** = 16 bits = 2 bytes
- **i32** = 32 bits = 4 bytes
- **i64** = 64 bits = 8 bytes
- **i128** = 128 bits = 16 bytes

**More bits = larger range of numbers** but uses more memory.

## 2. Signed vs Unsigned Integers

### Signed (`i` = integer)
- Can store **positive AND negative** numbers
- Uses one bit for the sign (+/-)
- Range: `-(2^(n-1))` to `2^(n-1) - 1`

### Unsigned (`u` = unsigned)
- Can store **ONLY non-negative** numbers (0 and positive)
- Uses all bits for the value
- Range: `0` to `2^n - 1`

### Visual Comparison for 8-bit:

```
Signed (i8):    -128 to 127     (256 total values)
Unsigned (u8):    0 to 255      (256 total values)

Bit pattern comparison:
Binary | i8 value | u8 value
00000000 |    0    |    0
01111111 |  127    |  127
10000000 | -128    |  128
11111111 |   -1    |  255
```







## 5. Quick Reference Table

| Type | Bits | Signed Range | Unsigned Range |
|------|------|--------------|----------------|
| i8/u8 | 8 | -128 to 127 | 0 to 255 |
| i16/u16 | 16 | -32,768 to 32,767 | 0 to 65,535 |
| i32/u32 | 32 | -2.1B to 2.1B | 0 to 4.29B |
| i64/u64 | 64 | -9.2×10¹⁸ to 9.2×10¹⁸ | 0 to 1.84×10¹⁹ |
| i128/u128 | 128 | huge | huge |
| isize/usize | pointer | arch dependent | arch dependent |



**Key takeaway**: Use i32 for most integers (default), usize for indexing/array sizes, and choose smaller types only when memory is critical!