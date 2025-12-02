Dit is de ODBC driver voor connectie met de VTRIN RTDB Historie database
         

For example AVG1hour is the usual name for table that contains one hour average values.
 
SELECT HTNAM,TTYPE FROM HistoryTables WHERE ttype \<\> 15
 
The names of the history tables can be listed with:

# Determining the available history levels
 
The CSI means "status invalid" : 0 = OK, 1 = NOT OK.  
For integer variables, the result column is CVI instead of CVF :  
-- CSPT = 0 means that the value is float (CVF) and CSPT=1 means that it is  
-- integer (CVI). IDT is the variable name (this is a virtual result column  
-- that the ODBC driver reads from Variables.VariableName. However IDT is not  
-- indexed so it should not be used in WHERE predicate instead of IDN).
 
The current value, timestamp in UTC and status for analog values can then be retrieved with:  
SELECT IDN, IDT, CVI, CVF, CSPT, CT_UTC, CS  
FROM CurrentValues  
WHERE (IDN \> 10314) AND (IDN \< 10329)

# READING THE CURRENT VALUES OF VARIABLES
 
The above example also reads the value type. If ValueType is zero, the type is analog (double precision floating). 1 and 2 integer64 and binary variables (64 bit integers).
 
```
SELECT        RowModificationTime, VariableId, VariableName, Description, "Section", Alias, DisplayFormat, Unit, SymbolGroup, Combined, Source, ValueType, BinaryTextId, ProcessArea, DiscreteValue, Created, Deleted,   
                         Connected, ProcessingMethod, ValueMaxF, ValueMinF, ValueMaxI, ValueMinI, SubstituteMethod, SubstituteValueF, SubstituteValueI, SubstituteVariable, RecordingMethod, CompressionMethod, CompressionError,  
                          ValueChangeReceiver, Events, PreventDisableOnInit, PreprocessingMethod, NoiseFilterFactor, NoiseFilterEnable, AnalogPower0, AnalogPower1, AnalogPower2, AnalogPower3, AnalogSquareRoot,   
                         AnalogZeroClamping, Inverted, PulseToEngineering, PulseLowLimit, PulseHighLimit, PulseEngineeringVariable, PulseDerivatedVariable, PulseWeight, PulseDerivatedCoefficient, PulseSensorVariable,   
                         ApplicationType, CalcActivation, StatisticsLimitFunction, StatisticsReferenceValueI, StatisticsReferenceValueF, PathId, Security, UserStatusId, SendOutputMode, ProducerTable, RowModificationTime_UTC,   
                         Created_UTC, Deleted_UTC, Variables_RowId, v_LongPath  
FROM            Variables  
WHERE        (Source = 0)




















```

# Opvragen van de Variabel Ids
 
Zie ook  
[RTDB SQL examples](Sibelco/800xA/VTRIN%20-%20Historie/RTDB%20SQL%20examples.md)
 
SELECT CurrentValues.IDN, CurrentValues.CT, CurrentValues.CVF, CurrentValues.IDT  
FROM CurrentValues CurrentValues  
WHERE (CurrentValues.IDN=10373)

## M5_TT120 value
 
SELECT Variables.VariableId, Variables.ValueType, Variables.VariableName  
FROM Variables Variables

# SQL queries (getest op eng client met excel)
   

Server: 10.32.29.60  
Database: DESSRVHIS1-RTDB  
User: tl  
Pw:

# ODBC instellingen