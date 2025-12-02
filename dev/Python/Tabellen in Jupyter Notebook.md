---
date created: 2025-07-23
modified: 2025-08-20
---
# Tabellen in Jupyter Notebook


## Een grote time-series tabel omzetten naar 1 maand
```python
def format_table2(df: pl.DataFrame):

    '''Format the dataframe for display.'''

    _df = df.sort("datetime")

    _df = _df.group_by_dynamic("datetime", every="1mo")\

        .agg([pl.all().exclude('datetime').sum()])\

        .filter(pl.col('datetime') >= pl.datetime(2020, 1, 1, 0, 0, 0))

    return _df
```
##  Een experiment met een Great Table
```python
def format_table3(df: pl.DataFrame, cols):
    _df = GT(df).fmt_date(columns="datetime").fmt_number(columns=cols, decimals=0, use_seps=False).opt_stylize(style=5, color="blue", )
    return _df
```
## Een polars dataframe omvormen naar een tabel
```python
def format_table4(df: pl.DataFrame, cols):
    pdf = df.to_pandas().style.format({"datetime": lambda t: t.strftime("%m/%Y")}, precision=1)
    #pdf.style.set_properties(**{'text-align': 'left'})
    #html_table = pdf.to_html()

    html_table = f"""
    <div style="font-size:12px; text-align:left">
        {pdf.to_html(index=False, justify='left')}
    </div>
    """
    return HTML(html_table)
```
## Main function
Een time-series tabel omvormen naar een geschikt notebook tabel
```python
def format_table(df: pl.DataFrame, cols):
    _cols = ['datetime']
    _cols.extend(cols)
    _df = df.select(_cols)
    _df = format_table2(_df)
    gt = format_table4(_df, cols)
    return gt
```

## Links
- [Jupyter Notebook](dev/Python/Jupyter%20Notebook.md)
- [Great Tables](dev/Python/Great%20Tables.md)
- [peer](dev/peer.md)