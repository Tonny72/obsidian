---
date modified: 2025-07-21
---
# IO Status.
- created: [[2011-04-26]]
- dinsdag 26 april 2011
  9:15
  
  1.  **IO Status.**
      1.  **IO Status Dword.**
  The datatype of the status information is of type Dword. It applies to the predefined structured data types DwordIO, DintIO, BoolIO and RealIO used in the devices in the PCDeviceLib.
  
  ***Note***. This does not apply to the control connection, CC.Forward.Status. Refer to section below for details.
  
  The status property is implemented as a Dword. The 32-bits (bits 0 to 31) of the status component are defined according to table below.
  
  Bits 0-7 are used for the data quality and sub-status information about the quality.
  
  Bits 8-16 are reserved for future use.
  
  Bits 17-23 are used to indicate Forced, ISP/OSP active, status of a redundant I/O module pair etc.
  
  Bits 24-31 are protocol specific status, which a protocol handler is allowed to use.
  
  ![image1](image1-17.gif)
  | **Bit(s)** | **Description**          | **Comment**                                                                                                     |
  |------------|--------------------------|-----------------------------------------------------------------------------------------------------------------|
  | p          | Protocol Specific Status | Used by the protocol handler.                                                                                   |
  | F          | Forced value             | Used as an indication to the application that the signal-value is forced.                                       |
  | I          | Inverted value           | Used as an indication to the application that the signal-value is inverted. Only applies for BoolIO and RealIO. |
  | M          | Simulated value          | Used as an indication to the application that the signal-value is simulated.                                    |
  | X          | ISP/OSP active           | Used as an indication to the application that the signal-value is an ISP or OSP value.                          |
  | O          | Backup error             | Used as an indication that the backup unit of a Redundant pair has indicated an error.                          |
  | U          | Unit B primary           | Used as an indication to the application that unit B of a redundant pair is running as primary.                 |
  | R          | Redundant mode           | Used as an indication to the application that this channel has redundancy.                                      |
  | r          | Reserved                 |                                                                                                                |
  | Q          | Quality                  | Used as shown in tables below                                                                                   |
  | S          | Sub status               | Used as shown in tables below                                                                                   |
  | L          | Limit                    | Used as shown in tables below                                                                                   |
  Table 4 Definition of Status Bits
  
  | **Quality** | **Bit value** | **Definition** | **Description**                                                                |
  |-------------|---------------|----------------|--------------------------------------------------------------------------------|
  | 0           | 00SSSSLL      | Bad            | Value is not useful for reasons indicated by the Sub status.                   |
  | 1           | 01SSSSLL      | Uncertain      | The quality of the value is uncertain for reasons indicated by the Sub Status. |
  | 2           | 10SSSSLL      | Not used.      | **                                                                            |
  | 3           | 11SSSSLL      | Good           | The quality of the value is good.                                              |
  Table 5 Definition of Quality Bits
  
  ****
  <table style="width:100%;">
  <colgroup>
  <col style="width: 13%" />
  <col style="width: 13%" />
  <col style="width: 17%" />
  <col style="width: 55%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><strong>Sub status</strong></th>
  <th><strong>Bit value</strong></th>
  <th><strong>Definition</strong></th>
  <th><strong>Description</strong></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>0-2</td>
  <td></td>
  <td>Not used</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>3</td>
  <td>000011LL</td>
  <td>I/O Unit Failure</td>
  <td><p>An I/O unit failure has been detected.</p>
  <p>The I/O-value will be frozen to the last known value. Bit 20 (X) is set if ISP/OSP used.</p></td>
  </tr>
  <tr class="odd">
  <td>4</td>
  <td>000100LL</td>
  <td>Channel Failure</td>
  <td><p>An I/O channel error has been detected.</p>
  <p>The I/O-value will be frozen to the last known value. Bit 20 (X) is set if ISP/OSP used.</p>
  <p>Additional information could be given in Limit field, like HighHigh and LowLow.</p></td>
  </tr>
  <tr class="even">
  <td>5-15</td>
  <td></td>
  <td>Not used</td>
  <td></td>
  </tr>
  </tbody>
  </table>
  Table 6 Definition of Sub Status Bits Quality = Bad.
  
  <table>
  <colgroup>
  <col style="width: 12%" />
  <col style="width: 13%" />
  <col style="width: 20%" />
  <col style="width: 54%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><strong>Sub status</strong></th>
  <th><strong>Bit value</strong></th>
  <th><strong>Definition</strong></th>
  <th><strong>Description</strong></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>0-4</td>
  <td></td>
  <td>Not used</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>5</td>
  <td>010101LL</td>
  <td>Engineering Units Exceeded.</td>
  <td><p>The I/O-value is outside the engineering units defined for this parameter, but is not bad data quality. The value is in underflow or overflow.</p>
  <p>Limit field indicates which limit has been exceeded but does NOT necessarily imply that the value cannot move farther out of range.</p></td>
  </tr>
  <tr class="odd">
  <td>6-15</td>
  <td></td>
  <td>Not used</td>
  <td></td>
  </tr>
  </tbody>
  </table>
  Table 7 Definition of Sub Status Bits Quality = Uncertain.
  
  | **Sub status** | **Bit value** | **Definition** | **Description**            |
  |----------------|---------------|----------------|----------------------------|
  | 0-5            |              | Not used       |                           |
  | 6              | 110110LL      | Local Override | The value has been Forced. |
  | 7-15           |              | Not used       |                           |
  Table 8 Definition of Sub Status Bits Quality = Good
  
  | **Sub status** | **Bit value** | **Definition** | **Description**                              |
  |----------------|---------------|----------------|----------------------------------------------|
  | 0              | QQSSSS00      | Not limited    | The value is free to move up or down.        |
  | 1              | QQSSSS01      | Low limited    | The value has ‘pegged’ at some lower limit.  |
  | 2              | QQSSSS10      | High limited   | The value has ‘pegged’ at some higher limit. |
  | 3              | QQSSSS11      | Not used       |                                             |
  Table 9 Definition of Limit Bits
  
  | **Dword status bits 0 to 7** | **Hex Value** | **Dec Value** | **Description**                        |
  |------------------------------|---------------|---------------|----------------------------------------|
  | 11000000                     | C0            | 192           | Good data quality, no errors           |
  | 11011000                     | D8            | 216           | Good data quality and Forced           |
  | 01010101                     | 55            | 85            | Uncertain, Underflow (RealIO)          |
  | 01010110                     | 56            | 86            | Uncertain, Overflow (RealIO)           |
  | 00001100                     | C             | 12            | Bad, unit error                        |
  | 00010000                     | 10            | 16            | Bad, channel error                     |
  | 00010001                     | 11            | 17            | Bad, channel error, very low (RealIO)  |
  | 00010010                     | 12            | 18            | Bad, channel error, very high (RealIO) |
  Table 7 Typical Values of Status Bits
  
  ***Note.*** Uncertain, engineering units exceeded `16#54`, `10#84` is not used in 800xA.
  
  ***Note.*** Bad, channel error, very low (RealIO) `16#11`, `10#17` is only used be some analog input S900 IO modules. PCDeviceLib uses this value as ‘bad’ data quality.
  
  ***Note.*** Bad, channel error, very high (RealIO) `16#12`, `10#18` is only used be some analog input S900 IO modules. PCDeviceLib uses this value as ‘bad’ data quality.
  2.  **IO Status Determination.**
  
  In the control module code the last 8 bits QQSSSSLL are analyzed, the quality, the sub status and the limit are analyzed. The sub status information is not used in the CMT. No distinction is made between unit failure and channel failure.
  
  The code uses the values from the project constants cPI.IOStatus.
  
  QualityBit1 = `10#64`, = `16#40`, = `2# 0100 0000`
  
  QualityBit2 = `10#128`, = `16#80`, = `2# 1000 0000`
  
  ![image2](image2-24.jpg)
  
  If a signal quality becomes bad data quality, then an OE Alarm/Event is created.
  
  To analyze if a signal has been Forced, the parameter InteractionPar.Forced or IO.Forced is analyzed in the code, not the RealIO.Status or BoolIO.Status.