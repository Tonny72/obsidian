---
date created: 2025-08-01T14:22:14+02:00
date modified: 2025-10-01T21:20:15+02:00
---
- #dev
- # Python multi-process
- ```python
  import time
  from concurrent.futures import ProcessPoolExecutor
  
  class Table:
      def __init__(self, i: int) -> None:
          self.i = i
  
      def import_data(self):
          print(f"Task {self.i} starting")
          time.sleep(2)
          print(f"Task {self.i} completed")
          return
  
  if __name__ == '__main__':
      executor = ProcessPoolExecutor()
      count = 0
      taken = []
      while True:
          n = int(input("Enter aantal: "))
          for i in range(count, count + n):
              obj = Table(i)
              taken.append(obj)
              future = executor.submit(obj.import_data)
          count += n
  
  ```
-