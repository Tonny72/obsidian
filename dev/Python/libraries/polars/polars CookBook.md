---
tags:
  - dev
  - polars
date created: 2024-08-07
modified: 2025-07-29
---
# Diff between rows per category
```python
import polars as pl	
from datetime import datetime

pl.Config.set_tbl_rows(100)
data  = [[datetime(2012, 5, 1, 0, 0, 0), 1.0, 'A'],
         [datetime(2012, 5, 1, 4, 0, 0), 3.0, 'A'],
         [datetime(2012,5,2), 2.0, 'B'],
         [datetime(2012,5,3), 3.3, 'A'],
         [datetime(2012,5,4), 4.4, 'B'],
         [datetime(2012,5,5), 5.5, 'B'],
         [datetime(2012,5,6,15,0,0), 6.0, 'A'],
         [datetime(2012,5,6,15,10,0), 7.0, 'B'],
         [datetime(2012,5,6,17,0,0), 7.7, 'B'],
         [datetime(2012,5,7,1,1,0), 8.8, 'A'],
         [datetime(2012,5,7,1,3,0), 9, 'B'],
         [datetime(2012,5,8,1,1,0), 9.9, 'B'],
         [datetime(2012,5,8,2,1,0), 3.0, 'B'],
         [datetime(2012,5,9,1,1,0), 4.0, 'A'],
         [datetime(2012,5,9,1,10,2), 6.0, 'B'],
         [datetime(2012,5,15,0,0,0), 7.0, 'B']]

df = pl.DataFrame(data)
df = df.rename({df.columns[0]: "datetime", df.columns[1]: "value", df.columns[2]: "source"}).sort("datetime")

df.with_columns(x=pl.col('value').diff().over('source'))
```

# Datetime range
```python
from datetime import datetime  
  
rng = pl.datetime_range(   
    datetime(2000,1,1,10,0),  
    datetime(2000,1,1,22,0),  
    interval='1h',  
    eager=True,  
)  
rng
```

# Cast Datetime
```python
df = df.with_columns(pl.col("datetime").cast(pl.Datetime("ms")))
```

# Upsample
```python
df = pl.read_csv(path,  
                 separator=";",  
                 has_header=False,  
                 try_parse_dates=True,  
                 columns=['column_1', 'column_2'],  
                 dtypes={'column_1': pl.Datetime, 'column_2': pl.Float64})  
df = df.rename({'column_1': 'datetime', 'column_2': 'value'})  
df = df.sort('datetime').group_by_dynamic("datetime", every='1s').agg(pl.col(f'value').max())  
  
x = df.upsample(time_column = "datetime", every="1s").with_columns(pl.col("value").interpolate().alias('interpolate'))  
display(x)
```
![[assets/images/Pasted image 20240807104343\.jpg]]

# Plot Histogram
```python
plt.hist(df['delta'], bins=100, range=[q1, q3])  
plt.show()
```

# Plot Line
```python
import matplotlib.pyplot as plt  
plt.figure(figsize = (12, 5))  
plt.plot(df['datetime'], df['value'])  
plt.title("C3_PT420_01")  
plt.show()
```

