---
modified:  2025-09-15 10:28
tags: [dev, Python]
date created: 2020-06-18T00:00:00+02:00
date modified: 2025-10-01T21:28:49+02:00
---
## UITVOEREN PYTHON SUBPROGRAMMAS
- voeg een -m toe
```commandline
python -m experiments.experiment2
```

## Python no-gil
Vanaf versie 3.13 is er een no-gil versie die echte multithreading toelaat. Maar `pywin32` ondersteund dit niet.

## Parallel Processing in Python
### multi-threading
- numerous threads inside a single process run simultaneously
- sharing the same memory
- example:

```python
import threading import requests 

def download_page(url): 
response = requests.get(url)    
print(f"Downloaded {url}") 

urls = [ 
"https://example.com", 
"https://google.com", 
"https://openai.com" 
] 

threads = [] 
for url in 
urls: 
thread = threading.Thread(target=download_page,
args=(url,))     thread.start()    threads.append(thread) 

for thread in threads: 
thread.join() 
```
## multi-processing
- offers genuine parallelism by using several processes
- each with their own memory space
- **conclusion:** do not use multi-processing
## asynchronous programming

- By leveraging non−blocking operations, asynchronous programming enables the efficient execution of I/O−bound processes. Coroutines, event loops, and futures may all be used to create asynchronous code in Python thanks to the asyncio package
- example
	  
```python
import asyncio 
import aiohttp 

async def fetch_page(url):     async with aiohttp.ClientSession() as session:         async with session.get(url) as response: 
		  return await response.text() 

async def main(): 
  urls = [ 
	  "https://example.com", 
	  "https://google.com", 
	  "https://openai.com" 
  ] 

  tasks = [fetch_page(url) for url in urls]     pages = await asyncio.gather(*tasks)     
print(pages) 

asyncio.run(main()) 
```

![Differences Between Asyncio and Threading](https://superfastpython.com/wp-content/uploads/2022/11/Differences-Between-asyncio-and-threading.png)
## Which one to choose
- **IO bound problems**: use async if your libraries support it and if not, use threading.


