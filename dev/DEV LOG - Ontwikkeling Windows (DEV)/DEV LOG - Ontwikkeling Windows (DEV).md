---
date created: 2016-11-25 00:00
modified: 2025-09-15 10:42
---
# Ontwikkeling voor Windows (C#, Python, Jupyter, SQL, Node, Node-Red) #remember-for-later
 
# 25/11/2016 14:54

Nog eens verder gewerkt aan TTool.
 
=\> Werk maken van de data opkuis. Zie
 
Excel [https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/Documents/Energy/Datalog%20Tags.xlsx?d=w3eaa20dbcbe34bf68a88fc48258ba4b7](https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/Documents/Energy/Datalog%20Tags.xlsx?d=w3eaa20dbcbe34bf68a88fc48258ba4b7)
   

# 28/11/2016 12:53

Opbouw van een Log-tabel  
CREATE TABLE [dbo].[ABBDatalog_Perslucht2](  
[tagID] [int] NOT NULL,  
[dts] [datetime2](7) NOT NULL,  
[value] [float] NULL,  
CONSTRAINT [PK_Perslucht2] PRIMARY KEY CLUSTERED  
(  
[tagID] ASC,  
[dts] ASC  
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]  
) ON [PRIMARY] 
# 28/11/2016 16:32

Omzettingen van logtabellen: gebleven bij  
INSERT INTO ABBDatalog_Energy  
SELECT (SELECT TOP (1) ID FROM ABB_TAG_ID WHERE tag = 'S_KWHM6_7_PM_ActEngImpT1'), timestamp, S_KWHM6_7_PM_ActEngImpT1  
FROM DATALOG_TOTAL_1M b  
WHERE S_KWHM6_7_PM_ActEngImpT1 IS NOT NULL
 
# 19/12/2016 8:42

Niks bijzonders te melden. Bekijk de wijzigingen in Git.
 
# 11/04/2019
De DEV-directory
D:\OneDrive - Sibelco\DEV
 
# 9/05/2019

## Installatie van Python (3.7.3)
De installatie avn Python detecteerd al een Python installatie van Visual Studio.  
Ervoor gekozen om deze te upgraden.
 
Bij de installatie zit ook pip
 
==\> Rechtstreeks uitvoeren van pip lukt niet.
 
Terug Azure Data Studio geïnstalleerd.
 
# 2/08/2019

Team foundation server is omgezet naar devops dev.azure.com  
   
Op account tonny.lemmens@sibelco.com is niks, alles staat op tonnylemmens@outlook.com  
   
De DEV-directory bevat 3GB en is te groot om in OneDrive - Personal te zetten.  
   
=\> Zo veel mogelijk van de code in devops zetten  
   
Op Engineering Station maak gebruik van OneDrive-Sibelco.  
En niet dmv een mapping naar [\\tsclient\D\Onedrive - Sibelco](file:///\\tsclient\D\Onedrive%20-%20Sibelco)  
   
Opmerking: Onedrive op engineering (en ook oursibelco) is zeer traag.  
Maar een grote HDA export op Eng naar [\\tsclient\d](file:///\\tsclient\d) nam meer dan twee uur in beslag (1GB). Lokaal enkele minuten.  
 

# 3/11/2019

Visual Studio op MSI geïnstalleerd
 
# 5/11/2019

UWP en .NET Core 3.0 is the way to go voor Windows  
-\> Betere performance en universeler
 
Al een eerste poging gewaagd om in XAML een binding te doen.
 
In de XAML  
\<Grid\>  
\<Button Content="Button" Height="118" Margin="252,125,0,0" VerticalAlignment="Top" Width="206"/\>  
\<TextBlock HorizontalAlignment="Left" Height="109" Margin="252,296,0,0" ==Text="{x:Bind Half(100.0)}"== TextWrapping="Wrap" VerticalAlignment="Top" Width="297"/\>
 
\</Grid\>
 
In de Code  
public double ==Half==(double value) =\> value / 2.0;
 
[https://docs.microsoft.com/en-us/windows/uwp/data-binding/function-bindings](https://docs.microsoft.com/en-us/windows/uwp/data-binding/function-bindings)
 
[https://docs.microsoft.com/en-us/windows/uwp/data-binding/function-bindings#two-way-function-bindings](https://docs.microsoft.com/en-us/windows/uwp/data-binding/function-bindings#two-way-function-bindings)  
**Two way function bindings**  
In a two-way binding scenario, a second function must be specified for the reverse direction of the binding. This is done using the **BindBack** binding property. In the below example, the function should take one argument which is the value that needs to be pushed back to the model.  
XAML  
\<TextBlock Text="{x:Bind a.MyFunc(b), ==BindBack=a.MyFunc2, Mode=TwoWay==}" /\>
 \> Van \<[https://docs.microsoft.com/en-us/windows/uwp/data-binding/function-bindings#two-way-function-bindings](https://docs.microsoft.com/en-us/windows/uwp/data-binding/function-bindings#two-way-function-bindings)\>   
# 10/12/2019

Om code met syntax highlighting te kunnen copy pasten, moet de Extension 'Copy as HTML' worden geïnstalleerd.
 
# Binding met een Dictionary

Voorzie een dictionary in de MainWindow (en voeg enkele fields toe). Vergeet niet DataContext in te stellen  
public partial class MainWindow : Window￼{￼    Dictionary\<string, object\> _data = new Dictionary\<string, object\>();￼ ￼    public MainWindow()￼    {￼        InitializeComponent();￼ ￼        _data["field1"] = new OPC("Tonny", "Lemmens");￼        _data["field2"] = "John Doe";￼ ￼        string t = "field3";￼        _data[t] = DateTime.Now;￼ ￼        this.DataContext = _data;￼    }￼}
 
## Custom UserControl code

Object OPC bevat twee string-velden: FirstName en LastName
 
public OPC Motor￼        {￼            get { return (OPC)GetValue(MotorProperty); }￼            set { SetValue(MotorProperty, value); }￼        }￼ ￼        // Using a DependencyProperty as the backing store for MyProperty.  This enables animation, styling, binding, etc...￼        public static readonly DependencyProperty MotorProperty =￼            DependencyProperty.Register("Motor", typeof(OPC), typeof(UserControl2), new PropertyMetadata(new OPC("VN","LN")));
   

## Custom UserControl xaml

\<Grid\>￼   \<TextBox HorizontalAlignment="Left" Height="22" Margin="10,0,0,0" TextWrapping="Wrap"   
Text="{Binding Motor.FirstName, ElementName=Venster}" VerticalAlignment="Top" Width="180"/\>￼        \<TextBox HorizontalAlignment="Left" Margin="10,27,0,10" TextWrapping="Wrap"   
Text="{Binding Motor.LastName, ElementName=Venster}" Width="156"/\>￼    \</Grid\>
   

# Faceplates in WPF

Code om een Window te openen en om het openstaande window te sluiten.  
Indien een window wordt geclosed, moet deze op null worden gezet.  
private void Button1_Click(object sender, RoutedEventArgs e)￼        {￼            if (window3 == null)￼            {￼                window3 = new Window3￼                {￼                    Topmost = true￼                };￼            }￼ ￼            if (myOwnedWindow != null)￼            {￼                myOwnedWindow.Close();￼                myOwnedWindow = null;￼            }￼            window3.Show();￼        }￼ ￼        private void Button_Click(object sender, RoutedEventArgs e)￼        {￼            if (myOwnedWindow == null)￼            {￼                myOwnedWindow = new Window2();￼                myOwnedWindow.Topmost = true;￼            }￼            if (window3 != null)￼            {￼                window3.Close();￼                window3 = null;￼            }￼            myOwnedWindow.Show();￼        }
   

# 16/12/2019

# Scaling in WPF

Gebruik een Viewbox ipv Grid
 
# 24/12/2019

Custom Classes moet de Observable Class implementeren
 
public class Observable : INotifyPropertyChanged￼    {￼        public event PropertyChangedEventHandler PropertyChanged;￼ ￼        protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)￼        {￼            var handler = PropertyChanged;￼            if (handler != null)￼            {￼                handler(this, new PropertyChangedEventArgs(propertyName));￼            }￼        }￼ ￼        protected virtual bool SetProperty\<T\>(ref T storage, T newValue, [CallerMemberName] string propertyName = null)￼        {￼            if (object.Equals(storage, newValue)) return false;￼            storage = newValue;￼            OnPropertyChanged(propertyName);￼            return true;￼        }￼    }
   

Bijvoorbeeld  
public class StringObservable: Observable￼    {￼        private string v;￼ ￼        public StringObservable(string v)￼        {￼            this.v = v;￼        }￼ ￼        public string Value￼        {￼            get { return v; }￼            set￼            {￼                SetProperty(ref v, value);￼            }￼        }￼    }
    
# 28/01/2020

TTools opgekuist.
 
Afgelopen dagen nog eens wat getest om een Peer tabel opgezet te krijgen.  
==CONCLUSIE: Als er teveel records in een tabel zitten, is het niet meer werkbaar met SQL SERVER.==
 
=\> Tabel "datalog_calc" aangemaakt.

|   |   |   |   |   |
|---|---|---|---|---|
|Log periode|ptn per dag|ptn per week|ptn per maand|ptn per jaar|
|1 minuut|1440|10080|44640|525600|
|5 minuten|288|2016|8928|105120|
|15 minuten|96|672|2976|35040|
 
# 29/01/2020

De hoeveelheid gegevens blijft een probleem voor de laadtijd in power bi.
 
Het laden van een tabel met metingen met een miljoen records duurt lang.
 
Oplossing: gebruik Parameters in Power bi  
Een parameter kan aanpassen in een rapport via

![Help gevens Indeling Gegevensanalyseren Query s Ve...](Exported%20image%2020250721193429-0.png)  

De parameter (begindts) kan je in de query gebruiken om het aantal records te beperken
 
# 4/02/2020

Het joinen van de DIFF tabellen van alle metingen duurt te lang. Zelfs met beperking van gegevens.
 
Het joinen van 13 tabellen met resultaat 13000 records duurt al 25 seconden.  
Het joinen van 13 tabellen met resultaat 130000 records duurt 24 seconden
 
Het joinen van 23 tabellen met resultaat 130000 records duurt 44 seconden  
Het joinen van 23 tabellen met resultaat 13000 records duurt 20 seconden
 
=\> Verder doen met opvullen datalog_calc
 
Test met datalog_calc:  
Opgevuld met 3 500 000 datums
 
Select count(*) duurt 1 seconde  
SELECT Min(dts)  
FROM datalog_Calc  
Group by dateadd(mi, datediff(mi, 0, dts) / (24*60) * (24*60), 0)  
Duurt 3 seconden
 
# 9/02/2020

Had natuurlijk geen index op dts liggen loempe.
 
**31/01/2021**  
Even de programmeertalen vergelijken.  
Afhankelijk van de projecten in github.  
   
Golang is simpel en snel. Vooral ingebouwde concurrency (goroutines) zijn veelbelovend. Maar heeft toch veel nadelen  
   
Since the Go programming language is simple, you won’t find popular features like inheritance; there’s only composition. There are also no numerations, only groups of constants. Additionally, Golang doesn’t support overloaded functions. For containers, there’s only slice arrays and named lists (maps). There are no exceptions, but Go provides an opportunity to return multiple values that contain the error objects. There are also no compilation warnings, only errors. Memory can be managed via the garbage collector or manually, using the unsafe package.  
 

|   |   |   |   |
|---|---|---|---|
||**C#**|**Python**|**JS**|
|OPC DA|37 github projecten|21 github projecten|12 github projecten|
|Pandas (resample)  <br>resample is een belangrijke feature om rapporten te berekenen|DataFrame bestaat in ML.Net maar is summier. Geen timeserie functionaliteit gevonden  <br>De Deedle bibliotheek is ook niet intuitief. Vooral op F# toegelegd.  <br>   <br>31/03/2021 : Voorlopig geen fatsoenlijke vervanger voor Pandas in C# gevonden  <br>   <br>23/08/2021 : Nog met Deedle geëxperimenteerd. F# is niet zomaar aan te roepen vanuit C#|+|niet gevonden|
|||||
   

# 31/03/2021

Overweging om Pandas zelf in C# te maken.   Dit is een test script om de verschillende collections te vergelijken  
static void Main(string[] args)  
{  
Dictionary\<DateTime, Double\> dic = new Dictionary\<DateTime, Double\>();  
Stopwatch sw = new Stopwatch();  
sw.Start();  
   
int n = 100000000;  
   
for (int i = 0; i \< n; i++)  
{  
dic.Add(RandomDate(), random.NextDouble());  
}  
   
sw.Stop();  
Console.WriteLine("Elapsed={0}", sw.Elapsed);  
Console.WriteLine("Einde");  
Console.ReadLine();  
}
 
# RANDOM INSERT

n = 10 000 000

|   |   |   |   |
|---|---|---|---|
|## Collection|## Runtime|## Mem usage in debugger||
|Dictionary|4.13s|686 MB||
|SortedDictionary|33.24s|871 MB||
|SortedList|Veel te traag|||
|C5.TreeDictionary|40.17s|1 GB||
|C5.HashDictionary|20.5s|1.2 GB||
|Dictionary -\> SortedDictionary|28.1s|1 GB||
|List met initiële capaciteit|3.11s￼na sort 5.66s|190 MB||
|MS DataFrame|8.8s|367 MB|biblitheek is niet volledig uitontwikkeld  <br>Veel methods bevatten een NotImplementedException￼￼8/09/2021 : nog eens geprobeerd. ￼Een Dataframe sorteren kan met OrderBy|
|Daany|6,48s|823 MB||
|Combinatie index met kolomlijst - 1 kolom￼  <br>private Dictionary\<DateTime, int\> index = new Dictionary\<DateTime, int\>();  <br>private List\<List\<double\>\> ll = new List\<List\<double\>\>(10000000);|3.83s|1003 MB||
|Combinatie index met kolomlijst - 3 kolommen￼  <br>private Dictionary\<DateTime, int\> index = new Dictionary\<DateTime, int\>();  <br>private List\<List\<double\>\> ll = new List\<List\<double\>\>(10000000);<br><br>  <br><br>en met 3 kolommen|4.68s|1.3 GB||
|Dictionary\<DateTime, List\<double\>\> values = new Dictionary\<DateTime, List\<double\>\>();  <br>3 kolommen|6.26s|1.4GB||
|Dictionary\<DateTime, List\<double\>\> values = new Dictionary\<DateTime, List\<double\>\>();  <br>100 kolommen|18s|9.3 GB|100 kolommen * 10000000 =  <br>1 000 000 000 values|
|Dictionary\<DateTime, List\<double\>\> values = new Dictionary\<DateTime, List\<double\>\>();  <br>100 kolommen|61s|29.5 GB|100 kolommen en 1 seconde voor een heel jaar 31 536 000|
|Een List\<DateTime\>|1.33s|295 MB||
|Een List\<object\>|2.7s|521 MB||
|Een List\<double\>|1.45s|296 MB||
|Een List\<Single\>|1.09s|153 MB||
|Een Dictionary\<DateTime,int\>|5.88s|680 MB||
|MS PrimitiveDataFrameColumn\<double\> met PrimitiveDataFrameColumn\<long\> want DateTime is niet gesupporteerd|70s|1,7 GB||
 
# 8/04/2021

Geprobeerd om de ABB_HDA dll en de OPC Foundation HDA dll in een .NET Core 5.0 omgeving te laten werken.  
Foundation dll werkt enkel in x86 .NET Framework, niet met Core.
 
Geprobeerd met x64, x86, MultitargetFrameworks, Foundation Nuget packages
 
Hou deze website in het oog voor eventuele updates  
[https://opcfoundation.org/forum/classic-opc-da-ae-hda-xml-da-etc/](https://opcfoundation.org/forum/classic-opc-da-ae-hda-xml-da-etc/)
 
# 9/04/2021

GELUKT met de foundation Nuget packages! In x64 en Core 5.0
 
~~Afvoeren van YAML. Dit zit niet standaard in .Net~~
 
# 4/07/2021

Even geëxperimenteerd met Deedle. Toch nog even een kans geven
 
# 9/07/2021

~~In JSON is geen commentaar toegestaan. Dus toch Yaml ? =\> NEE~~  
1/03/2022 : Een tijdje terug geprobeerd om Pandas in C# te krijgen. Dit bleek niet haalbaar. Het nadeel dat Yaml niet in C# valt dus weg.  
DUS YAML

![configyml UselnEnergyCa1cu1ation true Log Logl Nam...](Exported%20image%2020250721193429-1.png)  

Er loopt nog veel fout met het importeren van data uit ABB  
=\> Online en Historical data combineren
 
Voorbeeld nieuw Model:  
Connections
 
Tag  
Signal  
OnlineDA data  
Source,  
DA-path  
Historical data  
Source,  
HDA-path  
Log1, Log2  
Total signal  
Import  
Current Import  
DA-path  
Historical  
HDA-path  
Log1, Log2  
Export  
Current export  
DA-path  
Historical  
HDA-path  
Log1, Log2
 
# 29/07/2021

Bij TTools2 Dynamic Loading en Unloading toegevoegd
 
**SIGNAL**  
~~Een signal kan 2 verschillende bronnen hebben: Online en Stored on Disk (HDA)~~  
~~Elke Source heeft deze eigenschappen~~  
~~Connection~~
 
Misschien het model van UaModeler gebruiken (in VMWare Automation Tools)  
In het _Server_ object zitten meedere NodeClasses

![Information Model Displayname Objects Aliases Find...](Exported%20image%2020250721193430-2.png)  

Een variabele heeft

![Instance Type Defin bon Modelling Rule Data Type V...](Exported%20image%2020250721193430-3.png)   
# 30/07/2021

In JSON kan je een array hebben of een opsomming van objecten.  
Voorbeeld array:  
"array": [  
"22",  
{  
"Name": 66  
},  
{  
"Type": "OPC_HDA",  
"Server": "opchda://ABB.AdvHtHistorySrv.1"  
}  
],
 
Voorbeeld Opsomming:  
"obj1": {  
"Name": "test"  
},  
"obj2": {  
"Name": "test"  
},
 
Bij een opsomming moeten unieke namen  
**The names within an object SHOULD be unique.**
 
Bij zowel een array als een opsooming moet het Object-type gespecifieerd worden =\> Keuze= Opsomming
 
JSON is dé manier om met configuratie bestanden te werken.
 
Nog kiezen voor 1 grote config file, of opsplitsen in AppSettings.json en Config.json
 
Oplossing zoeken om dit te kunnen doen  
// Connections  
OpcDaConnection dAConnection = new OpcDaConnection("OPC_DA");  
OpcHdaConnection hdaConnection = new OpcHdaConnection("OPC_HDA");  
config.connections.Add(dAConnection);
 
# 11/08/2021

[Design Patterns (refactoring.guru)](https://refactoring.guru/design-patterns)  
Lees Composite pattern
 
# 15/08/2021

SCR_1 (SentronPac)  
UnitPath = Applications.HSK15_1.HSK151_Energy.SentronPacs.SCR1_PM_  
Total Active Power (Property)  
_OPC_  
DataCollection (1 keer per minuut)  
HDALogs  
Active Energy Import (Property)  
Active Energy Export (Property)
 
# 16/08/2021

DataSource en Model moet uiteen worden getrokken
 
ABB_DA_HDA_Source  
OPC_Server  
UnitPath  
Property  
Logs
   

## DataSource

SCR_1  
type = SentronPac
 
TotalActivePower  
OPC_Server  
UnitPath  
Property  
Logs
 
ActiveEnergyImport  
OPC_Server  
UnitPath  
Property  
Logs
 
## OPC UA Model

SCR_1 : SCR_1  
SCR_1 : {  
ActiveE
 
# 18/08/2021

Nog maar eens geëxperimenteerd met Deedle, maar ik krijg de Resampling niet in orde.
 
TPandas in orde maken.  
Denk aan

- geheugengebruik
- snelheid
- Resampling
- Operator +, -
- Enkel 1 kolom, of toch meerdere kolommen.
 
# 2/09/2021
Microsoft.Data.Analysis DataFrame is niet af
veel methods not implemented
 
# 3/09/2021
geheugen gebruik
aantal = 1 000 000 000;

|   |   |
|---|---|
|DateTime|8.2 GB|
|Int16|2.1 GB|
|Int32|4.1 GB|
|Int64|8.2 GB|
|DateTimeOffset|16.5 GB|
|double|8.2 GB|
|dictionary\<datetime, int\>||
|ML.NET DataFrame|6/11/2021 : Niet gebruiken|
 
# 15/10/2021
Vergelijking van Python en C# voor het bouwen van een reporting tool

|                |                                                                                                                                     |                                                                                                                        |           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------- |
|                | # Python                                                                                                                            | # C#                                                                                                                   |           |
| PlotLib        | Heeft een uitgebreide plot bibliotheek  <br>[Matplotlib: Python plotting — Matplotlib 3.4.3 documentation](https://matplotlib.org/) | Lijkt ook een plot blibliotheek te hebben ￼[ScottPlot - Interactive Plotting Library for .NET](https://scottplot.net/) | gelijk    |
| Web framework  | Flask wordt gebruikt voor eenvoudige websites                                                                                       | geen idee welke het meest geschikt                                                                                     | geen idee |
| Data crunching | Python defacto standaard om grote data te verwerken                                                                                 | Enkel ML.NET lijkt geschikt                                                                                            | Python    |
| Snelheid       | Snelheid van Pandas is zeer goed, maar het doorlopen van een zéér traag                                                             | Snelheid is top, en multithreading is mogelijk                                                                         | C#        |
| debugging      | is moeilijk                                                                                                                         | makkelijker                                                                                                            | C#        |
| taal           | komt ongestructureerd over                                                                                                          | programming taal is op lijkt op alle vlakken beter                                                                     | C#        |
|                |                                                                                                                                     |                                                                                                                        |           |

# 5/11/2021
De machine learning bevat een nieuwere uitgebreidere versie van DataFrame dan CorefxLab
[machinelearning/src/Microsoft.Data.Analysis at main · dotnet/machinelearning (github.com)](https://github.com/dotnet/machinelearning/tree/main/src/Microsoft.Data.Analysis)
[dotnet/corefxlab: This repo is for experimentation and exploring new ideas that may or may not make it into the main corefx repo. (github.com)](https://github.com/dotnet/corefxlab)
Zie DataFrame [machinelearning/src/Microsoft.Data.Analysis at main · dotnet/machinelearning (github.com)](https://github.com/dotnet/machinelearning/tree/main/src/Microsoft.Data.Analysis)
 
# 6/11/2021
De Microsoft DataFrame namaken is te moeilijk
 
# 8/11/2021
In TestPandas.cs _SUM Month_ verder uitwerken
 
# 13/11/2021

Na wat experimenteren met (abstract) classes, inheritance tot de conclusie gekomen dat elk datatype best zijn eigen class krijgt.  
Dus geen DataFrameColumn\<T\> gebruiken.  
Dit geeft gigantisch veel werk.
 
Dit krijg je niet compiled  
public class Gen\<T\>  
{  
public T Plus\<T\>(T par1, T par2)  
{  
return par1 + par2;  
}  
}
 
Generics kunnen niet worden gebruikt.
 
public abstract partial class TAbstractDataFrameColumn : IEnumerable
 
# 15/11/2021
[Link naar een Fijn stukske code](dev/dev%20languages/C-sharp/Fijn%20stukske%20code%201.md)
int n = 1_000_000_000;

|   |   |   |
|---|---|---|
|LIST\<\>||nullable|
|DateTime|8.2 GB|16.5 GB|
|Int16|2.1 GB|4.1 GB|
|Int32|4.1 GB|8.2 GB|
|Int64|8.2 GB|16.5 GB|
|double|8.2 GB|16.5 GB|
|object|opgevuld met 1.234 33.2 GB  <br>opgevuld met 1234 8.4 GB||
 
# 19/11/2021

Bezig met omzetten Test_Peer.  
=\> todo: DataFrame Join
 
# 25/11/2021
Performantie verschil ForEach en For..Next

int n = 1000000000;  
   
List\<DateTime\> list = new List\<DateTime\>();  
   
Stopwatch sw = new Stopwatch();  
sw.Start();  
   
Console.WriteLine("Fill random datetime");  
for (int i = 0; i \< n; i++)  
{  
list.Add(new DateTime(rnd.NextInt64(DateTime.MinValue.Ticks, DateTime.MaxValue.Ticks)));  
}  
Console.WriteLine("Elapsed={0}", sw.Elapsed);  
   
DateTime x;  
   
Console.WriteLine("Foreach");  
sw.Restart();  
foreach (var item in list)  
{  
x = item;  
}  
Console.WriteLine("Elapsed={0}", sw.Elapsed);  
   
Console.WriteLine("ForNext");  
sw.Restart();  
for (int i = 0; i \< list.Count; i++)  
{  
x = list[i];  
}  
   
Console.WriteLine("Elapsed={0}", sw.Elapsed);
 ![Foreach ForNext](Exported%20image%2020250721193431-4.png)

Marginaal verschil
 
# 2/12/2021

Het laden en joinen van alle csv 's werkt.  
18 secenden en 1.4 GB geheugen gebruik.  
96228 rijen (van 1/1/2020 tot 1/12/2021) en 184 kolommen
 
96228*184=17705952
 


[Modern Time Series Analysis | SciPy 2019 Tutorial | Aileen Nielsen](https://www.youtube.com/watch?v=v5ijNXvlC5A) #time-series 
 ![Embedded YouTube video](https://www.youtube.com/embed/v5ijNXvlC5A?feature=oembed&autoplay=true)


backup van onenote

- OPC-HDA-Client-master
	- Dit haalt HDA data uit [[Sibelco/Leveranciers/ABB]] en steekt deze in [[SQL server]]. 
	  Wordt gebruikt in ABB Eng als scheduled task

```add-summary
tags: #dev 
```