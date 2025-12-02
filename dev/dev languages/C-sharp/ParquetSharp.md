---
date created: 2025-08-01T14:22:14+02:00
date modified: 2025-09-19T21:01:50+02:00
---
tags:: parquet

# Writing a Parquet file
- result = 1.47s  aantal = 100_000_000
```c#
  using ParquetSharp;
  using System;
  using System.Collections.Generic;
  using System.Data.Common;
  using System.Diagnostics;
  using System.Linq;
  using System.Runtime.InteropServices;
  using System.Text;
  using System.Threading.Tasks;
  
  namespace fastparquet_experiment
  {
      internal class Program
      {
          static DateTime random_datetime()
          {
              var random = new Random();
              var start = new DateTime(2000, 1, 1);
              var range = (DateTime.Today - start).Days;
              var randomDate = start.AddDays(random.Next(range))
                                    .AddHours(random.Next(0, 24))
                                    .AddMinutes(random.Next(0, 60))
                                    .AddSeconds(random.Next(0, 60))
                                    .AddMilliseconds(random.Next(0, 1000));
              return randomDate;
          }
  
          static void Main(string[] args)
          {
              var columns = new Column[]
          {
              new Column<DateTime>("datetime"),
              new Column<float>("value")
          };
  
              var fileWriter = new ParquetFileWriter("random_data.parquet", columns);
              var rowGroupWriter = fileWriter.AppendRowGroup();
              var aantal = 100000000;
              var random = new Random();
              var dateTimes = new DateTime[aantal];
              var floats = new float[aantal];
  
              for (int i = 0; i < aantal; i++)
              {
                  dateTimes[i] = random_datetime();
                  floats[i] = (float)(random.NextDouble() * 100);
              }
  
              Stopwatch sw = new Stopwatch();
  
              sw.Start();
  
              // Write data to columns
              using (var dateTimeWriter = rowGroupWriter.NextColumn().LogicalWriter<DateTime>())
              {
                  dateTimeWriter.WriteBatch(dateTimes);
              }
  
              using (var floatWriter = rowGroupWriter.NextColumn().LogicalWriter<float>())
              {
                  floatWriter.WriteBatch(floats);
              }
  
              fileWriter.Close();
              sw.Stop();
  
              Console.WriteLine("Elapsed={0}", sw.Elapsed);
              Console.WriteLine("Parquet file created successfully.");
              Console.ReadLine();
          }
      }
  }
  
  ```