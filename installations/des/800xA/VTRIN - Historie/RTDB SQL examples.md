---
title: RTDB SQL examples
updated: [[2015-01-22]]T12:17:28.0000000+01:00
created: [[2014-10-16]]T14:18:18.0000000+02:00
---

--------------------------------------------------------------------------------
-- RTDB-SQL-Examples.txt
--
-- Description:
--
-- A white paper that contains examples how to access RTDB data by using
-- ODDB/SQL. This is a step by step guide. that has been organized as a
-- SQL script file (so that the syntax of the SQL examples can be verified)
--
-- See the RTDB Developer's Manual for more information (see chapters
-- "RTDB ODBC" and "Current value processing tables"). A copy of "RTDB
-- Developer's Manual" resides in the RTDB installation media in directory
-- \Document (and the latest draft in its "Latest Drafts" subfolder).
--
-- History:
--
-- 09-MAR-2007/Jari Kulmala
-- Original (Collected from various mail messages)
--
-- 11-DEC-2009/Jari Kulmala
-- Describe SimbaClient installation. Updatable \_All virtual table.
--
-- 15-JUL-2010/Jari Kulmala
-- Describe connection string syntax.
-- Reveal a the way now to make the DSN work in Vtrin Client computer
-- for all environments.
--------------------------------------------------------------------------------
-- 1. INSTALLING THE ODBC DATA SOURCE NAME
--
-- In the RTDB database server computer there are two different ODBC
-- data sources for the same database: for example: MY_RTDB and MY_RTDB_C32.
-- The difference between these are that MY_RTDB is a 1-tier DSN (uses
-- "RTDB-ODBC Driver" driver) and MY_RTDB_C32 is a 2-tier DSN
-- (uses "Simba Client" ODBC driver). It is recommended that applications use
-- the MY_RTDB_C32 -version. Using MY_RTDB requires admin rights and can be
-- harmful because it allows connection even if the database is shut down.
-- The application program must be capable of reconnecting if the connection
-- breaks (for example if the database is restarted).
--
-- The database can be accessed also from remote computers. In computers
-- where the RTDB Client (for example "Vtrin MY_RTDB" is installed, the
-- 2-tier data source MY_RTDB (yes, its name does not end with \_C32) is
-- available but only in the correct client environment, that is in the
-- Vtrin program started with the "Start/Programs/Abb Oy/Vtrin MY_RTDB"
-- command, or in a process started by that. Or in a command prompt window
-- started with "%SystemDrive%\RTDB CPM Client\Cmd_MY_RTDB.bat". The good
-- thing about this environment is that the driver software is automatically
-- update during each restart. If the data sources is needed also for other
-- environments, the oemcln32.dll file should be copied to a directory in
-- the PATH (from the local installation directory,
-- %LOCAL_APPDATA%\ABB Oy\\%APP_DSN%\bin) where LOCAL_APPDATA is the local
-- appdata directory (such as
-- "C:\Documents and Settings\Administrator\Local Settings\Application Data"
-- in Windows XP) and APP_DSN is the data source name.
--
-- If the RTDB Client is not needed at the client computer, A traditional
-- SimbaClient ODBC driver can also be installed. The setup kit for the
-- "SimbaClient" ODBC driver is available in the distribution DVD in folder
-- "\Misc\SimbaClient X.X". The installation requires administrator privileges
-- After installing, the ODBC DSN can be defined with ODBC control panel. You
-- need to know the database DSN name and database server IP address or
-- network name. Remember that if you have a 64-bit windows, you need to
-- start the ODBC control panel with command:
-- "%systemroot%\syswow64\odbcad32.exe"
-- Otherwise, the control panel shows only 64-bit drivers and defines only
-- 64-bit data sources (the SimbaClient ODBC driver is 32-bit). The
-- SimbaClient communicates with the "Simba Server" service in the RTDB server
-- computer by using the TCP/IP port number 1583.
--
-- When accessing the database with SimbaClient DSN, the ODBC connection string
-- has the format "DSN=datasource;UID=username;PWD=password"
--------------------------------------------------------------------------------
-- 2. CREATING NEW VARIABLES
--
-- These are examples how new variables are created. However, variables must
-- be created with the Excel Population application in actual RTDB projects.
--
{ Call CreateDatapoint('JAKU_EXAMPLE_A', '')};
{ Call CreateDatapoint('JAKU_EXAMPLE_STATUS', '')};
UPDATE Variables SET IDPT=2 WHERE VariableName='JAKU_EXAMPLE_STATUS';
{call SendCommand ('NotifyTableConfigChange', 'TableID=0', '', 0) };
--
--
--------------------------------------------------------------------------------
-- 3. GETTING INFORMATION ABOUT VARIABLES
--
-- All measurement, calculated, manual entered, or forecast data in the RTDB
-- database is stored as Variables. Each variable has a name, description,
-- engineering unit and other information. This information is stored in the
-- Variables table. The Variables table also contains a unique column
-- VariableID that is a 32-bit integer that is used as a foreing key to in
-- many tables. In most other tables name of the VariableId column is IDN.
--
--
SELECT VariableId,ValueType from Variables WHERE
VariableName='JAKU_EXAMPLE_A';
--
-- The above example also reads the value type. If ValueType is zero, the type
-- is analog (double precision floating). 1 and 2 integer64 and binary
-- variables (64 bit integers).
--
-- If you want to list measured variables from OPC-client, you can select

SELECT VariableName FROM Variables WHERE Source=64;

-- or the calculated variables with Source=1 or the manual entries
-- with Source=2.
--
--
--
--------------------------------------------------------------------------------
-- 4. READING THE CURRENT VALUES OF VARIABLES
--
--
-- The current value, timestamp in UTC and status for analog values can then
-- be retrieved with: (assuming variable id 10008 for example)

SELECT CVF, CT_UTC,CSI FROM CurrentValues WHERE IDN=10008;

--
-- The CSI means "status invalid" : 0 = OK, 1 = NOT OK.
-- For integer variables, the result column is CVI instead of CVF :
--

SELECT CVI, CT_UTC,CSI FROM CurrentValues WHERE IDN=10009;

-- If you need to read all (or almost all) variables, you may consider:

SELECT IDN,IDT,CVI,CVF, CSPT,CT_UTC,CSI FROM Currentvalues;

-- CSPT = 0 means that the value is float (CVF) and CSPT=1 means that it is
-- integer (CVI). IDT is the variable name (this is a virtual result column
-- that the ODBC driver reads from Variables.VariableName. However IDT is not
-- indexed so it should not be used in WHERE predicate instead of IDN).
--
--------------------------------------------------------------------------------
-- 5. PRODUCING CURRENT VALUES OF VARIABLES
--
-- Current values must be produced with a separate stored procedure.
-- For example:

{ Call ProduceCurrentValue('JAKU_EXAMPLE_STATUS', 1, NULL(), '', 0)};

--
--------------------------------------------------------------------------------
-- 6. READING HISTORICAL DATA OF VARIABLES
--
--
-- RTDB stores the measured current values to history table called
-- CurrentHistory (perhaps compressed by omitting values that are not
-- needed if interpolated values result to good enough estimate).
-- This table is always present in RTDB databases.
-- However, the length (in time range) of the table is usually restricted.
-- In most installations, the RTDB database has been configured to collect
-- average values from measurement data. The names of the history tables
-- are not fixed (however, there is a naming convention for them).
--
-- The architecture of history data is "long and narrow", so that one row
-- contains value for one period and one variable.
--
-- Also forecast data is stored in similar kind of tables.
--
--
--
-- 6.1 Determining the available history levels
--
-- The names of the history tables can be listed with:

SELECT HTNAM,TTYPE FROM HistoryTables WHERE ttype \<\> 15;

-- For example AVG1hour is the usual name for table that contains one hour
-- average values.
--
--
-- 6.3 Getting data with \_REP -query
--
-- The \_REP query guarantees that it returns history periods using
-- constant time intervals. Vast tijdsinterval
--

select rep_begtim_utc,rep_aveval,rep_valid_length from AVG1hour_rep where
idn=10017 and
rep_begtim_utc\>={ ts '[[2007-01-16]] 22:00:00'} and
rep_begtim_utc\<{ ts '[[2007-01-17]] 22:00:00'} and
rep_resolution_secs=3600;

--
--
-- 6.4 Getting data with \_PLOT -query
--
-- The \_PLOT query can be used to restrict size of the result set according
-- to the given resolution. Vast aantal punten
--

select plot_ix_utc,plot_iy,plot_isi from AVG1minute_plot where
idn=10017 and
plot_begtim_utc = { ts '[[2007-01-16]] 22:00:00'} and
plot_endtim_utc = { ts '[[2007-01-17]] 22:00:00'} and
plot_resolution_pixels=1000;

--
--
-- 6.5 Getting data from physical history tables
--
-- CAUTION: The RTDB history data should be read by using the \_REP and \_PLOT
-- techniques instead by reading from the physical tables because in future
-- versions the organization of data in the history tables can change.
--
-- The most important columns are:
--
-- IDN INTEGER : the variable IDN number
-- HT_UTC TIMESTAMP : the UTC timestamp of the beginning time of the hour
-- period
-- HVF DOUBLE : The value. There is also an overlaid column HVI of type
-- int64 but average history uses only HVF
-- HSI BIT : The invalid data HSI=1 means that the value is invalid
-- HSHS BIT : HSHS=1 means that the value has been manually entered
-- and should not be overwritten.
-- HSVT BIT : HSVT=1 means that the value is "discrete" instead of
-- "linear" (all average values are "discrete", though)
-- HSPT BIT : HSPT=1 means that the value is int64 instead of double
-- (all average values are double, though)
--
-- Please note:
-- The physical table (e.g. AVG1hour) contains only two latest periods.
-- We say that the table is the "head" part. Older histories are stored to
-- separate "split" tables with name "TABLENAME xxx", where xxx is a timestamp
-- in a certain format. If you want to fetch data from the complete history,
-- you need to use the table name "TABLENAME_All". This is a kind of view that
-- presents data from all "split" history parts and also from the "active"
-- part. (Before RTDB 4.2 the physical table was so called "active" part
-- of history and it typically contained more than two periods).
-- Note: the \_All implementation in RTDB 4.2 does NOT support iteration
-- through multiple IDN numbers. (Follow the release notes for updated
-- information).
--
-- 6.5.1 Retrieve 1 hour forecast values
--
-- The columns are identical as in the average history case. Also FOR1hour by
-- definition contains only discrete data, so it is expected that HSVT
-- is always 1.
-- Forecast history may contain also integer type variables (i.e. where
-- HSPT=1), in which case the value must be read from HVI instead of HVF.
-- However, most often the forecast data contains only double data type.
--
--

SELECT HT_UTC,HVF,HSI,HSHS,HSVT,HSPT FROM FOR1hour WHERE Idn=10652 AND
HT_UTC\>={ ts '[[2006-02-02]] 22:00:00'} and
HT_UTC \< { ts '[[2006-02-03]] 22:00:00'};

-- 6.5.2 Retrieve 1 hour forecast values from the scenario 1
--
-- Scenario data is present in the database in a special way in two different
-- tables: FOR1hour contains the "base" data, and FOR1hour_Sc\* (where \* is a
--------------------------------------------------------------------------------
-- number) contains only that data that differs from the base data. Because a
-- data sample in the the history table is always considered to continue until
-- the next sample, the scenario table uses a special bit HSLIS to indicate
-- the "last in sequence" sample. The special SQL table FOR1hour_Sc\*\_Comb
-- is a kind of view that combines data from the FOR1hour and FOR1hour_Sc\*
-- -tables.
--
--

SELECT HT_UTC,HVF,HSI,HSHS,HSVT,HSPT FROM FOR1hour_Sc1_Comb WHERE
Idn=10652 AND
HT_UTC\>={ ts '[[2006-02-02]] 22:00:00'} and
HT_UTC \< { ts '[[2006-02-03]] 22:00:00'};

--------------------------------------------------------------------------------
-- 7. AUTOFLUSH
--
-- Before performing massive amount of INSERT or UPDATE commands, consider
-- to turn off automatic flush for performance reasons.
--

{ call SetDatabaseOptions('AUTOFLUSH=0') };

--
-- To turn the statement-wise flushing on again:

{ call SetDatabaseOptions('AUTOFLUSH=1;ClearCache=ALL') };

--
-- This instructs the ODBC driver to flush all changes to disk and to close
-- all cached tables. If this is not done, the modification can be lost if the
-- computer crashes. This is not needed if you close the ODBC connection now.
--
--------------------------------------------------------------------------------
-- 8. UPDATING HISTORICAL DATA OF VARIABLES
--
-- 8.1 Updating historical data
--
-- The stored procedure ProduceHistoryValue is a simple way to update
-- history values. The same procedure can be used to retrieve values for
-- getting the default values for the update.
--

{ call ProduceHistoryValue('MYVAR', 'AVG1minute',
{ ts '[[1999-11-11]] 11:20:00' },
{ ts '[[1999-11-11]] 11:50:00' },
10.0, 20.0, 2, 0, '') };

--
-- The stored procedure UpdateHistory has more capabilities. Also the user
-- id and a comment can be provided in the update.
--

{ call UpdateHistory(10001, NULL(), 0, 0, 1, 2, 15, 0,
'6521b234-7d13-42d3-9646-9f018b63d8da', 'AVG1minute', NULL(), NULL(),
NULL(), 'Test update', '', 0,
{ ts '[[2005-03-17]] 06:00:00'},
{ ts '[[2005-03-17]] 09:00:00'},
NULL(), NULL(),
'123.4', '234.5', NULL(), 1, '') };

--
--
-- 8.2 Updating data in the physical history tables
--
-- CAUTION: you should NOT use the INSERT and UPDATE commands to update
-- data in physical tables instead you should use the stored procedure
-- UpdateHistory or its older version ProduceHistoryValue. This is because
-- the history compression rules must be known by the application if it
-- updates physical tables directly (including the \_All virtual table).
-- Starting from RTDB 4.2, the target table name for the modification
-- statemets can also be \_All. Before that version, the \_All virtual table
-- was not updatable, and it was very difficult to perform history writes
-- if the history table used splitted storing (which is the usual way).
-- Starting from RTDB 4.2, the plain history table name (without \_All suffix)
-- means the "head" table, which contains only two newest periods.
--
-- The application must check the HSHS value and if it is 1, the application
-- must leave the value as it is. If you are interested only for samples
-- where HSHS=1, you can add that to the WHERE predicate.
--
SELECT HT_UTC,HVF,HSI,HSHS,HSVT,HSPT FROM AVG1hour_all WHERE Idn=10652 AND
HT_UTC\>={ ts '[[2006-02-02]] 22:00:00'} and
HT_UTC \< { ts '[[2006-02-03]] 22:00:00'};

-- 8.2.1 inserting new data
--
-- HSVT must be set to 1 because by definition, average
-- values are always discrete. The invalid-status-bit (HSI) does not need to
-- be set here because its default value is 0 (also the default value of
-- HSPT is 0).
-- Note that existing data must be updated by using UPDATE statements,
-- while new data must be entered with INSERT statements.
--
INSERT INTO AVG1hour_All(IDN,HT_UTC,HVF, HSVT) VALUES (10652, { ts '[[2006-02-02]] 22:00:00'}, 100.0, 1);
INSERT INTO AVG1hour_All(IDN,HT_UTC,HVF, HSVT) VALUES (10652, { ts '[[2006-02-02]] 23:00:00'}, 100.1, 1);
INSERT INTO AVG1hour_All(IDN,HT_UTC,HVF, HSVT) VALUES (10652, { ts '[[2006-02-03]] 00:00:00'}, 100.2, 1);
INSERT INTO AVG1hour_All(IDN,HT_UTC,HVF, HSVT) VALUES (10652, { ts '[[2006-02-03]] 01:00:00'}, 100.3, 1);
--
-- 8.2.2 Updating existing data.
--
-- HSI=0 is here only in case that the old data is invalid.
--

UPDATE AVG1hour_All SET HVF=200.0, HSI=0 WHERE IDN=10652 AND HT_UTC={ ts '[[2006-02-02]] 22:00:00'};
UPDATE AVG1hour_All SET HVF=200.1, HSI=0 WHERE IDN=10652 AND HT_UTC={ ts '[[2006-02-02]] 23:00:00'};

--
--
-- 8.2.3 Insert new data to forecast
--

INSERT INTO FOR1hour_All(IDN,HT_UTC,HVF, HSVT) VALUES (10652, { ts '[[2006-02-02]] 22:00:00'}, 100.0, 1);
INSERT INTO FOR1hour_All(IDN,HT_UTC,HVF, HSVT) VALUES (10652, { ts '[[2006-02-02]] 23:00:00'}, 100.1, 1);
INSERT INTO FOR1hour_All(IDN,HT_UTC,HVF, HSVT) VALUES (10652, { ts '[[2006-02-03]] 00:00:00'}, 100.2, 1);
INSERT INTO FOR1hour_All(IDN,HT_UTC,HVF, HSVT) VALUES (10652, { ts '[[2006-02-03]] 01:00:00'}, 100.3, 1);

--
-- 8.2.4 Insert new data to scenario 1
--
--
INSERT INTO FOR1hour_Sc1_All(IDN,HT_UTC,HVF, HSVT, HSLIS) VALUES (10652, { ts '[[2006-02-02]] 23:00:00'}, 200.1, 1, 0);
INSERT INTO FOR1hour_Sc1_All(IDN,HT_UTC,HVF, HSVT, HSLIS) VALUES (10652, { ts '[[2006-02-03]] 00:00:00'}, 200.2, 1, 1);
--
--
--------------------------------------------------------------------------------
-- 9. PRODUCING DIAGNOSTIC INFORMATION
--
-- Example how an application can produce error information. The example
-- variable JAKU_EXAMPLE_STATUS is binary variable with values 0/1 = Fail/OK.
-- The application can produce value 1 to this variable whenever its operation
-- has been successful. In case of failure, it should produce value 0 to it.
--

{ Call ProduceCurrentValue('JAKU_EXAMPLE_STATUS', 1, NULL(), '', 0)};

--
--
--------------------------------------------------------------------------------
