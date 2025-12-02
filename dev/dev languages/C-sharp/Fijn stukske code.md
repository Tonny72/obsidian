---
date created: 2021-11-15
tags:
  - dev
---

// See <https://aka.ms/new-console-template> for more information
```C#
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

PrimitiveDataFrameValue dfv1 = new PrimitiveDataFrameValue(5);
PrimitiveDataFrameValue dfv2 = new PrimitiveDataFrameValue(6);
StringDataFrameValue sdfv1 = new StringDataFrameValue("tttt");

List <DataFrameValue> list = new List\<DataFrameValue\> { dfv1, dfv2, sdfv1 };

double a = dfv1.GetValue();
var b = dfv1.Add(66);

var c = dfv1.Length;
var d = list\[2\].Length;

Console.WriteLine("Einde");
Console.ReadLine();

public abstract partial class DataFrameColumn : IEnumerable
{
private long _length;

/// \<summary\>
/// The length of this column
/// \</summary\>
public long Length
{
get =\> \_length;
protected set
{
if (value \< 0)
throw new ArgumentOutOfRangeException();
\_length = value;
}
}

/// \<summary\>
/// The number of \<see langword="null" /\> values in this column.
/// \</summary\>
public abstract long NullCount
{
get;
}

private string \_name;

/// \<summary\>
/// The name of this column.
/// \</summary\>
public string Name =\> \_name;

/// \<summary\>
/// The type of data this column holds.
/// \</summary\>
//public Type DataType { get; }
protected DataFrameColumn(string name, long length)
{
Length = length;
\_name = name;
// DataType = type;
}

public abstract int GetLength();

public IEnumerator GetEnumerator()
{
throw new NotImplementedException();
}

/// \<summary\>
/// Indexer to get/set values at \<paramref name="rowIndex"/\>
/// \</summary\>
/// \<param name="rowIndex"\>The index to look up\</param\>
/// \<returns\>The value at \<paramref name="rowIndex"/\>\</returns\>
public object this\[int rowIndex\]
{
get =\> GetValue(rowIndex);
set =\> SetValue(rowIndex, value);
}

public abstract void SetValue(int rowIndex, object value);

public abstract void AddValue(object value);

/// \<summary\>
/// Returns the value at \<paramref name="rowIndex"/\>.
/// \</summary\>
/// \<param name="rowIndex"\>\</param\>
/// \<returns\>The value at \<paramref name="rowIndex"/\>.\</returns\>
public abstract object GetValue(int rowIndex);

public static DataFrameColumn operator +(DataFrameColumn left, DataFrameColumn right)
{
return left + right;
}
}

// --------------------------------------------------------------------------

public abstract class DataFrameValue
{
public string name = "Tonny";
public int Length { get =\> GetLength(); }

protected abstract int GetLength();
}
public abstract class DataFrameValue\<T\> : DataFrameValue
{
public abstract T GetValue();

public abstract T Add(T value);

public static T operator +(DataFrameValue\<T\> x, T y)
{
return x.Add(y);
}
}
// --------------------------------------------------------------------------
public partial class PrimitiveDataFrameValue : DataFrameValue\<double\>
{
public double \_value;

public PrimitiveDataFrameValue(double value)
{
\_value = value;
}

public override double Add(double value)
{
return \_value + value;
}

public override double GetValue()
{
return \_value;
}

protected override int GetLength()
{
return 1;
}
}
// --------------------------------------------------------------------------
public partial class StringDataFrameValue : DataFrameValue\<string\>
{
public string \_value;

public StringDataFrameValue(string value)
{
\_value = value;
}

public override string Add(string value)
{
return \_value + value + name;
}

public override string GetValue()
{
return \_value;
}

protected override int GetLength()
{
return \_value.Length;
}
}

```
