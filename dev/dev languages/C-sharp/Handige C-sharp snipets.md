---
modified:  2025-08-29
date created: 2021-11-25T00:00:00+02:00
date modified: 2025-09-19T20:59:03+02:00
---
# Random DateTime

Random rnd = new Random();  
DateTime dt = new DateTime(rnd.NextInt64(DateTime.MinValue.Ticks, DateTime.MaxValue.Ticks));