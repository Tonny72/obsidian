---
modified:  2025-09-15 10:40
date created: 2022-12-01T00:00:00+02:00
date modified: 2025-10-16T05:05:27+02:00
---
![Avatar](Exported%20image%2020250721193501-0.png)

**Tonnylemmens**  
Yesterday at 21:18  
import polars as pl  
df = pl.DataFrame(  
{  
"year": [2020, 2020, 2021, 2022, 2022],  
"foo": ["A", "A", "B", "B", "C"],  
"N": [1, 2, 2, 4, 2],  
"bar": ["k", "l", "m", "m", "l"],  
}  
)  
print(df)  
The console output in debug is wrong, in run is it correct

- [polars debug escape chars bug.py](https://jbs.zendesk.com/attachments/token/3cjoGGsoGIpANQ8KP8XuB5LQI/?name=polars+debug+escape+chars+bug.py) (239 Bytes)
- ![Run.jpg](https://jbs.zendesk.com/attachments/token/zJZhwQ8agCPyE1K40qdS2dNEI/?name=Run.jpg) (10 KB)
- ![debug.jpg](https://jbs.zendesk.com/attachments/token/nZE41hb1ZgGu8CkH6KIqFc4mH/?name=debug.jpg) (50 KB) 
**Andrey Resler**  
Yesterday at 22:05  
Hi,  
Thank you for contacting JetBrains support.  
Could you please make sure that you have encoding set to UTF-8 in **Preferences | Editor | General | Console**. Does the issue still persist?
 \> From \<[https://intellij-support.jetbrains.com/hc/en-us/requests/4501139?page=1](https://intellij-support.jetbrains.com/hc/en-us/requests/4501139?page=1)\>      
\> From \<[https://intellij-support.jetbrains.com/hc/en-us/requests/4501139?page=1](https://intellij-support.jetbrains.com/hc/en-us/requests/4501139?page=1)\>