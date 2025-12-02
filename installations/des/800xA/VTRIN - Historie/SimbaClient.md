---
created: [[2014-10-16]]T12:39:32.0000000+02:00
tags:
  - 800xA
---
Dit is de ODBC driver voor connectie met de VTRIN RTDB Historie database
[SimbaClient7.2.7z](assets/resources/SimbaClient7.2.7z)

- # ODBC instellingen
  Server: 10.32.29.60
  Database: [[network/des/PCs en Servers/800xA/DESSRVHIS1 1]]-RTDB
  User: tl
  Pw:
- # SQL queries (getest op eng client met excel)
  SELECT Variables.VariableId, Variables.ValueType, Variables.VariableName
  FROM Variables Variables
- ## [[M5_TT120]] value
  ```SQL
  SELECT CurrentValues.IDN, CurrentValues.CT, CurrentValues.CVF, CurrentValues.IDT
  FROM CurrentValues CurrentValues
  WHERE (CurrentValues.IDN=10373)
  ```
  Zie ook
  [RTDB SQL examples](onenote:#RTDB%20SQL%20examples&section-id={76216470-E07B-48E3-B25C-1257A045F10C}&page-id={BAA9435F-3A11-4FD8-85FD-C73ADD3CEC8B}&end&base-path=https://d.docs.live.net/648fe635197c5860/Documenten/OneNote's/Persoonlijk%20(web)/Sibelco/Installaties/DES/800xA/VTRIN%20-%20Historie.one)
- # Opvragen van de Variabel Ids
  ```SQL
  SELECT RowModificationTime, VariableId, VariableName, Description, "Section", Alias, DisplayFormat, Unit, SymbolGroup, Combined, Source, ValueType, BinaryTextId, ProcessArea, DiscreteValue, Created, Deleted,
  Connected, ProcessingMethod, ValueMaxF, ValueMinF, ValueMaxI, ValueMinI, SubstituteMethod, SubstituteValueF, SubstituteValueI, SubstituteVariable, RecordingMethod, CompressionMethod, CompressionError,
  ValueChangeReceiver, Events, PreventDisableOnInit, PreprocessingMethod, NoiseFilterFactor, NoiseFilterEnable, AnalogPower0, AnalogPower1, AnalogPower2, AnalogPower3, AnalogSquareRoot,
  AnalogZeroClamping, Inverted, PulseToEngineering, PulseLowLimit, PulseHighLimit, PulseEngineeringVariable, PulseDerivatedVariable, PulseWeight, PulseDerivatedCoefficient, PulseSensorVariable,
  ApplicationType, CalcActivation, StatisticsLimitFunction, StatisticsReferenceValueI, StatisticsReferenceValueF, PathId, Security, UserStatusId, SendOutputMode, ProducerTable, RowModificationTime_UTC,
  Created_UTC, Deleted_UTC, Variables_RowId, v_LongPath
  FROM Variables
  WHERE (Source = 0)
  ```
  
  The above example also reads the value type. If ValueType is zero, the type is analog (double precision floating). 1 and 2 integer64 and binary variables (64 bit integers).
- # READING THE CURRENT VALUES OF VARIABLES
  The current value, timestamp in UTC and status for analog values can then be retrieved with:
  SELECT IDN, IDT, CVI, CVF, CSPT, CT_UTC, CS
  FROM CurrentValues
  WHERE (IDN \> 10314) AND (IDN \< 10329)
  
  The CSI means "status invalid" : 0 = OK, 1 = NOT OK.
  For integer variables, the result column is CVI instead of CVF :
  -- CSPT = 0 means that the value is float (CVF) and CSPT=1 means that it is
  -- integer (CVI). IDT is the variable name (this is a virtual result column
  -- that the ODBC driver reads from Variables.VariableName. However IDT is not
  -- indexed so it should not be used in WHERE predicate instead of IDN).
- # Determining the available history levels
  The names of the history tables can be listed with:
  
  SELECT HTNAM,TTYPE FROM HistoryTables WHERE ttype \<\> 15
  
  For example AVG1hour is the usual name for table that contains one hour average values.