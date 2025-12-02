---
date created: 2024-09-22T07:43:00+02:00
date modified: 2025-09-19T21:11:46+02:00
---

- # Log
- ## 2024-10-10
  Rust is echt wel moeilijk
- # Difference between & and *
  ```rust
  let x = 5;
  let y = &x; // y is a shared reference to x
  println!("The value of y is: {}", y);
  
  let mut x = 7; // Declare a mutable variable
  let y = &mut x; // Create a mutable reference to x
  *y += 1; // Modify the value through the mutable reference
  println!("The value of x is: {}", x);
  
  let x = 9;
  let y = &x; // y is a reference to x
  let z = *y; // z is the value that y points to, which is 5
  println!("The value of z is: {}", z);
  ```
  
  ```output
  Hello, world!
  The value of y is: 5
  The value of x is: 8
  The value of z is: 9
  ```
- # Smart Pointer
  [Box / Rc / Arc / Mutex - Smart Pointers Simplified - Rust (youtube.com)](https://www.youtube.com/watch?v=mNHdD69iLzA)
  Probleem:
  ![[assets/images/Pasted image 20241001071847\.jpg]]
  
  Oplossing:
  ![[assets/images/Pasted image 20241001072555\.jpg]]
- # Rc<T\> (Single-threaded reference-counting pointer)
  Multiple ownership
- If you need mutability, put a Cell or RefCell inside the Rc.
- A cycle between Rc pointers will never be deallocated. For this reason, Weak is used to break cycles. For example, a tree could have strong Rc pointers from parent nodes to children, and Weak pointers from children back to their parents.
- # Rust snippets
- ## HashMap
  Een Hashmap moet altijd mutable zijn.
  ```rust
  struct Table {  
    name: String,  
    columns: HashMap<String, String>,  
  }  
  
  fn main() {  
    println!("Let's get rusty!");  
      
    let mut table: HashMap<String, String> = HashMap::new();   
      
    let s1 = String::from("string1");  
    let s2 = String::from("string2");  
    let s3 = String::from("string3");  
    let s4 = String::from("string4");  
      
    table.insert(s1, s2);  
  }
  ```
- ## Option
  Option is een enum
  ```Rust
  pub enum Option<T> {
    None,
    Some(T),
  }
  ```
- ## Result
  ```Rust
  enum Result<T, E> { 
  Ok(T), 
  Err(E), 
  }
  ```