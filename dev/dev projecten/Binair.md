---
modified:  2025-08-29
tags: [dev]
date created: 2021-02-08T00:00:00+02:00
date modified: 2025-09-19T20:59:17+02:00
---
created:: 2021-02-08
tags:: dev

- # Overzicht
  HP ZBook 17 G6: Intel(R) Core(TM) i7-9850H CPU @ 2.60GHz, 2592 Mhz, 6 Core(s), 12 Logical Processor(s)+
  
  ![image1](image1-7.jpeg)

| Python (HP ZBook) | 0.000262s =   0.263ms = 263µs                            |  |
| Python (HP Zbook G10) | 0.00010309s = 0.103 ms = 103µs cpyton|
| Python (HP Zbook G10) | 0.00002512s = 0.0251 ms = 25.1µs pypy|
| ------------------- | ------------------------------------------------------------ | --- |
| C# .Net Core 3.1 (debug) (HP ZBook)                                        | 23.3 µs                                                      |     |
| C# .Net 5.0 (release) (HP ZBook)                                           | 19.7 µs                                                      |     |
| C# .Net 6.0 (HP ZBook G6)<br>  Visual Studio 2022 met Start without debugging | 12.9 µs                                                      |     |
| C# .Net 8.0 (HP ZBook G6)<br>  Visual Studio 2022 met Start without debugging | 6.6 µs !!                                                    |     |
| Julia (HP ZBook G6)                                                           | 0.0000335s<br>  0.0335ms<br>  33.5µs                         |     |
| Rust                                                                       | 23 µs <br>Update 2024-1010 Gecompileerd als Release: 11.5 µs |     |
| Scala (HP Zbook G6 2024-10-10) | 6.24 µs  |
| C# (Zbook G10 2024-12-05) .Net 9.0 (start without debugging) | 3.78 µs |
| javascript (ZBook G10 2024-12-22) Node 22.11.0|5.038 µs|

- # Scala #dev
  collapsed:: true
	- ```scala
	  @main	
	  def main(): Unit =
	  
	    val before = System.nanoTime
	    val aantal  = 1000000
	    for (x <- 1 to aantal) {
	      var teller: Int = 0
	      var z = new Array[String](256)
	      for (a <- 0 to 1) {
	        for (b <- 0 to 1) {
	          for (c <- 0 to 1) {
	            for (d <- 0 to 1) {
	              for (e <- 0 to 1) {
	                for (f <- 0 to 1) {
	                  for (g <- 0 to 1) {
	                    for (h <- 0 to 1) {
	                      z(teller) = (100000000 + a * 10000000 + b * 1000000 + c * 100000 + d * 10000 + e * 1000 + f * 100 + g * 10 + h).toString()
	                      teller = teller + 1
	                    }
	                  }
	                }
	              }
	            }
	          }
	        }
	      }
	    }
	    val totalTime=System.nanoTime-before
	    val totalTimemMicro = totalTime / 1000.0 / aantal
	    println(totalTimemMicro)
	  ```
-
- # Scala
  ```Scala
  
  @main  
  def main(): Unit =  
  
  val before = System.nanoTime  
  val aantal  = 1000000  
  for (x <- 1 to aantal) {  
    var teller: Int = 0  
    var z = new Array[String](256)  
    for (a <- 0 to 1) {  
      for (b <- 0 to 1) {  
        for (c <- 0 to 1) {  
          for (d <- 0 to 1) {  
            for (e <- 0 to 1) {  
              for (f <- 0 to 1) {  
                for (g <- 0 to 1) {  
                  for (h <- 0 to 1) {  
                    z(teller) = (100000000 + a * 10000000 + b * 1000000 + c * 100000 + d * 10000 + e * 1000 + f * 100 + g * 10 + h).toString()  
                    teller = teller + 1  
                  }  
                }  
              }  
            }  
          }  
        }  
      }  
    }  
  }  
  val totalTime=System.nanoTime-before  
  val totalTimemMicro = totalTime / 1000.0 / aantal  
  println(totalTimemMicro)
  ```
- # Python
  ```python
  importtime
  start=time.time()
  arr=\[\]
  aantal=100000
  forxinrange(aantal):
  teller=0
  forainrange(2):
  forbinrange(2):
  forcinrange(2):
  fordinrange(2):
  foreinrange(2):
  forfinrange(2):
  forginrange(2):
  forhinrange(2):
  x=str(100000000+a\*10000000+b\*1000000+c\*100000+d\*10000+e\*1000+f\*100+g\*10+h)
  arr.append(x\[-8:\])
  
  elapsed_time=time.time()-start
  print("----------------------")
  foryinrange(256):
  print(f"{y}-{arr\[y\]}")
  print(f"{elapsed_time/aantal}")
  ```
- # C# 
  ```C#
  using System;
  using System.Diagnostics;
  
  namespace Binair_core
  {
    class Program
    {
        static void Main(string[] args)
        {
            string[] arr = new string[2570];
            Console.WriteLine("Hello World!");
            var aantal = 1000000;
  
            Stopwatch stopWatch = new Stopwatch();
            stopWatch.Start();
            for (int i = 0; i < aantal; i++)
            {
                int teller = 0;
                for (int a = 0; a < 2; a++)
                {
                    for (int b = 0; b < 2; b++)
                    {
                        for (int c = 0; c < 2; c++)
                        {
                            for (int d = 0; d < 2; d++)
                            {
                                for (int e = 0; e < 2; e++)
                                {
                                    for (int f = 0; f < 2; f++)
                                    {
                                        for (int g = 0; g < 2; g++)
                                        {
                                            for (int h = 0; h < 2; h++)
                                            {
                                                arr[teller] = (100000000 + a * 10000000 + b * 1000000 + c * 100000 + d * 10000 + e * 1000 + f * 100 + g * 10 + h).ToString().Substring(1);
                                                teller++;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            stopWatch.Stop();
            // Get the elapsed time as a TimeSpan value.
            TimeSpan ts = stopWatch.Elapsed;
  
            for (int i = 0; i < 256; i++)
            {
                Console.WriteLine($"{i} -  {arr[i]}");
            }
  
            var ns = ts.TotalMilliseconds / aantal * 1000;
            Console.WriteLine($"{ns} µs");
  
            Console.ReadLine();
        }
    }
  }
  
  
  ```
  
  
  Runtime per loop: 00:00:00.0000233 = 23.3 ns
- # Julia ([[2022-05-06]])
  ```julia
  arr = Array{String}(undef,256)
  aantal = 1000000
  t = time()
  for x in 1:aantal
  teller = 1
  for a in 0:1
  for b in 0:1
  for c in 0:1
  for d in 0:1
   for e in 0:1
  for f in 0:1
    for g in 0:1
  	for h in 0:1
  	  y = last(string(100000000+a\*10000000+b\*1000000+c\*100000+d\*10000+e\*1000+f\*100+g\*10+h),8)
  	  arr\[teller\] = y
  	  teller = teller + 1
  	end
    end
  end
   end
  end
  end
  end
  end
  end
  dt = (time() - t)/aantal
  println(dt)
  \# for x in 1:256
  \#   println(arr\[x\])
  \# end
  ```
- # RUST binair
  ```rust
  use std::time::{Instant};  
  fn main() {  
    const EMPTY_STRING: String = String::new();  
    let mut ar: [String;256] = [EMPTY_STRING; 256];  
  
    let start = Instant::now();  
    let aantal = 100000;  
    for _x in 0..aantal {  
        let mut teller = 0;  
        for a in 0..2 {  
            for b in 0..2 {  
                for c in 0..2 {  
                    for d in 0..2 {  
                        for e in 0..2 {  
                            for f in 0..2 {  
                                for g in 0..1 {  
                                    for h in 0..2 {  
                                        ar[teller] = (100000000 + a * 10000000 + b * 1000000 + c * 100000 + d * 10000 + e * 1000 + f * 100 + g * 10 + h).to_string();  
                                        teller += 1;  
                                    }  
                                }  
                            }  
                        }  
                    }  
                }  
            }  
        }  
    }  
    let duration = start.elapsed() / aantal;  
  
    for _i in 0..256 {  
        println!("{}", ar[_i]);  
    }  
  
    println!("Time elapsed in expensive_function() is: {:?}", duration);  
    println!("{}",aantal);  
  }
  
  ```
-
- javascript
- ```javascript
  const arr = [];
  aantal = 1000000;
  startTime = performance.now();
  for (i = 0; i < aantal; i++)
  {
      teller = 0;
      for (a = 0; a < 2; a++) {
          for (b = 0; b < 2; b++) {
              for (c = 0; c < 2; c++) {
                  for (d = 0; d < 2; d++) {
                      for (e = 0; e < 2; e++) {
                          for (f = 0; f < 2; f++) {
                              for (g = 0; g < 2; g++) {
                                  for (h = 0; h < 2; h++) {
                                      arr[teller] = (100000000 + a * 10000000 + b * 1000000 + c * 100000 + d * 10000 + e * 1000 + f * 100 + g * 10 + h).toString().substring(2)
                                      teller++;
                                  }
                              }
                          }
                      }
                  }
              }
          }
      }
  }
  endTime = performance.now();
  var timeDiff = endTime - startTime; //in ms
  // strip the ms
  timeDiff /= 1000;
  timeDiff /= aantal;
  
  for (i = 0; i < 256; i++)
  {
      console.log(arr[i]);
  }
  
  ms = timeDiff.toExponential(6)
  console.log(ms + " seconds");
  ```