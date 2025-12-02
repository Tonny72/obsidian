Tags: PP874, Local Panel
 
# Scripting

20/04/2018
 
Bij het project van BBZ (TBMA) komen er fysieke externe drukknoppen voor de bediening.
 
De functie van deze drukknoppen is afhankelijk van welk scherm wordt getoond.
 
De tag **ActiveScreenPP** wordt opgevuld met het actieve scherm nummer.
 
## Probleem:

Als er met de Panel Builder het huidige (TBMA) project wordt gerund. Dit kan zijn om een aanpassing te testen, dan zijn er twee schermen actief en wordt ActiveScreenPP door twee schermen opgevuld.
 
Dit is nefast voor de koppeling van de fysieke drukknoppen
 
## Oplossing1:

Gebruik maken van de Nonvolatile setting bij de tags.  
Dit werkt niet als er opnieuw wordt gedownload.

![Machine generated alternative text Tags Con tr oll...](../../../../../../../assets/images/Exported%20image%2020250721204222-0.png)   
## Oplossing2:

Het schrijven een Settings.xml file
 
Maar bij een download van het project naar de display wordt de file gewist.
 
## Conclusie:

Geen van de twee oplossing is optimaal. Dus gekozen voor de simpelste oplossing = Oplossing1  
Bij een herstart, moet 'Enable External Buttons' worden aangezet door de operator.
 
## Script

Roep script op als er in een input-veld wordt geschreven.

![Machine generated alternative text Builder 800 Ver...](../../../../../../../assets/images/Exported%20image%2020250721204222-1.png)   
IN DIT SCRIPT WORDT ENKEL tag User en veld UserName gebruikt  
//--------------------------------------------------------------  
// Press F1 to get help about using script.  
// To access an object that is not located in the current class, start the call with Globals.  
// When using events and timers be cautious not to generate memoryleaks,  
// please see the help for more information.  
//---------------------------------------------------------------
 
```
namespace Neo.ApplicationFramework.Generated  
{  
    using System.Windows.Forms;  
    using System;  
    using System.Drawing;  
    using Neo.ApplicationFramework.Tools;  
    using Neo.ApplicationFramework.Common.Graphics.Logic;  
    using Neo.ApplicationFramework.Controls;  
    using Neo.ApplicationFramework.Interfaces;  
      
using System.Xml;  
using System.IO;  
using System.Text;  
using System.Collections.Specialized;  
      
    public partial class ScriptModule1  
    {  
private  NameValueCollection m_settings;  
private  string m_settingsPath;



















void ScriptModule1_Created(System.Object sender, System.EventArgs e)  
{  
m_settingsPath = "Settings.xml";



if(!File.Exists(m_settingsPath))  
{   
m_settings = new NameValueCollection();  
m_settings.Add("ServerIP", "1");  
m_settings.Add("UserName", "");  
m_settings.Add("Password", "xxx");  
m_settings.Add("PhoneNumber", "123");  
m_settings.Add("TimeOut", "99");








Update();  
}


System.Xml.XmlDocument xdoc = new XmlDocument();  
xdoc.Load(m_settingsPath);  
XmlElement root = xdoc.DocumentElement;  
System.Xml.XmlNodeList nodeList = root.ChildNodes.Item(0).ChildNodes;




// Add settings to the NameValueCollection.  
m_settings = new NameValueCollection();  
m_settings.Add("ServerIP", nodeList.Item(0).Attributes["value"].Value);  
m_settings.Add("UserName", nodeList.Item(1).Attributes["value"].Value);  
m_settings.Add("Password", nodeList.Item(2).Attributes["value"].Value);  
m_settings.Add("PhoneNumber", nodeList.Item(3).Attributes["value"].Value);  
m_settings.Add("TimeOut", nodeList.Item(4).Attributes["value"].Value);







if (UserName == "") {  
Neo.ApplicationFramework.Generated.Globals.Tags.User.Value = UserName;  
}  
}

// DIT OPROEPEN ALS ER WORDT GESCREVEN IN DE USER-tag  
public void UpdateUser(){  
UserName = Neo.ApplicationFramework.Generated.Globals.Tags.User.Value;  
Update();  
}





public void Update()  
{


XmlTextWriter tw = new XmlTextWriter(m_settingsPath, System.Text.UTF8Encoding.UTF8);  
tw.WriteStartDocument();  
tw.WriteStartElement("configuration");  
tw.WriteStartElement("appSettings");




for(int i=0; i\<m_settings.Count; ++i)  
{  
tw.WriteStartElement("add");  
tw.WriteStartAttribute("key", string.Empty);  
tw.WriteRaw(m_settings.GetKey(i));  
tw.WriteEndAttribute();






tw.WriteStartAttribute("value", string.Empty);  
tw.WriteRaw(m_settings.Get(i));  
tw.WriteEndAttribute();  
tw.WriteEndElement();  
}





tw.WriteEndElement();  
tw.WriteEndElement();


tw.Close();  
}


public string ServerIP  
{  
get { return m_settings.Get("ServerIP"); }  
set { m_settings.Set("ServerIP", value); }  
}





public string UserName  
{  
get { return m_settings.Get("UserName"); }  
set { m_settings.Set("UserName", value); }  
}





public string Password  
{  
get { return m_settings.Get("Password"); }  
set { m_settings.Set("Password", value); }  
}





public string PhoneNumber  
{  
get { return m_settings.Get("PhoneNumber"); }  
set { m_settings.Set("PhoneNumber", value); }  
}





public string TimeOut  
{  
get { return m_settings.Get("TimeOut"); }  
set { m_settings.Set("TimeOut", value); }  
}





public string LastTransmit  
{  
get { return m_settings.Get("LastTransmit"); }  
set { m_settings.Set("LastTransmit", value); }  
}





public string DatabasePath  
{  
get { return m_settings.Get("DatabasePath"); }  
set { m_settings.Set("DatabasePath", value); }  
}






    }  
}




```
 
void ScriptModule1_Created(System.Object sender, System.EventArgs e)  
{  
m_settingsPath = "Settings.xml";
 
if(!File.Exists(m_settingsPath))  
{  
m_settings = new NameValueCollection();  
m_settings.Add("ServerIP", "1");  
m_settings.Add("UserName", "");  
m_settings.Add("Password", "xxx");  
m_settings.Add("PhoneNumber", "123");  
m_settings.Add("TimeOut", "99");
 
Update();  
}
 
System.Xml.XmlDocument xdoc = new XmlDocument();  
xdoc.Load(m_settingsPath);  
XmlElement root = xdoc.DocumentElement;  
System.Xml.XmlNodeList nodeList = root.ChildNodes.Item(0).ChildNodes;
 
// Add settings to the NameValueCollection.  
m_settings = new NameValueCollection();  
m_settings.Add("ServerIP", nodeList.Item(0).Attributes["value"].Value);  
m_settings.Add("UserName", nodeList.Item(1).Attributes["value"].Value);  
m_settings.Add("Password", nodeList.Item(2).Attributes["value"].Value);  
m_settings.Add("PhoneNumber", nodeList.Item(3).Attributes["value"].Value);  
m_settings.Add("TimeOut", nodeList.Item(4).Attributes["value"].Value);
 
if (UserName == "") {  
Neo.ApplicationFramework.Generated.Globals.Tags.User.Value = UserName;  
}  
}
 
// DIT OPROEPEN ALS ER WORDT GESCREVEN IN DE USER-tag  
public void UpdateUser(){  
UserName = Neo.ApplicationFramework.Generated.Globals.Tags.User.Value;  
Update();  
}
 
public void Update()  
{
 
XmlTextWriter tw = new XmlTextWriter(m_settingsPath, System.Text.UTF8Encoding.UTF8);  
tw.WriteStartDocument();  
tw.WriteStartElement("configuration");  
tw.WriteStartElement("appSettings");
 
for(int i=0; i\<m_settings.Count; ++i)  
{  
tw.WriteStartElement("add");  
tw.WriteStartAttribute("key", string.Empty);  
tw.WriteRaw(m_settings.GetKey(i));  
tw.WriteEndAttribute();
 
tw.WriteStartAttribute("value", string.Empty);  
tw.WriteRaw(m_settings.Get(i));  
tw.WriteEndAttribute();  
tw.WriteEndElement();  
}
 
tw.WriteEndElement();  
tw.WriteEndElement();
 
tw.Close();  
}
 
public string ServerIP  
{  
get { return m_settings.Get("ServerIP"); }  
set { m_settings.Set("ServerIP", value); }  
}
 
public string UserName  
{  
get { return m_settings.Get("UserName"); }  
set { m_settings.Set("UserName", value); }  
}
 
public string Password  
{  
get { return m_settings.Get("Password"); }  
set { m_settings.Set("Password", value); }  
}
 
public string PhoneNumber  
{  
get { return m_settings.Get("PhoneNumber"); }  
set { m_settings.Set("PhoneNumber", value); }  
}
 
public string TimeOut  
{  
get { return m_settings.Get("TimeOut"); }  
set { m_settings.Set("TimeOut", value); }  
}
 
public string LastTransmit  
{  
get { return m_settings.Get("LastTransmit"); }  
set { m_settings.Set("LastTransmit", value); }  
}
 
public string DatabasePath  
{  
get { return m_settings.Get("DatabasePath"); }  
set { m_settings.Set("DatabasePath", value); }  
}
   

}  
}