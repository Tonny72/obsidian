---
created: [[2012-07-21]]T09:27:57.0000000+02:00
tags:
  - MHZ
---

Basic law of CS var change
zaterdag 21 juli 2012
9:27

Outotec
Logic for Changing CellStation Variable

Q = Value that DCS Writes to its Output
I = Value what DCS Reads from its Input
N = New Value from DCS Operator

' DCS try to Change CellStation Variable and it's Time-Out is in Progress
1\. Is Time Elapsed ?
If YES Go to Step 3 ' Changing Unsucceed

If NO Go to Step 2 ' Check if Change was Succeed

' Wait until CellStation Sends New Value Back
2\. Q = I ?
If YES Reset Timer and Stop ' DCS Change Succeed

If NO Stop

' New Value is Supplied from DCS
3\. N = Q ?
If YES Go to Step 4

If No Set Q = N and Start Timer

' Value Changed on CellStation
4\. N = I ?
If YES Stop

If No Set N = I
