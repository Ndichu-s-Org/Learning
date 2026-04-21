**Block Scope**: Variables declared with `let` or `const` are only accessible within the `{}` block where they're declared—like `if`, `for`, or just `{}` braces. Outside that block, they don't exist.

**Hoisting**: JavaScript moves `var` (and function) declarations to the top of their scope before execution, but keeps assignments in place. This makes `var x` available (as `undefined`) anywhere in its function, even before the line where you wrote it.

**Rule of Thumb** : Always use const by default. Use let only when you know the variable will be reassigned. Never use
var in modern code.