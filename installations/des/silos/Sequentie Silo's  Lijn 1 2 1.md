## Init Stap
![test](test.svg)

```d2
S1: "S1: Inlezen keuze" 
S2: "S2: (Inlezen Keuze done)"
S3: S3: Keuzestap

S1 --> S2: Wacht 5 seconden.
S2 --> S3: Wacht 5 seconden.
S3 --> S10: doelsilo = Silo1
S3 --> S20: doelsilo = Silo2
```
Spring naar:
- [[installations/des/silos/Sequentie Silo's  Lijn 1 2 1#S10 Keuze = Silo1|S10 (doelsilo = Silo 1)]]
- [[installations/des/silos/Sequentie Silo's  Lijn 1 2 1#Keuze = Silo2|Keuze = Silo2]]

# S10: Keuze = Silo1
```d2
S2 --> S3
S4: dd
explanation: |md

  # I can do headers
  - lists
  - lists
  And other normal markdown stuff
|
```
## Keuze = Silo2
```mermaid
graph LR

  Prague(Czechia, Prague) -- "✈" --> Madrid(Spain, Madrid)


class Czechia internal-link;

class Madrid internal-link;
```


