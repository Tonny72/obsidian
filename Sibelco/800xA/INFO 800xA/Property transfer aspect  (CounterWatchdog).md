Om in de controller connectie met 800xA te verifieren wordt het Property Transfer aspect gebruikt.
 
_Control Module Type SibelcoCommonLib2.800xAConnectionWatchog gemaakt._  
NIET VERGETEN Property Transfer Definition Disable en Enable Transfer te doen
 ![Exported image](../../../../../../../assets/images/Exported%20image%2020250721203942-0.png)  

# Property Transfer Service

In de service structure voeg bij Property Transfer, Service een Service Group toe.
 ![Exported image](../../../../../../../assets/images/Exported%20image%2020250721203943-1.png)   
Selecteer het Service Group Definition Aspect en klik op **Add**
 ![Exported image](../../../../../../../assets/images/Exported%20image%2020250721203943-2.png)  

Voeg twee Service Providers toe.
 
Selecteer een Service Provider en klik View.  
Koppel de Service provider aan een Server (800 connectivity server)

![Exported image](../../../../../../../assets/images/Exported%20image%2020250721203944-3.png)   
# Property transfer

Om waarden van 800xA naar de AC800M te sturen, moet het property transfer aspect worden toegevoegd.
 
## Voorbeeld CounterWatchdog

Maak een variable 'CounterWatchdog' aan in Counter Builder.  
Voeg op dezelde plaats in de Control Structure een 'Property Transfer Definition' aspect toe.
 ![Exported image](../../../../../../../assets/images/Exported%20image%2020250721203948-4.png)   
Er wordt van de Expression naar de Aspect/Property geschreven.