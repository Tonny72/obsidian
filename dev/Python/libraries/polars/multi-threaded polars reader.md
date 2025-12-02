---
date created: 2025-07-18
modified: 2025-07-30
---
- #Python, #Polars, #[[multi-threading]]
- ```python
  async def read_pq(tags, name):
      _tags = add_path(tags)
      print("start reading", name)
      df = pl.scan_parquet(_tags)
      df = await df.collect_async()
      print(name, "reading done")
      return df
  
  
  async def main_async():
      tasks = set()
      task = asyncio.create_task(read_pq(M4_GT1, "M4_GT1"))
      tasks.add(task)
      task = asyncio.create_task(read_pq(M4_GT1, "M4_GT2"))
      tasks.add(task)
      task = asyncio.create_task(read_pq(M4_GT1, "C2_K22_PM_Power"))
      tasks.add(task)
      task = asyncio.create_task(read_pq(M4_GT1, "C2_FT101"))
      tasks.add(task)
      x = asyncio.gather(*tasks)
      r = await x
      pass
  ```